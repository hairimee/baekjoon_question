N, x= map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < x:
        print(A[i], end = ' ')