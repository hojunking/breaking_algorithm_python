

from ctypes import sizeof


def jump2(y,x,board,cache):
    n = len(board)
    if (y >= n or x >=n) :return 0
    if (y == n-1 and x == n-1) : return 1
    if (cache[y][x] != -1): return cache[y][x]
    jumpSize = board[y][x]
    cache[y][x] = jump2(y+jumpSize,x,board,cache) or jump2(y,jumpSize+x,board,cache)
    if cache[y][x] == 1:
        print('({}:{}) = {}'.format(y,x,jumpSize))
    return cache[y][x]

for _ in range(int(input())):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int,input().split())))
    cache =[[-1]*n for _ in range(n)]
    print ('YES' if jump2(0,0,board, cache)else 'NO')