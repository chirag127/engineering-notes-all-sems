### Encapsulation for the notes of the Unit 1 - Introduction: The meaning of Object Orientation in the subject of Object Oriented System Design

- Encapsulation is a fundamental concept in object-oriented programming (OOP) that involves bundling data and the methods that operate on that data within a single unit, known as a class .
- This concept helps to protect the data and methods from outside interference, as it restricts direct access to them .
- Encapsulation separates the contractual interface of an abstraction and its implementation. The interface defines the expected behavior and the implementation provides the details of how the behavior is achieved.
- Encapsulation allows an object to change its internal implementation without affecting the overall functioning of the system. This increases the flexibility and maintainability of the code.
- Encapsulation also enhances the reusability and modularity of the code, as different classes can be combined to create complex systems without exposing their internal details.
- Encapsulation can be achieved by using access modifiers, such as public, private, protected, and internal, to control the visibility and accessibility of the data and methods within a class .
- An example of encapsulation in C# is:

```csharp
// A class that encapsulates the data and methods of a bank account
public class BankAccount
{
    // Private data members that are not directly accessible from outside the class
    private string owner;
    private double balance;

    // Public constructor that initializes the data members
    public BankAccount(string owner, double balance)
    {
        this.owner = owner;
        this.balance = balance;
    }

    // Public methods that provide the interface for the class
    public string GetOwner()
    {
        return owner;
    }

    public double GetBalance()
    {
        return balance;
    }

    public void Deposit(double amount)
    {
        if (amount > 0)
        {
            balance += amount;
        }
    }

    public bool Withdraw(double amount)
    {
        if (amount > 0 && amount <= balance)
        {
            balance -= amount;
            return true;
        }
        else
        {
            return false;
        }
    }
}
```