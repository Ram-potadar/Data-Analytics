import os

a = ['a','b','c', 'd']
b = ['21', '31', '41', '51']

# for i, j in zip(a,b):
#     print(i, " ", j)

r = {}

for i,j in zip(a,b):
    r[i] = j

r['j'] = 87



print(r)