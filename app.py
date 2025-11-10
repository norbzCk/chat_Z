import os
import json

if os.path.exists("responses.json"):
    with open("responses.json", "r", encoding="utf-8") as f:
        response = json.load(f)  
else:
    response = {
        "niaje": "Freshi, mabo vipi",
        "mambo": "Poaa,",
        "hello": "Helloo",
        "how are you": "am good, how about you",
        "who are you": "Am an AI built by Norbz",
        "we nani": "Naitwa Chatty, AI nimetengenezwa na Norbz",
        "bye": "Goodbye! Have a nice day!",
        "default": "Sorry, I don't understand that!"
    }   

def save_responses():
    """Save the updated responses dictionary to the file."""
    with open("responses.json", "w", encoding="utf-8") as f:
        json.dump(response, f, ensure_ascii=False, indent=4)  

def chatbot():
    print("Karibu! I'm Chat_Z. I can learn new responses. Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "bye":
            print("Chat_Z:", response["bye"])
            save_responses()  
            break

        if user_input in response:
            print("Chat_Z:", response[user_input])
        else:
            print("Chat_Z: I don't know that yet. How should I respond?")
            new_reply = input("You teach Chatty: ").strip()
            response[user_input] = new_reply
            print("Chat_Z: Got it! I will remember that.")
            save_responses()  

chatbot()
