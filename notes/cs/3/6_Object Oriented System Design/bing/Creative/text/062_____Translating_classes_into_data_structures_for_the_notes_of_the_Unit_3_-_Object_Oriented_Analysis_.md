### Translating classes into data structures

- A class is a blueprint for creating objects that have common attributes and behaviors.
- A data structure is a way of organizing and storing data in memory or on disk.
- Translating classes into data structures involves mapping the attributes and behaviors of a class to the fields and methods of a data structure.
- There are different ways of translating classes into data structures, depending on the programming language and the design goals.
- Some common ways of translating classes into data structures are:

  - **Record or struct**: A record or struct is a data structure that groups a fixed number of fields of different types under a single name. A record or struct can be used to translate a class that has only attributes and no behaviors, or a class that has simple behaviors that can be implemented as functions or procedures. For example, a class `Point` that has two attributes `x` and `y` and a method `distance` that calculates the distance from another point can be translated into a record or struct as follows:

    ```c
    // C language
    struct Point {
      int x;
      int y;
    };

    // A function that calculates the distance between two points
    double distance(struct Point p1, struct Point p2) {
      return sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2));
    }
    ```

  - **Object or class**: An object or class is a data structure that encapsulates both data and behavior under a single name. An object or class can be used to translate a class that has both attributes and behaviors, or a class that has complex behaviors that depend on the state of the object. For example, a class `BankAccount` that has two attributes `balance` and `interestRate` and two methods `deposit` and `withdraw` that update the balance and apply interest can be translated into an object or class as follows:

    ```java
    // Java language
    class BankAccount {
      private double balance;
      private double interestRate;

      // A constructor that initializes the balance and interest rate
      public BankAccount(double balance, double interestRate) {
        this.balance = balance;
        this.interestRate = interestRate;
      }

      // A method that deposits an amount and applies interest
      public void deposit(double amount) {
        balance += amount;
        balance *= (1 + interestRate);
      }

      // A method that withdraws an amount and applies interest
      public void withdraw(double amount) {
        balance -= amount;
        balance *= (1 + interestRate);
      }

      // A method that returns the current balance
      public double getBalance() {
        return balance;
      }
    }
    ```

  - **Array or list**: An array or list is a data structure that stores a collection of elements of the same type in a sequential order. An array or list can be used to translate a class that represents a collection of objects that have the same attributes and behaviors, or a class that has behaviors that operate on a collection of objects. For example, a class `Student` that has two attributes `name` and `grade` and a class `Classroom` that has an attribute `students` that is a collection of `Student` objects and a method `averageGrade` that calculates the average grade of the students can be translated into an array or list as follows:

    ```python
    # Python language
    class Student:
      # A constructor that initializes the name and grade
      def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    class Classroom:
      # A constructor that initializes the students as an empty list
      def __init__(self):
        self.students = []

      # A method that adds a student to the list
      def addStudent(self, student):
        self.students.append(student)

      # A method that calculates the average grade of the students
      def averageGrade(self):
        total = 0
        for student in self.students:
          total += student.grade
        return total / len(self.students)
    ```