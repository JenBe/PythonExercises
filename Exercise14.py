"""
Exercise 14: Removing Duplicates
Remove the duplicates in the list a = ["1", 1, "1", 2]
Print output as a list
"""

a = ["1", 1, "1", 2]
print("Order not preserved:", list(set(a)))

'''Keep order:'''
from collections import OrderedDict
print("Order preserved:", list(OrderedDict.fromkeys(a)))
