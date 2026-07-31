### Abstract Data Types

- An abstract data type (ADT) is a mathematical model for data types that defines the logical form of the data and the operations that can be performed on the data .
- An ADT does not specify how the data is stored or implemented, but only the interface or behavior of the data type .
- An ADT can be implemented using different concrete data types (CDTs), such as arrays, lists, maps, queues, sets, stacks, tables, trees, vectors, etc .
- An ADT can be viewed as a concept or a specification, rather than a data type .
- In Python, an ADT can be defined using abstract base classes (ABCs), which are classes that cannot be instantiated, but can be subclassed by concrete classes that provide implementations for the abstract methods and properties.
- Some examples of ADTs in Python are collections.abc.Sequence, collections.abc.Mapping, collections.abc.Set, etc.

### ADT Interface in Python

- An ADT interface in Python is a set of abstract methods and properties that define the behavior of the ADT.
- An ADT interface can be created using the abc module, which provides the infrastructure for defining ABCs in Python.
- An ADT interface can be declared using the @abc.abstractmethod and @abc.abstractproperty decorators, which indicate that the method or property must be overridden by a concrete subclass.
- An ADT interface can also specify some concrete methods and properties that provide default or common functionality for the ADT, but can be overridden by a concrete subclass if needed.
- An ADT interface can be inherited by multiple concrete classes that provide different implementations for the ADT.
- An example of an ADT interface in Python is collections.abc.Container, which defines the abstract method __contains__ and the concrete method __iter__ for checking membership and iterating over the elements of a container.

### Sieve of Eratosthenes

- The sieve of Eratosthenes is an algorithm for finding all prime numbers up to a given limit.
- The algorithm was devised by the Greek mathematician Eratosthenes in the 3rd century BC.
- The algorithm works by creating a list of consecutive integers from 2 to the limit, and marking off multiples of each prime, starting from 2.
- The numbers that are not marked off are the prime numbers.
- The algorithm can be implemented in Python using the following steps:

  - Create a list of booleans of length limit + 1, initialized to True, except for the first two elements, which are False.
  - Loop over the list from 2 to the square root of the limit, and for each element that is True, mark off its multiples as False, starting from its square.
  - Loop over the list again and collect the indices that are True into a new list, which are the prime numbers.

- An example of the sieve of Eratosthenes in Python is:

```python
def sieve_of_eratosthenes(limit):
  # Create a list of booleans of length limit + 1
  is_prime = [False, False] + [True] * (limit - 1)

  # Loop over the list from 2 to the square root of the limit
  for i in range(2, int(limit**0.5) + 1):
    # If the element is True, mark off its multiples as False
    if is_prime[i]:
      for j in range(i*i, limit + 1, i):
        is_prime[j] = False

  # Loop over the list again and collect the indices that are True
  primes = []
  for i in range(2, limit + 1):
    if is_prime[i]:
      primes.append(i)

  # Return the list of prime numbers
  return primes
```