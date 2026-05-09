
def edit_distance(s1: str, s2: str) -> int:
    '''
    >>> edit_distance("kitten", "sitting")
    3
    >>> edit_distance("flaw", "lawn")
    2
    >>> edit_distance("intention", "execution")
    5
    '''
    def helper(i: int, j: int) -> int:
        if (i, j) in memo:
            counter[(i, j)] += 1
            return memo[(i, j)]
            
        if i == len(s1):
            return len(s2) - j
        if j == len(s2):
            return len(s1) - i
            
        if s1[i] == s2[j]:
            return helper(i + 1, j + 1)
        else:
            remove_dist = 1 + helper(i + 1, j)
            update_dist = 1 + helper(i + 1, j + 1)
            insert_dist = 1 + helper(i, j + 1)
    
            value = min(remove_dist, update_dist, insert_dist)
            memo[(i, j)] = value
            counter[(i, j)] = 0
            return value

    memo = {}
    counter = {}

    r = helper(0, 0)
    return r

import doctest
doctest.testmod()
