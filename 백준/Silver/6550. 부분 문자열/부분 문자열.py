import sys
input = sys.stdin.readline

while (True):
    iinput = input().strip()
    
    if not iinput:
        break
    else:
        s, t = iinput.split()
        j=0
        for i in range(len(t)):
            if s[j] == t[i]:
                j+=1
                if j ==  len(s):
                    print("Yes")
                    break
        else:
            print("No")