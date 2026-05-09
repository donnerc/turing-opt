
import sys

# Import Visualiser class from module visualiser
from visualiser.visualiser import Visualiser as vs

config = {
    "shape": "record",
    "color": "#f57542",
    "style": "filled",
    "fillcolor": "grey",
}

# Add decorator
# Decorator accepts optional arguments: ignore_args , show_argument_name, show_return_value and node_properties_kwargs

def edit_distance_full(s1: str, s2: str) -> int:
    '''
    >>> edit_distance_full("kitten", "sitting")
    3
    >>> edit_distance_full("flaw", "lawn")
    2
    >>> edit_distance_full("intention", "execution")
    5
    '''
    @vs(
        show_return_value=True,
        node_properties_kwargs=config,
    )
    def h(i: int, j: int) -> int:
        if i == len(s1):
            return len(s2) - j
        if j == len(s2):
            return len(s1) - i
            
        if s1[i] == s2[j]:
            return h(i + 1, j + 1)
        else:
            remove_dist = 1 + h(i + 1, j)
            update_dist = 1 + h(i + 1, j + 1)
            insert_dist = 1 + h(i, j + 1)
    
            value = min(remove_dist, update_dist, insert_dist)
            # print(s1, s2, remove_dist, update_dist, insert_dist)
            return value

    return h(0, 0)


def edit_distance_memo(s1: str, s2: str) -> int:
    '''
    >>> edit_distance_memo("kitten", "sitting")
    3
    >>> edit_distance_memo("flaw", "lawn")
    2
    >>> edit_distance_memo("intention", "execution")
    5
    '''
    def h(i: int, j: int) -> int:
        if (i, j) in memo:
            counter[(i, j)] += 1
            return memo[(i, j)]
            
        if i == len(s1):
            return len(s2) - j
        if j == len(s2):
            return len(s1) - i
            
        if s1[i] == s2[j]:
            return h(i + 1, j + 1)
        else:
            remove_dist = 1 + h(i + 1, j)
            update_dist = 1 + h(i + 1, j + 1)
            insert_dist = 1 + h(i, j + 1)
    
            value = min(remove_dist, update_dist, insert_dist)
            memo[(i, j)] = value
            counter[(i, j)] = 0
            return value

    memo = {}
    counter = {}

    r = h(0, 0)
    return r

if __name__ == "__main__":
    filename = "edit_distance"
    delay = 0.5
    
    _, variant, s1, s2 = list(sys.argv)
    func_name = f"edit_distance_{variant}"
    if func_name not in globals():
        raise ValueError(f"Unknown variant: {variant}")
    func = globals()[func_name]
    print(func)
    r = func(s1, s2)
    print(f"Edit distance between '{s1}' and '{s2}' is {r}")
    print(f"{func.__name__}({s1}, {s2}) = {r}")
    
    # Save recursion tree to a file
    vs.make_animation(f"{filename}_{variant}-{s1}-{s2}.gif", delay=delay)