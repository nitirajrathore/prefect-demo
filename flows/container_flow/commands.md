## Build the image



```
export FLOW_IMAGE_TAG="dockerreg:5000/prefectdemo.containerflow:latest"
```

```
docker build --progress=plain --no-cache -f flows/container_flow/Dockerfile . -t $FLOW_IMAGE_TAG
```

## set prefect server api
```
export PREFECT_API_URL="http://localhost:4200/api"
```

### check prefect configs
```
prefect config view
```

