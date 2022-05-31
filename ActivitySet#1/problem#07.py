# Strings

text = "X-DSPAM-Confidence:    0.8475"
x = text.find('0.8475')
num=text[x:]
val=float(num)
print(val)