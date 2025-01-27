n = int(input())
three=0;five=0

while (n >= 3):
    if(15 > n and n % 3 == 0):
        n -= 3
        three+=1
    else:
        n -= 5
        five+=1

if (n==0):
    print(five+three)
else:
    print("-1")
    n >= 15 or (15 > n >= 5 & n % 3 != 0)