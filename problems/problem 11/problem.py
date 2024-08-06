n = int(input())
scores = list(set(map(int , input().split())))

scores.sort()
scores.remove(max(scores))
print(max(scores))
