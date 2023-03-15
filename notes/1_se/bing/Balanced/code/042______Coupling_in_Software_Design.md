Coupling in software design refers to the degree of interdependence between software modules. It measures how closely connected two modules are and how much they rely on each other to function. A high coupling means that changing one module will affect many other modules, making the software complex and difficult to maintain. A low coupling means that modules are independent and can be changed or reused with minimal impact on other modules, making the software modular and easy to maintain.

One way to measure coupling is by counting the number of parameters, global variables, and external references that a module uses or exposes. Another way is by analyzing the types of relationships between modules, such as inheritance, aggregation, composition, or association.

There are different types of coupling, ranging from loose to tight, such as:

- **Data coupling**: Modules share only data through parameters. This is the loosest form of coupling and the most desirable one.
- **Stamp coupling**: Modules share a composite data structure through parameters and use only parts of it.
- **Control coupling**: Modules share control information through parameters, such as flags or function pointers. This can create implicit dependencies and reduce readability.
- **External coupling**: Modules depend on external systems or resources, such as files, databases, or network connections. This can create performance and reliability issues.
- **Common coupling**: Modules share global data or variables. This can create side effects and make the software unpredictable and hard to test.
- **Content coupling**: Modules access or modify the internal data or code of other modules. This is the tightest form of coupling and the least desirable one.

The goal of software design is to achieve low coupling and high cohesion, which means that modules are independent and focused on a single responsibility. This can improve the quality, maintainability, and reusability of the software.

Here is an example of code that demonstrates low coupling and high cohesion in Python:

```python
# Module A: Defines a class that represents a bank account
class Account:
    def __init__(self, balance):
        self.balance = balance # private attribute

    def deposit(self, amount):
        self.balance += amount # public method

    def withdraw(self, amount):
        if self.balance >= amount: # public method
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self): # public method
        return self.balance

# Module B: Defines a class that represents a bank customer
class Customer:
    def __init__(self, name, account):
        self.name = name # private attribute
        self.account = account # private attribute

    def get_name(self): # public method
        return self.name

    def get_account(self): # public method
        return self.account

# Module C: Defines a function that performs a transaction between two customers
def transfer(sender, receiver, amount):
    if sender.get_account().withdraw(amount): # data coupling
        receiver.get_account().deposit(amount) # data coupling
        return True
    else:
        return False

# Module D: Defines a main function that tests the code
def main():
    # Create two customers with different accounts
    alice = Customer("Alice", Account(1000))
    bob = Customer("Bob", Account(500))

    # Print their initial balances
    print(f"{alice.get_name()} has ${alice.get_account().get_balance()}")
    print(f"{bob.get_name()} has ${bob.get_account().get_balance()}")

    # Transfer $200 from Alice to Bob
    print("Transferring $200 from Alice to Bob...")
    if transfer(alice, bob, 200):
        print("Transfer successful!")
    else:
        print("Transfer failed!")

    # Print their final balances
    print(f"{alice.get_name()} has ${alice.get_account().get_balance()}")
    print(f"{bob.get_name()} has ${bob.get_account().get_balance()}")

# Run the main function
if __name__ == "__main__":
    main()
```

The code above shows low coupling and high cohesion because:

- Each module has a single responsibility and a clear interface.
- The modules communicate only through data, not through control or global variables.
- The modules do not access or modify the internal data or code of other modules.
- The modules can be changed or reused with minimal impact on other modules.