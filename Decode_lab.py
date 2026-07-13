def start_chatbot():
    print("==================================================")
    print("🤖 DecodeLabs Rule-Based AI Chatbot Initialized! 🤖")
    print("Type your message below. (Type 'exit', 'bye', or 'quit' to stop)")
    print("==================================================")
    while True:
        user_input = input("\nYou: ").strip().lower()
        if user_input in ['exit', 'quit', 'bye', 'goodbye']:
            print("Chatbot: Goodbye! Good luck with your DecodeLabs internship journey! 🚀")
            break
        if user_input in ['hi', 'hello', 'hey', 'greetings']:
            print("Chatbot: Hello there! I'm your rule-based AI assistant. How can I help?")
        elif "project" in user_input or "internship" in user_input:
            print("Chatbot: You're working on Project 1: Rule-Based Chatbot at DecodeLabs.")
        elif "how do you work" in user_input or "logic" in user_input:
            print("Chatbot: I follow simple if-else rules to match keywords and respond.")
        elif "how are you" in user_input:
            print("Chatbot: I'm doing well — ready to help.")
        else:
            print("Chatbot: I don't have an answer for that yet. Try asking about 'project' or say 'hi'.")

if __name__ == "__main__":
    start_chatbot()
