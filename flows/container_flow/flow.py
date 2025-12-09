from prefect import flow, task
import platform
import sys

@task
def log_environment():
    print(f"Running on host: {platform.node()}")
    print(f"Python version: {sys.version}")

@flow(log_prints=True)
def container_flow():
    print("Hello from Flow1!")
    log_environment()

if __name__ == "__main__":
    container_flow()