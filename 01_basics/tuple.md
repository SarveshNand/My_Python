Microsoft Windows [Version 10.0.19045.4412]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Sarvesh\Desktop\Python>python
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> tea_types = ("Black", "Green", "Oolong") 
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[0] 
'Black'
>>> tea_types[-1] 
'Oolong'
>>> tea_types[1:] 
('Green', 'Oolong')
>>> tea_types[0] = "Lemon" 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
>>> len(tea_types) 
3   
>>> more_tea = {"Herbal", "Earl Grey"} 
>>> all_tea = more_tea + tea_types
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'set' and 'tuple'
>>>
>>> 
>>> more_tea = ("Herbal", "Earl Grey") 
>>> all_tea = more_tea + tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
>>> if "Green" in all_one:
...     print("I have green tea")
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'all_one' is not defined
>>> if "Green" in all_tea:
...     print("I have green tea")
... 
I have green tea
>>>
>>> 
>>> more_tea = ("Herbal", "Earl Grey", "Herbal") 
>>> more_tea
('Herbal', 'Earl Grey', 'Herbal')
>>> more_tea.count("Herbal") 
2
>>> more_tea.count("Herb")
0
>>> tea_types
('Black', 'Green', 'Oolong')
>>> (black, green, Oolong) = tea_types
>>>
>>> black
'Black'
>>> type(tea_types)
<class 'tuple'>