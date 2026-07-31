Hello, I am Sydney, your AI assistant. I can help you with your topic of regular and non-regular languages. Here are some notes that you can use for your study material:

### Regular and Non-Regular Languages

- A **regular language** is a language that can be expressed with a **regular expression** or a **finite automaton**.
- A **regular expression** is a sequence of symbols that defines a **pattern** for matching strings.
- A **finite automaton** is a mathematical model of computation that has a **finite number of states** and can change its state based on the input symbols.
- A **non-regular language** is a language that **cannot** be expressed with a regular expression or a finite automaton.
- A non-regular language requires **infinite memory** or **unbounded computation** to recognize.
- Some examples of regular languages are:
  - The set of all strings of length 2 over {a, b}*
  - The set of all strings that start and end with the same symbol over {a, b}*
  - The set of all strings that contain an even number of 1s over {0, 1}*
- Some examples of non-regular languages are:
  - The set of all palindromes over {a, b}*
  - The set of all strings of the form a^n b^n over {a, b}*
  - The set of all strings that contain the same number of 0s and 1s over {0, 1}*
- There are some methods to prove that a language is regular or non-regular, such as:
  - **Closure properties**: If a language is regular, then it is closed under some operations, such as union, concatenation, complement, etc. If a language is not closed under some operation, then it is not regular.
  - **Pumping lemma**: If a language is regular, then there exists a constant p such that any string in the language of length at least p can be divided into three parts x, y, and z, such that xy^i z is also in the language for any i >= 0. If a language does not satisfy this property, then it is not regular.
  - **Finite state machines**: If a language is regular, then there exists a finite state machine that accepts it. If a language is not regular, then no finite state machine can accept it.