# Author: Bishal Sarang, https://github.com/Bishalsarang/Recursion-Tree-Visualizer/

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
@vs(
    show_return_value=True,
    node_properties_kwargs=config,
)
def fib(n):
    if n <= 1:
        return n
    return fib(n=n - 1) + fib(n=n - 2)


@vs(
    show_return_value=True,
    node_properties_kwargs=config,
)
def f(n):
    if n <= 1:
        return n
    return f(n=n - 1) + f(n=n - 1)


@vs(
    show_return_value=True,
    node_properties_kwargs=config,
)
def g(n):
    if n <= 1:
        return n
    return g(n=n - 2) + g(n=n - 2)


memo = {}
@vs(
    show_return_value=True,
    node_properties_kwargs=config,
)
def fib_memo1(n):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_memo1(n=n-1) + fib_memo1(n=n - 2)
    return memo[n]

def fib(n):
    memo = {}
    @vs(
        show_return_value=True,
        node_properties_kwargs=config,
        )
    def f(n):
        if n in memo:
            return memo[n]
    
        if n <= 1:
            result = n
        else:
            result = f(n - 1) + f(n - 2)
        memo[n] = result
        return result
    return f(n)

@vs(
    show_return_value=True,
    node_properties_kwargs=config,
)
def fib(n):
    if n <= 1:
        return n
    return fib(n=n - 1) + fib(n=n - 2)


def main(n=4, delay=1.5, filename="image"):
    # Call function
    print(fib(n=n))
    # Save recursion tree to a file
    vs.make_animation(f"{filename}-{n}.gif", delay=delay)


if __name__ == "__main__":
    n = 4
    delay = 1.5
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    if len(sys.argv) > 2:
        delay = float(sys.argv[2])
    else:
        delay = 1.5
    if len(sys.argv) > 3:
        filename = str(sys.argv[3])
    else:
        filename = "image"

    main(n, delay, filename)
