# TfL API

Line Status Endpoint:
>https://api-portal.tfl.gov.uk/api-details#api=AccidentStats&operation=AccidentStats_Get&definition=Tfl.Api.Presentation.Entities.AccidentStats.AccidentDetail
>

**It is important to substitude _$TFL_KEY_ in the dockerfile with the actual key.**

# Docker instructions
```
docker build . -t flapp
docker run -p 8080:5000 flapp
```

# Docker Compose Alternative Instructions

```
docker-compose up
```

You will find the app in the port 8080
