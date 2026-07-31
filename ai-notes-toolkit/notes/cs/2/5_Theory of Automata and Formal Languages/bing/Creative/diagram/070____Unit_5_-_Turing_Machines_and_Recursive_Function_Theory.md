# Unit 5 - Turing Machines and Recursive Function Theory

## Turing Machines

- A Turing machine is a theoretical model of computation that can perform any algorithmic task .
- A Turing machine consists of a finite set of states, a finite alphabet of symbols, a tape divided into cells, and a read-write head that can move along the tape and change the symbols on it .
- A Turing machine can be in one of the states at any time, and the state determines how the machine behaves on the current symbol on the tape .
- A Turing machine can change its state, write a new symbol on the tape, and move the head one cell to the left or right, according to a transition function that specifies the rules of the machine .
- A Turing machine can halt when it reaches a special state called the halt state, or it can run forever without halting .
- A Turing machine can accept or reject an input string by halting in an accept state or a reject state, respectively .
- A Turing machine can compute a function by writing the output on the tape when it halts in an accept state .
- A Turing machine can simulate any other Turing machine by encoding the states, symbols, and transition function of the other machine on its tape .
- A Turing machine can recognize a language by accepting all and only the strings that belong to the language .
- A language is called recursively enumerable (RE) or Turing-recognizable if there is a Turing machine that recognizes it .
- A language is called recursive or Turing-decidable if there is a Turing machine that decides it, i.e., halts on every input and accepts or rejects it .

## Recursive Function Theory

- Recursive function theory is a branch of mathematical logic that studies the properties and limitations of computable functions .
- A function from natural numbers to natural numbers is called computable or recursive if there is a Turing machine that can compute it .
- A function is called partial recursive if it is computable but may be undefined for some inputs .
- A function is called total recursive if it is computable and defined for all inputs .
- A function is called primitive recursive if it can be obtained from the basic functions (zero, successor, projection) by using composition and primitive recursion .
- A function is called μ-recursive if it can be obtained from the primitive recursive functions by using the minimization operator .
- The class of μ-recursive functions is equivalent to the class of Turing-computable functions, i.e., every μ-recursive function is Turing-computable and vice versa .
- A set of natural numbers is called recursive or decidable if its characteristic function (which returns 1 if the input belongs to the set and 0 otherwise) is recursive .
- A set of natural numbers is called recursively enumerable (RE) or semi-decidable if its characteristic function is partial recursive .
- A set of natural numbers is called co-recursively enumerable (co-RE) or co-semi-decidable if its complement is recursively enumerable .
- A set of natural numbers is called recursive or decidable if and only if it is both recursively enumerable and co-recursively enumerable .
- There are some functions and sets that are not computable or decidable, such as the halting problem, the diagonalization function, and the busy beaver function  .
- The Church-Turing thesis states that any function that can be effectively computed by a human or a machine is computable by a Turing machine or a μ-recursive function .