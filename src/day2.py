'''
### Day 2: Functional Programming Tools
- Mastering `lambda`, `map`, `filter`, and `reduce`.
- Using `itertools` for efficient looping and `functools.partial`.
'''

# The Big four - Lambda, Map, Filter, Reduce
# Lambda: Anonymous functions for quick, throwaway operations.
# Map: Apply a function to every item in an iterable.
# Filter: Select items from an iterable based on a condition.
# Reduce: Apply a function cumulatively to the items of an iterable, reducing it to a single value.
import time
def demo_lambda():
    # A lambda function to add 10 to a number
    add_ten = lambda x: x + 10
    print(add_ten(5))  # Output: 15

def square(x):
    return x**2
# Problem : given a list of integers, return a list of squares of only even numbers using filter and map with lambda
def demo_lambda_map_filter():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    fun_square = lambda x: x**2
    even_numbers_squared = list(map(square, filter(lambda n:n%2 == 0,numbers))) # map is lazy initialized so we need to convert it to list explicitly
    print(even_numbers_squared)

def dict_from_evens_comprehension(nums):
    return {x:x**2 for x in nums if x %2 == 0}

def dict_from_evens_map_filter(nums):
    return dict(map(lambda n : (n,n**2), filter(lambda n : n % 2 == 0, nums)))

#reduce is used to apply a function cumulatively to the items of an iterable, from left to right, reducing the iterable to a single value.
# For example, we can use reduce to calculate the product of all numbers in a list.
def demo_reduce():
    from functools import reduce
    numbers = [1,2,3,4,5]
    product = reduce(lambda x,y: x*y, numbers)
    print(product)  # Output: 120

def demo_itertools():
    import itertools
    # Example: Create an infinite counter starting from 0
    counter = itertools.count(0)
    print(next(counter))  # Output: 0
    print(next(counter))  # Output: 1
    print(next(counter))  # Output: 2

    # Avoiding nested loops for ML hyperparameter tuning
    learning_rates = [0.01, 0.1]
    batch_sizes = [16, 32]

    for lr, batch in itertools.product(learning_rates, batch_sizes):
        print(f"Training with LR: {lr}, Batch: {batch}")

def demo_partial():
    from functools import partial
    # Example: A function to calculate the power of a number
    def power(base, exponent):
        return base ** exponent

    # Create a new function that squares a number using partial
    square = partial(power, exponent=2)
    print(square(5))  # Output: 25

if __name__ == '__main__':
    demo_lambda_map_filter()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
            29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    start = time.perf_counter()
    comp = dict_from_evens_comprehension(nums)
    end = time.perf_counter()
    print(comp)
    print(f"comprehension: {(end - start) * 1000:.3f} ms")
    start = time.perf_counter()
    mf = dict_from_evens_map_filter(nums)
    end = time.perf_counter()
    print(mf)
    print(f"map_filter: {(end - start) * 1000:.3f} ms")
    # Comprehension is faster as it is optimized using C level implementation while map and filter are using lambda that is still python level implementation.
    # Although map and filters are also C level optimized but the use of lambda makes it slower than comprehension. In general, for simple transformations, comprehensions are often more efficient and easier to read than using map and filter with lambda functions.
    demo_itertools()
    demo_partial()