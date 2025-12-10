## Build the image
```
export FLOW_IMAGE_TAG="dockerreg:5000/prefectdemo.manual_approval_flow:latest"
```
```
docker build --progress=plain --no-cache -f flows/manual_approval_flow/Dockerfile . -t $FLOW_IMAGE_TAG
```

## build image with script


## Run receiver flow

```

```
## Run sender flow

```
prefect deployment run sender-flow/sender --param receiver_flow_run_id=$RECEIVER_FLOW_ID
```
