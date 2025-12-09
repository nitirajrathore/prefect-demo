## Build the image


```
export FLOW_IMAGE_TAG="dockerreg:5000/prefectdemo.containerflow:latest"
```

```
docker build --progress=plain --no-cache -f flows/container_flow/Dockerfile . -t $FLOW_IMAGE_TAG
```


