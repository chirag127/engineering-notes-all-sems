
### Modules: Introduction, Importing Modules 

- A module is a Python file containing definitions and statements. 
- The file name is the module name with the suffix .py appended. 
- Within a module, the module’s name (as a string) is available as the value of the global variable __name__. 
- To import a module, use the `import` statement. 
- When a module is imported, the interpreter first searches for a built-in module with that name. 
- If not found, it then searches for a file named `[module].py` in a list of directories given by the variable `sys.path`. 

### Unit 4 - Sieve of Eratosthenes: 

- The Sieve of Eratosthenes is an algorithm given by the Greek Mathematician named Eratosthenes, used to generate prime numbers. 
- It works by iteratively marking as composite (i.e. not prime) the multiples of each prime, starting with the multiples of 2. 
- The algorithm is as follows: 
    1. Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
    2. Initially, let p equal 2, the first prime number.
    3. Starting from p, count up in increments of p and mark each of these numbers greater than p itself in the list. These numbers will be 2p, 3p, 4p, etc.; note that some of them may have already been marked.
    4. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
    5. When the algorithm terminates, all the numbers in the list that are not marked are prime.