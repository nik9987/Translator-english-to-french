# Importing necessary libraries
from tkinter import scrolledtext

from googletrans import Translator
import tkinter as tk

# Setting up the translator
translator = Translator()

# Creating the GUI
root = tk.Tk()
root.title("Translator Chatbot")

# create the input field
input_field = tk.Entry(root, width=40)


# Defining the function to translate text
def translate_text():
    text_to_translate = input_text.get("1.0", "end-1c")
    translated_text = translator.translate(text_to_translate,dest='fr')
    output_text.delete("1.0", "end")
    output_text.insert("1.0", translated_text.text)

# Creating the input and output text widgets
input_label = tk.Label(root, text="Enter text to translate:", bg="sky blue")
input_label.pack()
input_text = tk.Text(root, height=10, width=50, bg="CadetBlue1")
input_text.pack()

output_label = tk.Label(root, text="Translated text:",bg="sky blue")
output_label.pack()
output_text = tk.Text(root, height=10, width=50,bg="CadetBlue1")
output_text.pack()

# Creating the translate button
translate_button = tk.Button(root, text="Translate",command=translate_text,bg="sky blue",highlightcolor="yellow", activebackground="green",activeforeground="white")
translate_button.pack()

# Running the GUI loop
root.mainloop()

