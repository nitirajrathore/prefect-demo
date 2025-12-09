FROM prefecthq/prefect:3.6.5-python3.12
COPY ../../ /opt/prefect/prefect-demo
WORKDIR /opt/prefect/prefect-demo/
RUN cat flows/manual_approval_flow/requirements.txt || echo "requirements.txt not found"
RUN python -m pip install -r flows/manual_approval_flow/requirements.txt
