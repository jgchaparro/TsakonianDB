# This script is used to convert Standard Greek active verbs into passive verbs
# for efficient data entry into the Tsakonian Database.

import pyperclip as p

cb = p.paste().strip()

# Check whether the clipboard is Greek or Tsakonian

lang = 'el' if cb[:-1] in 'ωώ' else 'ts'

# Change clipboard depending on language

if lang == 'el':
    cb = cb[:-1]
    cb += 'ομαι'

else:
    # Not working for all passive verbs
    cb = cb[:-2]
    # Remove accents
    cb = cb.translate(str.maketrans('άέήίόύώ', 'αεηιουω'))
    cb += 'ούμενε'

# Copy to clipboard
p.copy(cb)