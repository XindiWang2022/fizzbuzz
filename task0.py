# -*- coding: utf-8 -*-
"""task0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dRRG18Tk8MlBXSckUy6RoSEeNFqJv8Nf
"""

for i in range(1,101):
  if i % 5 == 0:
    if i % 3 == 0:
      print("FizzBuzz")
    else:
      print("Buzz")
  elif i % 3 ==0:
    print("Fizz")
  else:
    print(i)