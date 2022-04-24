Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==================== RESTART: C:\Users\Aniss\Desktop\AIL1.py ===================
>>> 4 + 5 - 3
6
>>> 2 * 3 / 6
1.0
>>> 2**8
256
>>> import math
>>> help(math)

>>> math.sqrt
<built-in function sqrt>
>>> math.sqrt(9)
3.0
>>> from math import *
>>> sin(0.5)
0.479425538604203
>>> asin(0.4794)
0.499970899146915
>>> degrees(pi)
180.0
>>> radians(90)
1.5707963267948966
>>> log(2)
0.6931471805599453
>>> log10(10)
1.0
>>> exp(2)
7.38905609893065
>>> e**2
7.3890560989306495
>>> cosh(0.3)
1.0453385141288605
>>> fmod(13, 6)
1.0
>>> gcd(123, 321)
3
>>> 1 / 3 + 1 / 4
0.5833333333333333
>>> from fractions import Fraction
>>> Fraction(1, 3) + Fraction(1, 4)
Fraction(7, 12)
>>> pi
3.141592653589793
>>> round(_, 5)
3.14159
>>> factorial(52) # 52x51x50x...3x2x1
80658175170943878571660636856403766975289505440883277824000000000000
>>> cell(2.5)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    cell(2.5)
NameError: name 'cell' is not defined
>>> ceil(2.5)
3
>>> ceil(-2.5)
-2
>>> floor(2.5)
2
>>> floor(-2.5)
-3
>>> trunc(2.5)
2
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> 
======================= RESTART: C:/Users/Aniss/Desktop/aiwp.py =======================
>>> 
==================== RESTART: C:/Users/Aniss/Desktop/aiwp.py ===================
>>> a = [1 , 2 , 3 , 4 , 5]
>>> type(a)
<class 'list'>
>>> a[0] #this is zero-based indexing
1
>>> a[-1] #last element in list
5
>>> a[-2] #second-to-last element in the list
4
>>> len(a) #returns the size of the list
5
>>> min(a) #minimum value in list
1
>>> max(a) #maximum value in list
5
>>> 5 in a #does it belong in the list
True
>>> 7 in a
False
>>> 2 * a #number used is multiplying the list ex.
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> a.append(6) #append allows an addition to the original list
>>> print(a)
[1, 2, 3, 4, 5, 6]
>>> a.remove(6) #removes element in a list
>>> print(a)
[1, 2, 3, 4, 5]
>>> a[1 : 3] #slices the list
[2, 3]
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(100))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> list(range(4, 9))
[4, 5, 6, 7, 8]
>>> list(range(2, 10, 2))
[2, 4, 6, 8]
>>> list(range(10, 5, -2))
[10, 8, 6]
>>> A = [[1, 2], [3,4]] #list of lists, see tensors
>>> print(A)
[[1, 2], [3, 4]]
>>> A[0][1] #Accesses second element in the first list
2
>>> A[1] [0]
3
>>> names = ['jon', 'seb', 'liz']
>>> names.index('seb') #where in list of names
1
>>> names.pop(1)
'seb'
>>> print(names)
['jon', 'liz']
>>> 