'''
Exercise 12:
Use range() to create the desired output of 
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
'''
numbers= range(1,21)
print([10*num for num in numbers])

""" Long way:
newNum = []
for num in numbers:
    newNum.append(10*num)

print(newNum)

"""
