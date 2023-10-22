import tkinter as tk
import pyperclip as pc

pages = {
    'a' : 23, 'α' : 23,
    'b' : 88, 'β' : 88, 
    'g' : 106, 'γ' : 106,
    'd' : 120, 'δ' : 120, 
    'e' : 137, 'ε' : 137,
    'z' : 159, 'ζ' : 159,
    'h' : 167, 'η' : 167,
    'u' : 168, 'θ' : 168,
    'i' : 174, 'ι' : 174,
    'k' : 176, 'κ' : 176,
    'l' : 232, 'λ' : 232, 
    'm' : 241, 'μ' : 241,
    'n' : 263, 'ν' : 263,
    'j' : 272, 'ξ' : 272,
    'o' : 285, 'ο' : 285,
    'p' : 297, 'π' : 297,
    'r' : 331, 'ρ' : 331,
    's' : 337, 'σ' : 337,
    't' : 372, 'τ' : 372,
    'y' : 396, 'υ' : 396,
    'f' : 398, 'φ' : 398,
    'x' : 406, 'χ' : 406,
    'c' : 415, 'ψ' : 415,
    'v' : 420, 'ω' : 420,

}


def submit(event=None):
    # This function will be called when any key is pressed
    user_input = event.char
    pc.copy(pages[user_input])
    window.destroy()  # Close the window

# Create the main window
window = tk.Tk()
window.title("Input Window")

# Create a label
label = tk.Label(window, text="Press any key:")
label.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(window)
entry.pack(pady=10)

# Set focus on the entry widget
entry.focus_set()

# Bind any key press to the submit function
entry.bind('<Key>', submit)

# Start the GUI event loop
window.mainloop()
