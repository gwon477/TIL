import sys

N, K = map(int,sys.stdin.readline().split())
products = []
for i in range(N):
    products.append(list(map(int,sys.stdin.readline().split())))

print("products:",products)