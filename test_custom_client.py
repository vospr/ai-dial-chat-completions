import asyncio

from task.clients.custom_client import CustomDialClient
from task.constants import DEFAULT_SYSTEM_PROMPT
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role


async def start(stream: bool) -> None:
    # Using CustomDialClient to see full request/response
    client = CustomDialClient(deployment_name="applications/public/gpt-4o")
    
    # Create Conversation object
    conversation = Conversation()
    
    # Get System prompt from console or use default
    print("Provide System prompt or press 'enter' to continue.")
    system_prompt = input("> ").strip()
    if not system_prompt:
        system_prompt = DEFAULT_SYSTEM_PROMPT
    
    # Add system message to conversation
    conversation.add_message(Message(role=Role.SYSTEM, content=system_prompt))
    
    print("\nType your question or 'exit' to quit.")
    
    # Infinite cycle
    while True:
        # Get user input
        user_input = input("> ").strip()
        
        # Check if user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting the chat. Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Add user message to conversation history
        conversation.add_message(Message(role=Role.USER, content=user_input))
        
        # Call appropriate completion method
        if stream:
            ai_message = await client.stream_completion(conversation.get_messages())
        else:
            ai_message = client.get_completion(conversation.get_messages())
        
        # Add generated message to history
        conversation.add_message(ai_message)


if __name__ == "__main__":
    asyncio.run(start(True))

