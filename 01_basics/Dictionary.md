Microsoft Windows [Version 10.0.19045.4412]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Sarvesh\Desktop\Python>python
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
>>> 
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Masala"] 
'Spicy'
>>>    
>>> chai_types.get("Ginger") 
'Zesty'
>>>    
>>> chai_types["Ginger"] = "Fresh" 
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Fresh', 'Green': 'Mild'}
>>>
>>> for chai in chai_types:
...     print(chai)
... 
Masala
Ginger
Green 
>>> for chai in chai_types:
...     print(chai, chai_types[chai])
... 
Masala Spicy
Ginger Fresh
Green Mild  
>>>
>>> 
>>> for key, value in chai_types.items():
...     print(key, value)
... 
Masala Spicy
Ginger Fresh
Green Mild
>>> if "Masala" in chai_types:
...     print("I have Masala Chai")
... 
I have Masala Chai
>>> print(len(chai_types)) 
3
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Fresh', 'Green': 'Mild'}
>>>
>>> chai_types["Earl Grey"] = "Citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Fresh', 'Green': 'Mild', 'Earl Grey': 'Citrus'}
>>>
>>> chai_types.pop("Ginger") 
'Fresh'
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Mild', 'Earl Grey': 'Citrus'}
>>> chai_types.popitem()    
('Earl Grey', 'Citrus')
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Mild'}
>>>
>>> del chai_types["Green"] 
>>> chai_types
{'Masala': 'Spicy'}
>>>
>>> 
>>> chai_types_copy = chai_types.copy()
>>> 
>>> tea_shop = { 
... "chai": {"Masala" : "Spicy", "Ginger" : "Zesty"},
... "Tea" : {"Green": "Mild", "Black": "Strong"} 
... }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> print(tea_shop) 
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>>
>>> tea_shop["chai"] 
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"] 
'Zesty'
>>>
>>> 
>>> 
>>> squared_num = {x: x**2 for x in range(6)}  
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> squared_num
{}
>>>
>>> 
>>> keys = ["Masala", "Ginger", "Lemon"]
>>> keys
['Masala', 'Ginger', 'Lemon']
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys, default_value)
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> new_dict = dict.fromkeys(keys, keys)
>>> new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
>>>