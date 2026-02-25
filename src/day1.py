### Day 1: Advanced Data Structures & Comprehensions
# - Go beyond lists: `defaultdict`, `Counter`, and `deque` from `collections`.
# - List, Dict, and Set comprehensions with nested logic.


"""
Standard Python dictionaries and lists are great, but they often require "boilerplate" code (like checking if a key exists).
The collections module provides specialized containers that are faster and cleaner.
"""

from collections import defaultdict, Counter, deque

def demo_defaultdict():
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    grouped_words = defaultdict(list)  #this will initialize every new key with an empty list
    for word in words:
        grouped_words[word[0]].append(word)  #this will append the word to the list corresponding to that key
    print(grouped_words)
    #{'a': ['apple', 'apple', 'apple'], 'b': ['banana', 'banana'], 'o': ['orange']}
    #Use defaultdict(int) for counters and defaultdict(list) for grouping. It prevents KeyError and makes the intent clear.
    counter_dict = defaultdict(int)
    for word in words:
        counter_dict[word] += 1  #this will increment the count for that word
    print(counter_dict)
    #{'apple': 3, 'banana': 2, 'orange': 1}

def demo_counter():
    data = "Python is great and Python is fast python is easy to learn"
    word_counts = Counter(data.split())  #this will count the occurrences of each word in
    print(word_counts)
    print(word_counts.items())
    #Counter({'Python': 2, 'is': 3, 'great': 1, 'and': 1, 'fast': 1, 'python': 1, 'easy': 1, 'to': 1, 'learn': 1})
    print(word_counts.most_common(2))  #this will print the 3 most common words

def demo_deque():
    d = deque()
    d.append(1)  #this will add 1 to the right end of the deque
    d.append(2)  #this will add 2 to the right end of the deque
    d.appendleft(0)  #this will add 0 to the left end of the deque
    print(d)  #deque([0, 1, 2])
    d.pop()  #this will remove and return the rightmost element (2)
    print(d)  #deque([0, 1])
    d.popleft()  #this will remove and return the leftmost element (0)
    print(d)  #deque([1])

    # Use case: A "Recent Files" list that only keeps the last 3 items
    history = deque(maxlen=3)
    history.append("file1.py")
    history.append("file2.py")
    history.append("file3.py")
    history.append("file4.py")  # file1.py is automatically popped from the left

    print(history)  # deque(['file2.py', 'file3.py', 'file4.py'], maxlen=3)

def demo_list_comprehension():
    # Create a list of squares for even numbers from 0 to 9
    squares = [x**2 for x in range(10) if x % 2 == 0]
    print(squares)  # [0, 4, 16, 36, 64]

def demo_dict_comprehension():
    # Create a dictionary mapping numbers to their squares for numbers from 0 to 9
    squares_dict = {x: x**2 for x in range(10)}
    print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    users = {1: "Jayesh", 2: "Sreya", 3: "Admin"}
    # Use case: Quick lookup by name instead of ID
    name_to_id = {name: uid for uid, name in users.items() if name != "Admin"}
    print(name_to_id)
    # {'Jayesh': 1, 'Sreya': 2}

def demo_set_comprehension():
    # Create a set of unique squares for numbers from 0 to 9
    unique_squares = {x**2 for x in range(10)}
    print(unique_squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
    # Extract unique file extensions, normalized to lowercase
    files = ['main.PY', 'utils.py', 'DATA.CSV', 'main.py']
    extensions = {f.split('.')[-1].lower() for f in files}
    print(extensions)
    # Result: {'py', 'csv'}

if __name__ == "__main__":
    demo_defaultdict()
    demo_counter()
    demo_deque()
    demo_list_comprehension()
    demo_dict_comprehension()
    demo_set_comprehension()