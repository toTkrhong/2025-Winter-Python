num = int(input())


for i in range (num):
    sentence = input()
    sentence = sentence.replace(" ", "")
    clist = list(sentence)

    dictionary = {}
    
    for char in clist:
        if char in dictionary:
            dictionary[char]+=1
        else:
            dictionary[char]=1

    max_frequency = '?'
    max = 0
    dup = 0
    for item in dictionary:
        if (max < dictionary[item]):
            max = dictionary[item]
            max_frequency = item
    for item in dictionary:
        if (max == dictionary[item] and max_frequency != item):
            dup = 1
            break

    if dup == 1:
            print('?')
    else:
        print(max_frequency)