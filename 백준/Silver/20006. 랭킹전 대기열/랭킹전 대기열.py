p, m = map(int, input().split())
main_dict = {}

for i in range(p):
    value, key = input().split()
    value = int(value)
    main_dict[key] = value

while main_dict:
    cnt = 0
    tmp_dict = {}
    for key in main_dict:
        if cnt == 0:
            first_level = main_dict[key]
        
        level_diff = first_level - main_dict[key]
        if (abs(level_diff) <= 10):
                tmp_dict[key] = main_dict[key]
                cnt+=1
        if cnt == m:
            break

    if cnt == m :
        print("Started!")
    else:
        print("Waiting!")

    for key in sorted(tmp_dict.keys()):
        print(tmp_dict[key], key)
        del main_dict[key]
