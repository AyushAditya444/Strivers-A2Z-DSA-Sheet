def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

n = int(input())
arr = list(map(int, input().split()))

for i in range(n//2):
    swap(arr, i, n-i-1)


print(arr)