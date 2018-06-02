def matrix(n) :
    a = 0
    b = 0
    i = 0
    for j in range(n):
        k = input().split()
        a += int(k[i])
        b += int(k[n-1-i])
        i += 1
    return abs(a-b)  

n = int(input())
res = matrix(n)
print(res)