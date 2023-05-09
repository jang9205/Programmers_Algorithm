# 첫 번째 풀이
n = int(input())
for i in range (n):
    for j in range (i+1):
        print('*', end= '')
    print('')
    
# 두 번째 풀이
n = int(input())
for i in range(1, n+1):
    print('*' * i)