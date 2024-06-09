# Insert at specific index :
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,
 "lemon")
## Add a placeholder
age = 36
txt = "My name is John, and I am  {}"
print(txt.format(age))

print('Name','ls','James',sep='**')

#Declaring a set (similar to a set in apex
sample_set = {'Banana','Grapes','Milk'}

#1)Given a Python list, Write a program to add all its elements into a given set.
list2Set = set([1,2,2,3])
print(list2Set)

#2) Return a new set of identical items from two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z  = y.intersection(x)
print(z)

q = x.union(y)
print(q)

# ordered collection and unchangeable
myTouple = (1,2,3)
# adding items to a touple
myTouple += (4,5)
myTouple += (6,)
print(myTouple)