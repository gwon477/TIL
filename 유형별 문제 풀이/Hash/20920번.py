# 7 4
# apple
# ant
# sand
# apple
# append
# sand
# sand

# sand
# apple
# append

import sys

def main():
    N,M = map(int,sys.stdin.readline().split())
    
    words = [sys.stdin.readline().strip() for i in range(N)]

    dic = {}
    
    for _ in words:
        if len(_) >= M:
            if _ in dic:
                dic[_] += 1    
            else:
                dic[_] = 1

    sorted_dic = dict(sorted(dic.items(), key=lambda x:(-x[1],-len(x[0]), x[0])))
    for _ in sorted_dic:
        print(_)
    return

main()