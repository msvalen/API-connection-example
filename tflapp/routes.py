from flask import  render_template, request
import requests
from tflapp import app

import pandas as pd
import re
import flat_table


def get_accidents_by_vehicle(response):
    dataframe = pd.read_json(response.text)
    flat_df = flat_table.normalize(dataframe)
    vehicles = pd.DataFrame(flat_df.groupby(['vehicles.type']).size())
    vehicles = vehicles.rename(columns = {0: 'N of accidents'})
    vehicles['Vehicles'] = vehicles.index
    vehicles['Vehicles'] = vehicles['Vehicles'].apply(lambda x: re.sub('([A-Z])', r' \1', x))
    vehicles['Vehicles'] = vehicles['Vehicles'].apply(lambda x: re.sub('(_)', r' ', x))
    return vehicles

@app.route('/')
@app.route('/index')
def index():
    return render_template('form.html')


@app.route('/year', methods = ['POST'])
def get_accidents():
    if request.method == 'POST':
        year = request.form['year']

    tfl_key = app.config.get('TFL_KEY')

    if(tfl_key):
        url ='https://api.tfl.gov.uk/AccidentStats/'+year+'?app_key='+tfl_key
        response = requests.get(url)
        accident_data = get_accidents_by_vehicle(response)
        return render_template('home.html', year = year, x = accident_data, xmax = accident_data['N of accidents'].max())
    else:
        return 'TFL app key missing'

    