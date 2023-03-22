 Here is the content in markdown format without any emojis or external links and in a formal tone:

## Unit 3 - Coding a sequence

1. Sequence: A sequence is a ordered collection of elements. In programming, sequences are used to store multiple values in a single variable.
2. Types of sequences: The common types of sequences used in programming are:
    - Lists: Lists are mutable sequences that are enclosed in square brackets []. Elements in a list can be accessed using an index.
    - Tuples: Tuples are immutable sequences that are enclosed in parentheses (). Elements in a tuple cannot be modified once defined.
    - Strings: Strings are immutable sequences of characters enclosed in either single ('') or double ("") quotes. String elements can be accessed using indexing.
3. Accessing elements: The elements in a sequence can be accessed using their index. Indexing starts from 0. For example:
    - List: my_list = ["a", "b", "c"]
            my_list[0] = "a"   //First element
    - Tuple: my_tuple = ("x", "y", "z")
            my_tuple[2] = "z"   //Third element
    - String: my_string = "abc"
             my_string[1] = "b"   //Second character
4. Slicing: Extracting parts of a sequence is known as slicing. It can be done by specifying the start and end index separated by a colon :. For example:
    - my_list[1:3]   //Elements at index 1 and 2
    - my_tuple[2:]   //Elements from index 2 till the end
    - my_string[:3]  //First 3 characters
5. Built-in functions: Python provides various built-in functions to work with sequences like len(), min(), max(), sum(), sorted(), etc. These functions can be used to find the length, minimum value, maximum value, sum of elements and sort the elements in a sequence respectively.