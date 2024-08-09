Active code page: 65001

C:\Users\Sarvesh\Desktop\Python\04_iteration_tools>python
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> f = open('chai.py')  
>>> f.readline()
'import time\n'
>>> f.readline()
'print("chai is here")\n'
>>> f.readline()
'username = "Sarvesh"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''
>>> f.readline()
''
>>> f = open('chai.py') 
>>> f.__next__()
'import time\n'
>>> f.__next__()        
'print("chai is here")\n'
>>> f.__next__()
'username = "Sarvesh"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
StopIteration
>>>
>>> 
>>> for line in open('chai.py'):
...     print(line)
... 
import time

print("chai is here")

username = "Sarvesh" 

print(username)      
>>>
>>> 
>>> for line in open('chai.py'):
...     print(line,end = '')
... 
import time
print("chai is here")
username = "Sarvesh"
print(username)>>>
>>> 
>>> 
>>> f = open('chai.py')  
>>> while True:
...     line = f.readline()
...     if not line: break 
...     print(line, end = '')
... 
import time
print("chai is here")
username = "Sarvesh"
print(username)>>>
>>> 
>>> 
>>> test = "hitesh" 
>>> if not test:
...     print("chai")
... 
>>> test = ""
>>> if not test:
...     print("chai")
... 
chai
>>>
>>> 
>>> myList = [1, 2, 3, 4]
>>> I = iter(myList)     
>>> I
<list_iterator object at 0x0000025CCEC9BBB0>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x0000025CCEC9BBB0>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
>>> 
>>> 
>>> 
>>> f = open('chai.py') 
>>> iter(f) is f
True
>>> iter(f) is f.__iter__() 
True
>>>
>>> 
>>> myNewList = [1, 2, 3] 
>>> iter(myNewList) is myNewList
False
>>>
>>> 
>>> D = {'a': 1, 'b':2}
>>> for key in D.keys():
...     print(key)
... 
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x0000025CCEA42070>
>>> next(I) 
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
>>> 
>>> range(5)
range(0, 5)
>>> R = range(5)
>>> R
range(0, 5)
>>> I = iter(R) 
>>> next(I)      
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>