n = int(input())
friends = list(map(int,input().split()))

for i in range(1,n+1):
    print(friends.index(i)+1 , end=' ')