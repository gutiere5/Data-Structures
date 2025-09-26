"""
The Problem: Look at the call tree for fib(5). The function fib(3) is calculated twice, fib(2) is calculated three times, and so on. This re-computation grows exponentially.

Time Complexity: O(2 ^ n) - Exponential. For each increase in n, the number of operations roughly doubles. This is terribly slow.
Space Complexity: O(n) - The maximum depth of the recursion stack.

Solution: We can use a technique called memoization to store the results of expensive function calls and return the cached result when the same inputs occur again.
By adding the cache, we ensure that fib_memo(n) for any given n is only ever computed once. All subsequent calls for that n are simple dictionary lookups.

Time Complexity: O(n) - Linear. We compute the Fibonacci value for each number from 1 to n exactly once.
Space Complexity: O(n) - The trade-off is that we now store the results for each number up to n in our cache.
"""

from functools import cache

# A dictionary to act as our cache
memo = {}

def fib_memo(n):
    # 1. Check if the result is already in our cache
    if n in memo:
        return memo[n]

    # Base case is the same
    if n <= 1:
        return n

    # 2. If not in the cache, compute it
    result = fib_memo(n - 1) + fib_memo(n - 2)

    # 3. Store the result in the cache before returning
    memo[n] = result

    return result


@cache
def fib_decorator(n):
    if n <= 1:
        return n
    return fib_decorator(n - 1) + fib_decorator(n - 2)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2) # Notice the two recursive calls

if __name__ == "__main__":
    import time
    start_time = time.time()
    print("Calculating Fibonacci without memoization...")
    print(fibonacci(40))  # This will be VERY slow! 🐢
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

    start_time = time.time()
    print("Calculating Fibonacci with memoization...")
    print(fib_memo(40))  # This will be MUCH faster! 🚀
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

    start_time = time.time()
    print("Calculating Fibonacci with functools.cache...")
    print(fib_decorator(40))  # This will also be MUCH faster! 🚀
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")








