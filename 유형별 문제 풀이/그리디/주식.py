import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))

    max_price = 0
    profit = 0

    # 뒤에서부터 순회
    for price in reversed(prices):
        if price > max_price:
            max_price = price
        profit += max_price - price

    print(profit)
