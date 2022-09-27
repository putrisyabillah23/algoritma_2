# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:11:23 2022

@author: putri
"""
import math
t1 = float(input("lattitude kota jakarta"))
f1 = float(input("longtitude kota jakarta"))

t2 = float(input("lattitude kota yogyakarta"))
f2 = float(input("longtitude kota yogyakarta"))

dlat = t2 - t1
dlon = f2 - f1

x = math.sin(math.radians(dlat/2)) ** 2 + math.cos(math.radians(t1)) * math.cos(math.radians(t2)) * math.sin(math.radians(dlon/2)) ** 2

b = 2 * math.asin(math.sqrt(x))

r = 6371.01

print ('\njarak antara dua titik adalah', b*r , 'km')
