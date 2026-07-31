# Finite Automata and Regular Languages

- A **finite automaton** is a mathematical model of a machine that can accept or reject a string of symbols based on its states and transitions .
- A **regular language** is a set of strings that can be described by a **regular expression** or recognized by a finite automaton .
- A **regular expression** is a notation that uses symbols and operators to define a regular language .
- A **regular grammar** is a type of grammar that generates a regular language by applying rules that replace a single non-terminal symbol with a string of terminal and non-terminal symbols .

## Properties of Regular Languages

- Regular languages are closed under the following operations: union, concatenation, star, complement, intersection, and difference .
- Regular languages can be decided by algorithms that test membership, emptiness, equivalence, and containment.
- Regular languages can be minimized by finding the smallest equivalent finite automaton.
- Regular languages can be pumped by applying the pumping lemma, which states that any sufficiently long string in a regular language can be divided into three parts that can be repeated to form new strings in the same language.

## Examples of Regular Languages

- The language of all strings over {a,b} that end with a .
- The language of all binary numbers that are divisible by 3 .
- The language of all strings over {0,1} that do not contain the substring 11 .
- The language of all strings over {a,b,c} that have an equal number of a's and b's.
- The language of all strings over {a,b} that have an odd length.