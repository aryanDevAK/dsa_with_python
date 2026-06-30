# Test OOP note examples

# 1. Book
class Book:
    category = "General Literature"
    def get_info(self):
        return "This is a book object."

# 2. Dog
class Dog:
    pass

# 3. BankAccount
class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = initial_balance
        print(f"[*] Account created successfully for {self.owner}.")
        
    def check_balance(self):
        return f"{self.owner}'s Balance: ${self.balance:.2f}"

# 4. Coordinate
class Coordinate:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    def print_coordinates(self):
        print(f"X-Coordinate: {self.x} | Y-Coordinate: {self.y}")
        
    def reset(self):
        print("[*] Resetting coordinates...")
        self.x = 0.0
        self.y = 0.0
        self.print_coordinates()


if __name__ == "__main__":
    # Test Book
    print("Testing Book...")
    print(f"Book Category: {Book.category}")
    b = Book()
    print(b.get_info())

    # Test Dog
    print("\nTesting Dog...")
    dog1 = Dog()
    dog2 = Dog()
    print(f"dog1 ID: {id(dog1)}")
    print(f"dog2 ID: {id(dog2)}")
    print(f"Is dog1 the same object as dog2? {dog1 is dog2}")
    dog_alias = dog1
    print(f"Is dog_alias the same object as dog1? {dog_alias is dog1}")

    # Test BankAccount
    print("\nTesting BankAccount...")
    acc1 = BankAccount("Alice", 1500.75)
    acc2 = BankAccount("Bob")
    print(acc1.check_balance())
    print(acc2.check_balance())
    try:
        acc3 = BankAccount("Charlie", -100.00)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    # Test Coordinate
    print("\nTesting Coordinate...")
    coord = Coordinate(12.5, 45.8)
    coord.print_coordinates()
    Coordinate.print_coordinates(coord)
    coord.reset()
