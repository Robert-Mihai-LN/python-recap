#1) Sum and multiplication of 2 numbers
num1 = 3
num2 = 4
print(num1*num2)
print(num1+num2)

#2) Sum of current number and previous number
n=10
for i in range(n):
    x = 0
    if i == 0 and x == 0:
        print('Current = '+str(x)+
              '\n Previous'+str(i))
    else:
        x=i+1
        print('Current = '+str(x)+ '\n Previous ='+
              str(i))

#3) Display characters that are present at an even
# index number.
str_ = "pynative"
# Even  = 2,4,6,8
for i in range(len(str_)):
    if i % 2 == 0:
        print(str_[i])

#4) Remove n first characters from a string
def remove_chars(stringInput,n):
    return stringInput[n:]

result = remove_chars("Zoltan",4)
print(result)

#5) Check if first and last number in a list are the same
numbers_x = [10, 20, 30, 40, 50]
numbers_y = [75, 66, 35, 75, 30]

#6)
def compareFirstLast(arr):
    return arr[0] == arr[-1]
print(compareFirstLast(numbers_x))
print(compareFirstLast(numbers_y))

# Iterate the given list of numbers and print
# only those numbers which are divisible by 5
def numbersDivisibleByFive(nums):
    for i in nums:
        if i%5 == 0:
            print(i)
numbersDivisibleByFive(numbers_y)

# Write a program to see how many times a given substring
# can be found in a string
str_x = "Emma is good developer. Emma is a writer"
print(str_x.count("Emma"))

# del str -> Avoid using del on built-in names like str

# Write a star ladder pattern python
for i in range(1, 10):
    print("*" * i)

# Palindrome checker python
newStr = ''.join(reversed(str_x))
print(newStr)

def oddEvenNums(arr1,arr2):
    oddNums = filter(lambda x: x % 2 != 0, arr1)
    evenNums = filter(lambda x: x % 2 == 0, arr2)
    return list(oddNums) + list(evenNums)

print(oddEvenNums([1,2,3],[4,1,8,7]))

# List comprehension is an easy way to structure your for loops
numbers = [1,2,3,4,5,6,7,8]
# <expression> for <variable in range>  <condition>
# E.g  num!=2 for num in range(15) if num==3
listComprehension = [num*2 for num in numbers if num>0]
listComprehension.sort(reverse=True)
print(listComprehension)