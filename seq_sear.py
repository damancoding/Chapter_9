# Sequential Search example from early in the day
def sequential_search(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1

array=range(0,50)
target= int(input("Please enter a number between 1 and 100: "))

index = sequential_search(array, target)

if index != -1:
    print("The target value was found at index", index)
else:
    print("The target value was not found in the array")
