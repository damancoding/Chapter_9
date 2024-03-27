# Name Search = Selection
# Amanda M
# 3/27/2024
# Chapter 9 Problem 4

from sort_names import names

def sequential_search(array,target):
    for i in range(len(names)):
        if names[i]==target:
            return i
    return -1

names=range(0,20)
target= input("Please enter a name: ")

index = sequential_search(names, target)

if index != -1:
    print("The target value was found at index", index)
else:
    print("The target value was not found in the array")

