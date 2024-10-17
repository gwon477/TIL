def check_bingo(board, called):
    bingo_count = 0

    # 가로줄 체크
    for row in board:
        if all(num in called for num in row):
            bingo_count += 1

    # 세로줄 체크
    for col in range(5):
        if all(board[row][col] in called for row in range(5)):
            bingo_count += 1

    # 왼쪽 위에서 오른쪽 아래로 가는 대각선 체크
    if all(board[i][i] in called for i in range(5)):
        bingo_count += 1

    # 오른쪽 위에서 왼쪽 아래로 가는 대각선 체크
    if all(board[i][4-i] in called for i in range(5)):
        bingo_count += 1

    return bingo_count >= 3

def bingo_game(bingo_board, numbers):
    called_numbers = set()
    
    for turn, number in enumerate(numbers):
        called_numbers.add(number)
        
        if turn >= 11:  # 최소 12번부터 빙고 가능
            if check_bingo(bingo_board, called_numbers):
                return turn + 1  # turn은 0부터 시작하므로 1을 더해줌

# 입력
bingo_board = [list(map(int, input().split())) for _ in range(5)]
numbers = [int(x) for _ in range(5) for x in input().split()]

# 출력
print(bingo_game(bingo_board, numbers))
