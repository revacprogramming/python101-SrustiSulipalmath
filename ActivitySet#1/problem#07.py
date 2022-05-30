# Strings

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0.8475')
float(text[pos:])
print(text[pos:])
