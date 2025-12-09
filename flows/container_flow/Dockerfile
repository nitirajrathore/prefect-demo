FROM prefecthq/prefect:3.6.5-python3.12
COPY ../../ /opt/prefect/prefect-demo
WORKDIR /opt/prefect/prefect-demo/
RUN ls -la .
RUN ls -la flows/container_flow/
RUN cat flows/container_flow/requirements.txt || echo "requirements.txt not found"
RUN python -m pip install -r flows/container_flow/requirements.txt
