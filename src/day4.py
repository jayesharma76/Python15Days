'''
### Day 4: Object-Oriented Python (Advanced)
- Dunder methods (`__str__`, `__call__`, `__getitem__`).
- Property decorators (`@property`), `@classmethod`, and `@staticmethod`.

Today, we are upgrading from writing scripts to architecting systems. Object-Oriented Programming (OOP) is the backbone of almost every major web framework (like Django and FastAPI) and is heavily used in Data Science for building custom Scikit-Learn estimators or PyTorch neural network layers.

To make this highly practical and aligned with real-world engineering, we are going to learn all the OOP concepts and keywords by doing a Low-Level Design (LLD) for the backend of an online classifieds marketplace.

1. The Core: Classes, Objects, and self
A Class is a blueprint. An Object is the actual house built from that blueprint.

class: The keyword to define the blueprint.

__init__: The constructor method. It initializes the state of the object the moment it is created.

self: The most important keyword. It represents the specific instance of the object calling the method. It is how an object keeps track of its own unique data.

'''

class MarketplaceUser:
    # __init__ sets up the initial state
    def __init__(self, username, email):
        self.username = username  # Instance variable
        self.email = email        # Instance variable
        self.is_active = True

    def deactivate_account(self):
        # 'self' allows the object to modify its own specific state
        self.is_active = False
        print(f"User {self.username} deactivated.")

# Creating objects (Instances)
user1 = MarketplaceUser("alice99", "alice@example.com")
user2 = MarketplaceUser("bob_seller", "bob@example.com")

user1.deactivate_account()
# user1 is passed implicitly as 'self'. user2 remains active.


'''
A. Encapsulation (Protecting the Data)
Encapsulation is the practice of hiding the internal state of an object and requiring all interaction to be performed through an object's methods. In Python, we use underscores to signal privacy.

_variable: Protected (convention only, tells other devs "don't touch this").

__variable: Private (triggers name-mangling, making it harder to access from outside).

@property: A decorator that lets you define a method that can be accessed like an attribute, perfect for getters/setters.
'''
class Wallet:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private variable

    @property
    def balance(self):
        # Getter method
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit must be positive.")

user_wallet = Wallet(500)
# print(user_wallet.__balance) # This will throw an AttributeError!
print(user_wallet.balance)     # Safe access via @property (Output: 500)


'''
B. Inheritance (Reusing Code)
'''

class Listing:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    @staticmethod
    def print_return(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(result)
            return result

        return wrapper

    @print_return
    def display(self):
        return f"Ad: {self.title} - ₹{self.price}"

# PremiumListing inherits from Listing
class PremiumListing(Listing):
    def __init__(self, title, price, feature_days):
        # super() calls the parent's __init__ to handle title and price
        super().__init__(title, price)
        self.feature_days = feature_days

    @Listing.print_return
    def display(self):
        # Method Overriding: Changing how the parent method works
        parent_display = super().display()
        return f"🌟 PREMIUM 🌟 {parent_display} (Featured for {self.feature_days} days)"


class AnalyticsTracker:
    total_page_views = 0  # Class variable (shared across all instances)

    def __init__(self):
        self.session_views = 0  # Instance variable

    @classmethod
    def record_global_view(cls):
        cls.total_page_views += 1

    @staticmethod
    def calculate_conversion_rate(clicks, views):
        # Doesn't need 'self' or 'cls', just utility math
        if views == 0: return 0
        return (clicks / views) * 100

# Magic methods (Dunder Methods)
class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # Without this, print() shows <__main__.Category object at 0x...>
        return f"Category: {self.name}"

    def __eq__(self, other):
        # Defines how two Category objects are considered "equal"
        if isinstance(other, Category):
            return self.name.lower() == other.name.lower()
        return False

cat1 = Category("Electronics")
cat2 = Category("electronics")
print(cat1 == cat2) # True, because we defined __eq__

if __name__ == "__main__":
    # Create a user and a wallet
    user = MarketplaceUser("charlie_buyer", "charlie@gmail.com")
    wallet = Wallet(1000)
    print(f"{user.username} has a wallet balance of {wallet.balance}.")
    standard_ad = Listing("Used Sofa", 5000)
    premium_ad = PremiumListing("Gaming Laptop", 45000, feature_days=7)
    standard_ad.display()
    premium_ad.display()
