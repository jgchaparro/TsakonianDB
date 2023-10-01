import pyperclip as pc

# Get the text from the clipboard
text = pc.paste()

# Set the diacritics replacements
replacements = {
    'λ' : 'λ̣',
    'ν' : 'ν̇',
    'ή' : 'π̇',
    'ό' : 'σ̌',
    'κ' : 'κ̇',
    'π' : 'π̇',
    'ζ' : 'ζ̌',
    'Π' : 'π̇',
}

# Replace the diacritics
for key, value in replacements.items():
    text = text.replace(key, value)

# Copy the text to the clipboard
pc.copy(text)