Microsoft Windows [Version 10.0.19045.4412]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Sarvesh\Desktop\Python>python
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> tea_varieties = ["Black", "Green", "Oolong", "White"]
>>> tea_varities
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tea_varities' is not defined. Did you mean: 'tea_varieties'?
>>> tea_varieties
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varieties)
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varieties[0])
Black
>>> print(tea_varieties[-2]) 
Oolong
>>> print(tea_varieties[1:3]) 
['Green', 'Oolong']
>>> print(tea_varieties[3])   
White
>>> tea_varieties[3] = "Herbal" 
>>> print(tea_varieties)        
['Black', 'Green', 'Oolong', 'Herbal']
>>> tea_varieties[1:2] = "Lemon" 
>>> tea_varieties
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> tea_varieties[1:2] = ["Lemon"] 
>>> tea_varieties
['Black', 'Lemon', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> tea_varieties = ["Black", "Green", "Oolong", "White"]
>>> tea_varities
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tea_varities' is not defined. Did you mean: 'tea_varieties'?
>>> tea_varieties
['Black', 'Green', 'Oolong', 'White']
>>>
>>>
>>> tea_varities = ["Lemon"]
>>> tea_varieties
['Black', 'Green', 'Oolong', 'White']
>>> tea_varieties[1:2] = ["Lemon"]
>>> tea_varieties
['Black', 'Lemon', 'Oolong', 'White']
>>>
>>>
>>> tea_varieties[1:3] = ["green", "Masala"]
>>> tea_varieties
['Black', 'green', 'Masala', 'White']
>>> tea_varieties[1:1]
[]
>>>
>>> 
>>> tea_varieties[1:1] = ["test", "test"] 
>>> tea_varieties      
['Black', 'test', 'test', 'green', 'Masala', 'White']
>>>
>>> 
>>> tea_varieties[1:3] = []
>>> tea_varieties
['Black', 'green', 'Masala', 'White']
>>>
>>> 
>>> for tea in tea_varieties:
...     print(tea)
... 
Black
green
Masala
White
>>> for tea in tea_varieties:
...     print(tea, end="-")
... 
Black-green-Masala-White->>> 
>>> 
>>> 
>>> tea_varieties
['Black', 'green', 'Masala', 'White']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong Tea")
...
>>> tea_varieties.append("Oolong")
>>> tea_varieties                )
['Black', 'green', 'Masala', 'White', 'Oolong']
>>>
>>> if "Oolong" in tea_varieties:
...     print("I have Oolong Tea")
...
I have Oolong Tea
>>>
>>> tea_varieties
['Black', 'green', 'Masala', 'White', 'Oolong']
>>> tea_varieties.pop()
'Oolong'
>>> tea_varieties
['Black', 'green', 'Masala', 'White']
>>>
>>> 
>>> tea_varieties.remove("green")
>>> tea_varieties
['Black', 'Masala', 'White']
>>>
>>> 
>>> tea_varieties
['Black', 'Masala', 'White']
>>> tea_varieties.insert(1, "green") 
>>> tea_varieties
['Black', 'green', 'Masala', 'White']
>>> tea_varieties_copy = tea_varieties.copy()
>>> tea_varities_copy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tea_varities_copy' is not defined. Did you mean: 'tea_varieties_copy'?
>>>
>>> 
>>> tea_varieties_copy()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>>     
>>> 
>>> tea_varieties_copy
['Black', 'green', 'Masala', 'White']
>>> tea_varieties_copy.append("Lemon") 
>>> 
>>> tea_varities
['Lemon']
>>>
>>> tea_varieties
['Black', 'green', 'Masala', 'White']
>>>
>>> tea_varieties_copy
['Black', 'green', 'Masala', 'White', 'Lemon']
>>>
>>> 
>>> 
>>> 
>>> range(10)
range(0, 10)
>>> print(range(10)) 
range(0, 10)
>>> y = range(10) 
>>> y
range(0, 10)
>>>
>>>
>>>
>>> squared_nums = [x**2 for x in range(10)]
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_nums = [y**3 for y in range(5)]
>>> cube_nums
[0, 1, 8, 27, 64]
>>>
>>> lst = [1, 2, 3, 4]
>>> lst.extend([8,9])               // Similar like append but it adds the element in a separate way
[1, 2, 3, 4, 8, 9]
>>>
>>>
>>> lst = [1, 2, 2, 3, 4, 5]
>>> lst.count(2)
2
>>> lst.index(1, 2, 4)
1
>>> lst = [1, 2, 3, 4, 5, 6]
>>> len(lst)
6