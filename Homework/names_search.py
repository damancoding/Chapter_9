# Name Search = Selection
# Amanda M
# 3/27/2024
# Chapter 9 Problem 4

from Classwork.sort_names import names

#start_scan = 0
#while start_scan < len(names) - 1:
 #   min_index = start_scan
  #  min_value = names[start_scan]

   # index = start_scan + 1
   # while index < len(names):
   #     if names[index] < min_value:
   #         min_value = names[index]
   #         min_index = index
   #     index = index + 1
  #      names[min_index] = names[start_scan]
   #     names[start_scan] = min_value

    #    start_scan = start_scan + 1



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
