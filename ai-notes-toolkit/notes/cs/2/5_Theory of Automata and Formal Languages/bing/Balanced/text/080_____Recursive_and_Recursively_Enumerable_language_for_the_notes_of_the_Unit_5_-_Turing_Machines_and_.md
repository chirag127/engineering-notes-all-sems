### Recursive and Recursively Enumerable language

- A **recursive language** is a formal language for which there exists a Turing machine (or other computable function) that will halt and accept when presented with any string in the language as input and will halt and reject when presented with any string not in the language .
- A **recursively enumerable language** is a formal language for which there exists a Turing machine (or other computable function) that will halt and accept when presented with any string in the language as input but may either halt and reject or loop forever when presented with a string not in the language .
- A recursive language is also recursively enumerable, but the converse is not true.
- A recursively enumerable language can be recognized by an enumerator, which is a Turing machine that outputs all the strings in the language in some order .
- A recursive language can be decided by a decider, which is a Turing machine that always halts and outputs yes or no depending on whether the input string is in the language or not .
- A recursively enumerable language is also called semi-decidable, because it can be decided for some inputs but not for all.
- A language that is not recursively enumerable is called non-enumerable or undecidable .