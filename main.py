# THE PASSING MECHANISM FOR ALL PRIMITIVE DATA TYPES IN PYTHON IS PASS BY VALUE
# WHICH MEANS THAT IF YOU CHANGE THE VALUE INSIDE THE METHOD IT DOESNT CHANGE THE ORIGINAL

# WHEN A PARAMETER IS PASSED BY REFERENCE THE VALUE CAN BE CHANGED BY THE METHOD AND IS CHANGED OUTSIDE AND INSIDE THE METHOD

# FUNCTIONS IDEALLY RETURNS A VALUE WITH NO CHANGES TO THE STATE OF THE APPLICATION
# PROCEDURES CHANGES STATE OF THE APPLICATION
# IN PYTHON THIS IS ONLY CONCEPTUAL



# from MyClass import MyClass


# aMyClass = MyClass()
# aMyClass.aString = "Hello World Replacement"
# aMyClass.appendAString("!!!")
# print(aMyClass.aString)



# LIST IN PYTHON []
# CAN BE OF DIFFERENT TYPES

myList = [1, 2, 3, 4, 5]
myList2 = ["1", 2 ,True]
variable_name_dictionary = {"myList": myList, "myList2": myList2, }

for name, value in variable_name_dictionary.items():
    print("The length of {} is: {}".format(name, len(value)))

for anItem in myList2:
    print(anItem)

print("---------------------")


# TUPLES IN PYTHON ()
# TUPLES CAN BE OF DIFFERENT TYPES
# TUPLES IN PYTHON ARE IMMUTABLE
# TUPLES TAKE UP LESS MEMORY BECAUSE THEY ARE IMMUTABLE
    
myTuple = (1, 2, 3, 4, 5)
myTuple2 = ("1", 2 ,True)

variable_name_dictionary2 = {"myTuple": myTuple, "myTuple2": myTuple2, }
for name, value in variable_name_dictionary2.items():
    print("The length of {} is: {}".format(name, len(value)))

for anItem in myTuple2:
    print(anItem)

print("---------------------")



# SETS IN PYTHON {}
# SETS CAN BE OF DIFFERENT TYPES
# SETS IN PYTHON ARE UNORDERED
# SETS TAKE UP LESS MEMORY BECAUSE THEY ARE UNORDERED
# SETS DO NOT ALLOW DUPLICATES

mySet = {1, 2, 3, 4, 5, 1, 2}
mySet2 = {"1", 2 ,True, True}

variable_name_dictionary3 = {"mySet": mySet, "mySet2": mySet2, }
for name, value in variable_name_dictionary3.items():
    print("The length of {} is: {}".format(name, len(value)))

for anItem in mySet2:
    print(anItem)

print("---------------------")


# DICTIONARIES IN PYTHON {}
# DICTIONARIES CAN BE OF DIFFERENT TYPES
# DICTIONARIES IN PYTHON ARE UNORDERED
# DICTIONARIES HAVE A KEY VALUE PAIR
# DICTIONARIES HAVE TWO METHODS THAT RETURN TUPLES .values() AND .keys()
# ALSO WHEN LOOPING THROUGH A DICTIONARY WITH A STANDARD LOOP THE KEY BECOMES THE ITERATOR

myDictionary = {"key1": "value1", "key2": 2, "key3": True, "key4": [1, 2, 3], "key5": True}
for key, value in myDictionary.items():
    print("The value of {} is: {}".format(key, value))

myDictionary["key6"] = "value6"
myDictionary["key7"] = {"key7_1": "value7_1", "key7_2": "value7_2"}
print()
print("Dictionary Values:")
for value in myDictionary.values():
    print(value)
print()
print("Dictionary Keys:")
for key in myDictionary.keys():
    print(key)

print("---------------------")



# Write a program that takes in grades one at a time until a -1 is seen to mark the end of the list.
# Each grade will be separated by an enter key.  
#When you are done, output the average (as an int) followed by the grades in order that you saw them.
# An example execution would look like this:
# Input: 
# 	80
# 	75
# 	70
# 	-1
# Output:
# 	75
# 	80
# 	75
# 	70

user_input = input("")
grades = []
sum_of_grades = 0

while user_input != "-1":
    grades.append(int(user_input))
    sum_of_grades += int(user_input)
    user_input = input("")

print(int(sum_of_grades / len(grades)))

for grade in grades:
    print(grade)
