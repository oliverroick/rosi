depth = lambda L: isinstance(L, list) and max(map(depth, L))+1
