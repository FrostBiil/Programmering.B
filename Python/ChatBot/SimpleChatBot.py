import tkinter as tk
from tkinter import ttk
import string

# Define the dictionary of questions and answers
Q_N_A = {
    "hej": "Hej! Hvordan har du det?",
    "hvordan har du det": "Jeg har det godt, tak! Hvad med dig?",
    "jeg har det godt": "Det er godt at høre!",
    "hvad hedder du": "Jeg hedder ChatBot.",
    "hvad laver du": "Jeg er en chatbot.",
    "hvad er din yndlingsfarve": "Min yndlingsfarve er blå.",
    "hvad er din yndlingsfilm": "Min yndlingsfilm er Star Wars.",
    "among us": "sus",
}

# Function to find the response based on user input
def find_response(user_input):
    user_input = user_input.lower().translate(str.maketrans('', '', string.punctuation))
    for key_phrase, response in Q_N_A.items():
        if key_phrase in user_input:
            return response
    return "Jeg forstår ikke hvad du mener."

# Function to handle button click
def on_button_click():
    user_input = user_input_entry.get()
    response = find_response(user_input)
    
    current_chat.append(f"You: {user_input}")
    current_chat.append(f"ChatBot: {response}")
    
    response_label.config(text=response)
    user_input_entry.delete(0, tk.END)

# Function to handle Enter key press
def on_enter_key(event):
    on_button_click()

# Function to print the chat log
def print_chat_log():
    chat_log = "\n".join(current_chat)
    print(chat_log)

# Define the color scheme
soft_sky_blue = "#A6D5E5"  # Background
pale_sage_green = "#B7C4B9"  # Subtle Accents (buttons, borders, icons)
lavender_mist = "#C7B7D1"  # Headers and titles
warm_sand = "#E8D5B7"  # Content Background
muted_coral = "#FFC3A0"  # Call to Action
dusty_rose = "#E3B4B8"  # Secondary Accents
ivory_cream = "#F5F2E3"  # Text and Content

# Create the main window
root = tk.Tk()
root.title("Small talk ChatBot")
root.geometry("600x400")

# Create a style for ttk widgets
style = ttk.Style()
style.configure("TButton", foreground=ivory_cream, background=pale_sage_green)
style.configure("TLabel", foreground=soft_sky_blue, background=ivory_cream)
style.configure("TEntry", fieldbackground=soft_sky_blue, background=ivory_cream)

# Create a frame for the chat display
chat_frame = ttk.Frame(root, padding=10)
chat_frame.grid(row=0, column=0, sticky="nsew")

# Create a label for the chat display
response_label = ttk.Label(chat_frame, text="", wraplength=380, justify=tk.LEFT)
response_label.grid(row=0, column=0, sticky="w")

# Create a frame for user input
input_frame = ttk.Frame(root, padding=10)
input_frame.grid(row=1, column=0, sticky="ew")

# Create an entry widget for user input
user_input_entry = ttk.Entry(input_frame)
user_input_entry.grid(row=0, column=0, padx=5, sticky="ew")

# Bind the Enter key to the Submit button
user_input_entry.bind("<Return>", on_enter_key)

# Create a button for submitting user input
submit_button = ttk.Button(input_frame, text="Submit", command=on_button_click)
submit_button.grid(row=0, column=1, padx=5)

# Create a button to print the chat log
print_button = ttk.Button(root, text="Print Chat Log", command=print_chat_log)
print_button.grid(row=2, column=0, pady=10)

# Create an empty list to store the chat log
current_chat = []

# Configure column and row weights to make the chat frame expandable
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Set the background color of the root window
root.configure(bg=soft_sky_blue)

# Start the Tkinter main loop
root.mainloop()