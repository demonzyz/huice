number = [2, 2, 11, 15]
target = 4

for i in range(len(number)-1):
    for j in range(i, len(number)-1):
        if i is not j:
            if number[i] + number[j] == target:
                print [i+1, j+1]
