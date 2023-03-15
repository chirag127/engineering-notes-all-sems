## Unit 3 - Coding a sequence

- A sequence is a set of ordered items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed number of terms or not.
- A sequence can be represented by a formula, a table, a graph, or a list of terms.
- To code a sequence, we need to use a programming language that can generate and manipulate sequences, such as Python.
- In Python, we can use lists, tuples, ranges, generators, or comprehensions to create sequences.
- A list is a mutable sequence of values that can be of any type, enclosed in square brackets [ ].
- A tuple is an immutable sequence of values that can be of any type, enclosed in parentheses ( ).
- A range is an immutable sequence of numbers that follow a certain arithmetic progression, created by the range() function.
- A generator is an object that can produce a sequence of values on demand, using the yield keyword or a generator expression.
- A comprehension is a concise way of creating a sequence from another sequence, using a for loop and an optional if condition inside brackets [ ] or parentheses ( ).

- To access a specific element of a sequence, we can use indexing, which is the process of specifying the position of the element using an integer inside square brackets [ ].
- Indexing starts from 0 for the first element, and can be negative for the last element (-1) or the previous ones (-2, -3, etc.).
- To access a subsequence of a sequence, we can use slicing, which is the process of specifying the start and end positions of the subsequence using a colon : inside square brackets [ ].
- Slicing can also take a third argument, which is the step size of the subsequence, indicating how many elements to skip between each one.
- Slicing can be used to reverse a sequence by using a negative step size.

- To iterate over a sequence, we can use a for loop, which is a control structure that repeats a block of code for each element of the sequence.
- The for loop has the syntax: for variable in sequence: block of code
- The variable takes the value of each element of the sequence in turn, and the block of code is executed with that value.
- The for loop can be used to perform various operations on a sequence, such as printing, counting, summing, filtering, mapping, etc.

- To test if a value is in a sequence, we can use the in operator, which returns True if the value is found in the sequence, and False otherwise.
- The in operator can also be used to test if a subsequence is in a sequence, by using the subsequence as the left operand and the sequence as the right operand.
- The in operator can be combined with the not operator to test if a value or a subsequence is not in a sequence.

- To compare two sequences, we can use the comparison operators, such as ==, !=, <, >, <=, >=, which return True or False depending on the result of the comparison.
- The comparison operators compare the sequences element by element, from left to right, until they find a difference or reach the end of one of the sequences.
- The comparison operators can also be used to compare a sequence with a single value, by using the sequence as the left operand and the value as the right operand.
- The comparison operators can be combined with the logical operators, such as and, or, not, to form complex conditions involving sequences.