'''


### Day 3: Decorators & Context Managers
- Understanding closures. Writing custom decorators (useful for Web Auth/Logging).
- Using `with` statements and creating custom context managers using `contextlib`.


'''

## The closure - remembers the values in enclosing scopes even after the outer function has finished execution

def make_counter():
    count = 0
    def increment():
        nonlocal count
        count+=1
        return count
    return increment

import time

## decorator - a function that takes another function and extends its behavior without explicitly modifying

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs) # Execute the original function
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.4f}s")
        return result
    return wrapper

@timer_decorator
def process_data(data):
    time.sleep(1) # Simulating heavy ML processing
    return [d * 2 for d in data]

process_data([1, 2, 3])

# custom context manager using class-based approach

class MLProfiler:
    def __init__(self, model_name):
        self.model_name = model_name
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        print(f"Starting training pipeline for {self.model_name}...")
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        elapsed = time.time() - self.start_time

        if exc_type is ValueError:
            print(f"Caught a ValueError: {exc_val}. Suppressing and continuing.")
            return True

        if exc_type:
            print(f"CRITICAL FAILURE in {self.model_name}: {exc_val}")
            return False

        print(f"Success! {self.model_name} completed in {elapsed:.4f} seconds.")
        return True


def train_model(simulate_error=False):
    with MLProfiler("XGBoost_Classifier"):
        time.sleep(1.5)
        if simulate_error:
            raise ValueError("NaN values found in dataset")


if __name__ == '__main__':
    print(make_counter())
    print(make_counter())
    process_data([1, 2, 3])
    train_model(simulate_error=True)