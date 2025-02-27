from shiny import Inputs, Outputs, Session, render, ui


def server(input: Inputs, output: Outputs, session: Session):
    # Create a chat instance and display it
    chat = ui.Chat(id="chat")  

    # Define a callback to run when the user submits a message
    @chat.on_user_submit  
    async def _():  
        # Simply echo the user's input back to them
        await chat.append_message(f"You said: {chat.user_input()}") 