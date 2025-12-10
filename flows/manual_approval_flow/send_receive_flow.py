from uuid import UUID
from prefect import flow
from prefect.logging import get_run_logger
from prefect.input import RunInput


class MessageData(RunInput):
    """Data model for messages sent between flows."""
    message: str
    multiplier: int = 1


@flow
async def receiver_flow(greeting: str = "Hello", max_messages: int = 5):
    """
    Receives messages and sends back processed responses.
    
    Args:
        greeting: The greeting prefix to use in responses
        max_messages: Maximum number of messages to process
    """
    logger = get_run_logger()
    logger.info(f"Receiver flow started with greeting: '{greeting}', max_messages: {max_messages}")
    
    message_count = 0
    
    async for data in MessageData.receive(timeout=300):
        message_count += 1
        logger.info(f"Received message #{message_count}: '{data.message}' with multiplier: {data.multiplier}")
        
        # Process the message
        processed_message = f"{greeting}, {data.message}!" * data.multiplier
        
        # Send response back to sender
        response = MessageData(
            message=processed_message,
            multiplier=1
        )
        await data.respond(response)
        logger.info(f"Sent response: '{processed_message}'")
        
        # Stop after max_messages
        if message_count >= max_messages:
            logger.info(f"Reached max_messages limit ({max_messages}). Stopping receiver.")
            break


@flow
async def sender_flow(
    receiver_flow_run_id: UUID,
    message: str = "World",
    multiplier: int = 2,
    num_messages: int = 3
):
    """
    Sends messages to the receiver flow and waits for responses.
    
    Args:
        receiver_flow_run_id: UUID of the receiver flow run
        message: The message to send
        multiplier: Number of times to repeat the message
        num_messages: Number of messages to send
    """
    logger = get_run_logger()
    logger.info(f"Sender flow started. Sending '{message}' x{multiplier}, {num_messages} times")
    
    # Create receiver once before the loop to maintain order
    receiver = MessageData.receive(flow_run_id=receiver_flow_run_id, timeout=60)
    
    for i in range(num_messages):
        # Send message to receiver
        message_data = MessageData(message=f"{message} #{i+1}", multiplier=multiplier)
        await message_data.send_to(receiver_flow_run_id)
        logger.info(f"Sent message #{i+1}: '{message_data.message}'")
        
        # Wait for response using the same receiver iterator
        response = await receiver.next()
        logger.info(f"Received response #{i+1}: '{response.message}'")


if __name__ == "__main__":
    """
    Example usage:
    
    1. First, start the receiver flow:
       python send_receive_flow.py receiver
       
    2. Note the flow run ID from the logs
    
    3. In another terminal, run the sender flow with the receiver's flow run ID:
       python send_receive_flow.py sender <receiver_flow_run_id>
    """
    import sys
    import asyncio
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Start receiver: python send_receive_flow.py receiver")
        print("  Start sender: python send_receive_flow.py sender <receiver_flow_run_id>")
        sys.exit(1)
    
    mode = sys.argv[1]
    
    if mode == "receiver":
        # Run receiver with custom parameters
        asyncio.run(
            receiver_flow(
                greeting="Greetings",
                max_messages=10
            )
        )
    elif mode == "sender":
        if len(sys.argv) < 3:
            print("Error: receiver_flow_run_id required for sender mode")
            print("Usage: python send_receive_flow.py sender <receiver_flow_run_id>")
            sys.exit(1)
        
        receiver_id = UUID(sys.argv[2])
        # Run sender with custom parameters
        asyncio.run(
            sender_flow(
                receiver_flow_run_id=receiver_id,
                message="Python Developer",
                multiplier=1,
                num_messages=3
            )
        )
    else:
        print(f"Unknown mode: {mode}")
        print("Use 'receiver' or 'sender'")
        sys.exit(1)
