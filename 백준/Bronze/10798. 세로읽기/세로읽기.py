word_list = [["" for col in range (15)] for row in range (5)]

for i in range (5):
    word = input().strip()
    for j in range(len(word)):
        word_list[i][j] = word[j]


for i in range (5):
    for j in range(15):
        if not word_list[i][j]:
            word_list[i][j]=""

for col in range (15):
    for row in range (5):
        if word_list[row][col]:
            print(word_list[row][col], end='')