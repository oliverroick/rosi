def depth(L):
    return isinstance(L, list) and max(map(depth, L))+1
