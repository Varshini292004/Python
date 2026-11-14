#Swap two variables without using a third variable.

a = 20
b = 10

"""
logic1
a , b = b , a
"""

#logic2 (arithmetic)
a = a + b # 20+10=30
b = a - b # 30-10=20
a = a - b # 30-20=10

print("a= ",a)
print("b= ",b)