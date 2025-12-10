
version=$(date +"%Y%m%d%H%M%S")
# export FLOW_IMAGE_TAG="dockerreg:5000/prefectdemo.manual_approval_flow:$version"
export FLOW_IMAGE_TAG="dockerreg:5000/prefectdemo.manual_approval_flow:latest"
echo "creating new image : $FLOW_IMAGE_TAG"
docker build --progress=plain --no-cache -f flows/manual_approval_flow/Dockerfile . -t $FLOW_IMAGE_TAG

docker push $FLOW_IMAGE_TAG