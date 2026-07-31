### Abstract Data Types

- An abstract data type (ADT) is a mathematical model for data types that defines the logical form of the data and the operations that can be performed on the data .
- An ADT does not specify how the data is stored or implemented, only the behavior and interface of the data type .
- An ADT can have multiple concrete data types (CDTs) that implement the ADT using different data structures and algorithms .
- Examples of ADTs are stack, queue, list, map, set, tree, etc. Each of these ADTs can have different CDTs, such as array-based, linked-list-based, hash-based, etc .

### ADT Interface in Python

- Python does not have a built-in way to define ADTs, but it provides some features that can help create and use ADTs .
- One feature is the use of abstract base classes (ABCs) from the `abc` module, which allow defining classes that cannot be instantiated, but can be subclassed by concrete classes that implement the abstract methods and properties of the ABC.
- Another feature is the use of duck typing, which means that an object's behavior is determined by its methods and attributes, not by its class. This allows using different CDTs that implement the same ADT interface without requiring inheritance or type checking .
- For example, to define a stack ADT, one can use an ABC with abstract methods for `push`, `pop`, and `is_empty`, and then implement different CDTs using lists, arrays, or other data structures that provide these methods. Alternatively, one can use any object that has these methods as a stack, regardless of its class.

### Sieve of Eratosthenes

- The sieve of Eratosthenes is an algorithm for finding all prime numbers up to a given limit.
- The algorithm works by creating a list of numbers from 2 to the limit, and then marking the multiples of each number, starting from 2, as composite. The remaining unmarked numbers are prime.
- The algorithm can be implemented in Python using a list as a CDT for the ADT of a sequence. The list can store boolean values indicating whether a number is prime or not, and the algorithm can iterate over the list and mark the multiples of each number as False.
- Here is a possible implementation of the sieve of Eratosthenes in Python:

```python
def sieve_of_eratosthenes(limit):
    # Create a list of booleans with True values
    is_prime = [True] * (limit + 1)
    # Mark 0 and 1 as not prime
    is_prime[0] = is_prime[1] = False
    # Loop from 2 to the square root of the limit
    for i in range(2, int(limit**0.5) + 1):
        # If i is prime, mark its multiples as not prime
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    # Return the list of prime numbers
    return [i for i in range(limit + 1) if is_prime[i]]
```