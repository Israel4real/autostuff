#! /usr/bin/python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Seperate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in 'lines'
    lines[i] = '* ' + lines[i]   # add star in front of element

text = '\n'.join(lines)

pyperclip.copy(text)

