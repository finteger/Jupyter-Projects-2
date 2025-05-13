#this is a comment
x = 5
print(x)

''' 
This is an example of a tuple. 
Tuples are ordered arrays that cannot change.
'''
mytuple = ('honda', 'toyota', 'ford')

#lists (arrays)
list = ['apple', 'cherry', 'orange']

#data dictionaries. key-value or object like collections
dictionary = {'Todd': 38, 'Janet': 60, 'Bob': 90}

#if-else conditional logic
a = 33
b = 220

if a > b:
    print('a is greater than b')
elif a < b:
    print('b is greater than a')   
else:
    print('a is equal to b')    
    
#looping in python
colours = ['red', 'green', 'grey', 'blue']

# for-in loop
for x in colours:
    print(x)
    
 #while loop

i = 1
while i < 10:
    print(i)
    i += 1        
    
#functions
def add(a, b):
    return a + b

print(add(14, 5))      

#casting
x = int(1) 
b = float(2.33)
v = str(23)
    
    