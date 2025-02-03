import sys
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    vowel_cnt = 0
    string = input().strip()
    if string == 'end':
        exit()
    word = list(string)
    flag = True

    for i in range(len(word)):
        if word[i] in vowel:
            vowel_cnt += 1

        if i > 0:
            if word[i] == word[i - 1] and word[i] not in ['e', 'o']:
                flag = False
                break

        if i > 1:
            if (word[i] in vowel) == (word[i - 1] in vowel) == (word[i - 2] in vowel):
                flag = False
                break

    if vowel_cnt == 0:
        flag = False

    if flag:
        print(f"<{string}> is acceptable.")
    else:
        print(f"<{string}> is not acceptable.")
