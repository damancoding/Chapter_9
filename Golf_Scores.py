#Sorted Golf = Selection sort
#sorting in the early beginning b/c the file won't display nor work properly
#****************************************
golfScore = []
def golf_Course():
    for i in range(10):
        scores = int(input("Please enter 10 golf scores here, line after line: "))
        golfScore.sort()
        golfScore.append(scores)

    startScan = 0
    while startScan < len(golfScore) - 1:
        min_index = startScan
        min_value = golfScore
        index = startScan + 1
        while index < len(golfScore):
            if golfScore[index] < len(min_value):
                min = golfScore[index]
                min_index = index
            else:
                index = index + 1
            index = index + 1
        golfScore[min_index] = golfScore[startScan]
        golfScore[startScan] = min_value
        startScan = startScan + 1

golf_Course()
print(golfScore)
