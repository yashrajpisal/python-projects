# simple_chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()
    if 'hello' in user_input:
        return "Hi there! How can I help you?"
    elif 'your name' in user_input:
        return "I'm a Python chatbot!"
    elif 'bye' in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand that."

# Main chat loop
print("Chatbot: Hello! Type something to start chatting (type 'bye' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
