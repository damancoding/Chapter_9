# Amanda M
# 3/27/24
# Sorted Names Chapter 9 Problem 2
#Sorted Name = Insertion

names = []
coral = ["James","Michael","Andrew","Tom","Tobey","Chris","Tony","Tahi","Nehemiah","Zaine"]
def add_name(words):
    print("There are already 10 names in the registry.")
    i = 0
    while i < 10: 
        words = input("Please input 10 more for filing: ")
        coral.append(words)
        i = i + 1

def double_check():
        while len(coral) <= 19:
            if len(coral) < 19:
                text = input("Enter more names: ")
                coral.append(text)
            elif len(coral) == 20:
                continue
def library():
    for i in range(0, len(coral)-1):
        names_idx = i
        for j in range(i + 1, len(coral)):
            if coral[j] < coral[names_idx]:
                names_idx = j
        coral[i], coral[names_idx] = coral[names_idx], coral[i]

names.append(coral)

add_name(words=vars)
library()
print(names)
