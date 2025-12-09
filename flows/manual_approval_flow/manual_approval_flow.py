from prefect import flow, task, pause_flow_run
from pydantic import BaseModel, Field
import platform
import sys

class UserInput(BaseModel):
    message: str = Field(..., description="Enter a message to continue the flow")

@task
def log_environment():
    print(f"Running on host: {platform.node()}")
    print(f"Python version: {sys.version}")

@task
def print_user_message(message: str):
    print(f"User entered: {message}")

@flow(log_prints=True)
def container_flow():
    print("Hello from Flow1!")
    log_environment()

@flow(log_prints=True)
def interactive_flow():
    print("Hello from interactive flow!")
    log_environment()
    user_input = pause_flow_run(wait_for_input=UserInput, timeout=3600)
    print_user_message(user_input.message)

if __name__ == "__main__":
    # Uncomment the flow you want to run
    # container_flow()
    interactive_flow()