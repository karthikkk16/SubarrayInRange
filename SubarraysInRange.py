def subarrayInRange(a,b,c):
    result=[]
    for i in range(b,c+1):
        result.append(a[i])
    return result

a=list(map(int,input().split()))
b=int(input())
c=int(input())
print(subarrayInRange(a,b,c))