from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


# Create a new chatbot instance
chatbot = ChatBot(
    'MyBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',  # To store training data in a database
    logic_adapters=[
        'chatterbot.logic.BestMatch',  # Matches the best response
        'chatterbot.logic.MathematicalEvaluation'  # Evaluate mathematical expressions
    ],
    database_uri='sqlite:///database.db'  # This stores the conversations in an SQLite database
)

# Train the chatbot using the English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')  # You can train it with different languages



def chat_with_bot():
    print("Hello! I'm your chatbot. Type 'exit' to stop chatting.")
    
    while True:
        try:
            user_input = input("You: ")
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break

            # Get the chatbot's response
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")

        except (KeyboardInterrupt, EOFError, SystemExit):
            break



trainer = ListTrainer(chatbot)

# Train the bot with custom data
trainer.train([
    "Hi, how can I help you?",
    "What is your name?",
    "I am a chatbot.",
    "What do you do?",
    "I help with tasks!"
])


if __name__ == "__main__":
    chat_with_bot()
