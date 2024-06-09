from enum import Enum
# learning enums
class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

# RPS(2) will print the name of the enum element
# in our case 2 is  PAPER
print(RPS(2))
print(RPS.ROCK)
# enum property names aren't strings so we need to convert
# them
print(str(RPS['ROCK']).replace('RPS.',''))
print(RPS.ROCK.value)


users = ['Dave','Jhon','Sarah']
data = ['Jhon',42,True]
print('Dave' in data)
print('Last element '+users[-1])
# prints index of Sarah
print(users.index('Sarah'))
# prints Dave and Jhon,so from up until 2,2 not included
print(users[0:2])
# prints from second element to last
print(users[1:])
# prints from -3 to -1
print(users[-3:-1])
# append = push
users.append('Elsa')
print(users)
# extend is used when we want nesting
users.extend(['Rob','BOb'])
print(users)
users.pop()
print(users)
# delete first element
del users[0]
# empty the list
data.clear()
print(data)
# add a new item at the start
users[1:2] = "Test"
print(users)

cars = [1,5,3]
cars.sort()