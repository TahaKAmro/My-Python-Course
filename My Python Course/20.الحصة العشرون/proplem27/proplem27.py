#proplem link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

n = int(input())
arr = map(int, input().split())
my_list = list(set(arr))
my_list.remove(max(my_list))
print(max(my_list))