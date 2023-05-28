# vue-project-2022

## Project setup

### Project build
```
docker build -t grooming_fast:latest .
```

### Project run
```
docker run -it --name grooming_server grooming_fast:latest
```

### Project run (Instant Testing)
```
docker run -it --name grooming_server --rm grooming_fast:latest
```

### Container -> Host connection?
See [Official Docker Reference](https://docs.docker.com/desktop/networking/) or [Korean Reference](https://yoo11052.tistory.com/143)
