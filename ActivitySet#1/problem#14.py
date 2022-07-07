# Using Web Services
# https://www.py4e.com/lessons/servces

import urllib.request, urllib.parse, urllib.error 

import xml.etree.ElementTree as ET

url = input('Enter location: ')

archivo = urllib.request.urlopen(url)

data = archivo.read()

print('Retrieving', len(data), 'characters') 

xml_data = ET.fromstring(data)

lst = xml_data.findall('.//count')  

Cont = len(lst)    
print("Count:", Cont)  

lista = [int(item.text) for item in lst]   
print("Sum:", sum(lista))