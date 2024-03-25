# 재귀를 이용해 트리 순회 구현

def dfs(cur_node):
    if cur_node is None:
        return
    
    dfs(cur_node.left)
    dfs(cur_node.right)

    
    
