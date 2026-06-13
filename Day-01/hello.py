print("hello world")
# variable = no let or const in python
name = "John"
age = 30

print(name)
print(age)

# python dada type 
# - str
# - int
#  - float
# - bool 
# - list
# - tuple
# - dict
# - set 


# input  and output
# name = input("Enter your name : ")
# while name == "":
#     name = input("Enter your name : ")

# print(name)



# Arrays → Lists
arr = [1, 2, 3]
arr.append(4)        # push()
arr.pop()            # pop()
arr[0]               # indexing same


# Objects in python are called dictionaries
person = { "name": "John", "age": 30 }
print(person)
print(person["name"])   # person.name


#  assign value or change value 
person["name"] = "Mohan Lal"
print(person)  

person.get("age")    # safe access (like optional chaining)



# Arrow fn → Lambda / regular def
double = lambda x: x * 2  # const double = x => x * 2
print(double(3))  

def add(a,b):
    return a+b;

print(add(10,20))  



#map/filter 

nums = [2,3,5]


# in javascript
# const nums = [1, 2, 3, 4];

# function double(x) {
#     return x * 2;
# }

# const doubled = nums.map(double);

# console.log(doubled);

def double(x):
    return x*2

nums = [1,2,3,4]
doubleData = list(map(double,nums))
print(doubleData)


#modify abcode using lambda

doubleLambda = list(map(lambda x :x*2,nums))
print(doubleLambda)


squared = map(lambda x: x ** 2,nums )

print(list(squared))  


# map
# map(function, iterable, ...)

# nums = [1,20,60,50]
list(map(print,nums))


#lambda and  print format 

list(map(lambda x : print(f"the number is {x}"),nums))




#filter 

nums2 = [1, 2, 3, 4, 5, 6]

# function isEven(num) {
#     return num % 2 === 0;
# }

# const evens = nums.filter(isEven);


#python 


def isEven(x):
    return  x%2 == 0

even = list(filter(isEven,nums2))
print(even)


# map / filter
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, nums))     # nums.map(x => x*2)
evens = list(filter(lambda x: x%2==0, nums)) # nums.filter(x => x%2===0)





# String Method 
str = "Hello world"
print(str.upper())  # upper case 


print(str.split(" "))




# loop
for x in range(10,20,2):
    print(x)


is_completed = False
while is_completed:
    print(f"hello brother")