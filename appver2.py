import tkinter as tk
from tkinter import scrolledtext, simpledialog
import json
import os

# ---------- Load or initialize responses ----------
if os.path.exists("responses.json"):
    with open("responses.json", "r", encoding="utf-8") as f:
        responses = json.load(f)
else:
    responses = {
        "hello": "Hello! How are you today?",
        "hi": "Hey there! Nice to meet you!",
        "how are you": "I’m great, thanks for asking!",
        "what is your name": "I’m Chatty v4, your friendly AI assistant!",
        "who created you": "I was created by Norbert!",
        "bye": "Goodbye! Have a wonderful day!",
        "default": "I don’t know that yet. Can you teach me what to reply?"
    }

def save_responses():
    """Save all responses to the file."""
    with open("responses.json", "w", encoding="utf-8") as f:
        json.dump(responses, f, ensure_ascii=False, indent=4)

# ---------- Smart response logic ----------
def get_response(user_input):
    """Return bot response or ask to learn a new one."""
    user_input_clean = user_input.lower().strip()
    normalized_responses = {k.lower(): v for k, v in responses.items()}

    if user_input_clean in normalized_responses:
        return normalized_responses[user_input_clean]
    elif user_input_clean == "bye":
        return normalized_responses["bye"]
    else:
        chat_box.insert(tk.END, f"\nChatty: {responses['default']}\nYou can type your answer below 👇\n", "bot")
        chat_box.see(tk.END)
        window.update()

        new_response = simpledialog.askstring("Teach Chatty", f"What should I reply when someone says '{user_input}'?")
        if new_response:
            responses[user_input_clean] = new_response
            save_responses()
            return "Got it! I’ve learned something new 😊"
        else:
            return "Okay, maybe next time!"

def send_message(event=None):
    """Send user message and get response."""
    user_input = user_entry.get().strip()
    if not user_input:
        return

    chat_box.insert(tk.END, f"\nYou: {user_input}", "user")
    user_entry.delete(0, tk.END)

    response = get_response(user_input)
    chat_box.insert(tk.END, f"\nChatty: {response}\n", "bot")
    chat_box.see(tk.END)
    
# ---------- GUI Setup ----------
window = tk.Tk()
window.title("🤖 Chatty v4 - Smart AI Assistant")
window.geometry("600x650")
window.config(bg="#1F1F1F")
window.resizable(False, False)

# Chat history area
chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=65, height=28, bg="#2C2F33", fg="#FFFFFF", font=("Consolas", 11))
chat_box.pack(padx=10, pady=10)
chat_box.tag_config("user", foreground="#61AFEF")
chat_box.tag_config("bot", foreground="#98C379")

# User input
user_entry = tk.Entry(window, width=50, font=("Consolas", 12))
user_entry.pack(padx=10, pady=5, side=tk.LEFT, fill=tk.X, expand=True)
user_entry.bind("<Return>", send_message)

# Send button
send_button = tk.Button(window, text="Send", command=send_message, bg="#61AFEF", fg="white", font=("Consolas", 12, "bold"))
send_button.pack(padx=10, pady=5, side=tk.RIGHT)

# Welcome message
chat_box.insert(tk.END, "🤖 Chatty v4 is online! Type something below to start chatting...\n", "bot")

window.mainloop()
