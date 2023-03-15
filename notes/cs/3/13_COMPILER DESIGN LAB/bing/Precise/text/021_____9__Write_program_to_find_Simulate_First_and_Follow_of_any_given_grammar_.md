### 9. Write program to find Simulate First and Follow of any given grammar.

First and Follow are important concepts in the construction of predictive parsers for context-free grammars. The First set of a symbol is the set of terminal symbols that can appear as the first symbol in a string derived from that symbol. The Follow set of a symbol is the set of terminal symbols that can appear immediately after that symbol in a sentential form.

Here is an example of how to find the First and Follow sets of a given grammar:

1. Begin by finding the First set for each terminal symbol. The First set of a terminal symbol is simply the terminal symbol itself.
2. For each production rule in the grammar, find the First set of the right-hand side of the rule. If the first symbol on the right-hand side is a terminal symbol, then the First set of the right-hand side is the First set of that terminal symbol. If the first symbol on the right-hand side is a non-terminal symbol, then the First set of the right-hand side is the union of the First sets of all the productions that have that non-terminal symbol on the left-hand side.
3. To find the Follow set of a non-terminal symbol, begin by adding the end-of-input marker to the Follow set of the start symbol. Then, for each production rule in the grammar, if the non-terminal symbol appears on the right-hand side of the rule, add the First set of the symbol immediately following it to the Follow set of the non-terminal symbol. If there is no symbol following the non-terminal symbol, or if the First set of the following symbol contains the empty string, then add the Follow set of the left-hand side of the rule to the Follow set of the non-terminal symbol.
4. Repeat step 3 until no more terminal symbols can be added to any Follow set.

Here is an example of a program that finds the First and Follow sets of a given grammar:

```python
def first(symbol, grammar):
    first_set = set()
    if symbol.isupper():
        for rule in grammar[symbol]:
            if rule == 'epsilon':
                first_set.add('epsilon')
            else:
                first_set = first_set.union(first(rule[0], grammar))
    else:
        first_set.add(symbol)
    return first_set

def follow(symbol, grammar, follow_sets):
    follow_set = set()
    if symbol == list(grammar.keys())[0]:
        follow_set.add('$')
    for key, rules in grammar.items():
        for rule in rules:
            if symbol in rule:
                index = rule.index(symbol)
                if index == len(rule) - 1:
                    follow_set = follow_set.union(follow_sets[key])
                else:
                    first_set = first(rule[index + 1], grammar)
                    if 'epsilon' in first_set:
                        first_set.remove('epsilon')
                        follow_set = follow_set.union(follow_sets[key])
                    follow_set = follow_set.union(first_set)
    return follow_set

def first_follow(grammar):
    first_sets = {}
    follow_sets = {}
    for key in grammar.keys():
        first_sets[key] = first(key, grammar)
        follow_sets[key] = set()
    while True:
        prev_follow_sets = follow_sets.copy()
        for key in grammar.keys():
            follow_sets[key] = follow(key, grammar, follow_sets)
        if prev_follow_sets == follow_sets:
            break
    return first_sets, follow_sets

grammar = {
    'S': ['AB', 'BC'],
    'A': ['aA', 'epsilon'],
    'B': ['bB', 'epsilon'],
    'C': ['cC', 'epsilon']
}

first_sets, follow_sets = first_follow(grammar)

print('First sets:')
for key, value in first_sets.items():
    print(key, value)

print('Follow sets:')
for key, value in follow_sets.items():
    print(key, value)
```

This program defines three functions: `first`, `follow`, and `first_follow`. The `first` function takes a symbol and a grammar as input and returns the First set of the symbol. The `follow` function takes a symbol, a grammar, and a dictionary of Follow sets as input and returns the Follow set of the symbol. The `first_follow` function takes a grammar as input and returns the First and Follow sets of all the non-terminal symbols in the grammar.

The program then defines a grammar as a dictionary, where the keys are the non-terminal symbols and the values are lists of production rules. The program calls the `first_follow` function to find the First and Follow sets of the grammar, and then prints the results.

This is an example of how to write a program to find the First and Follow sets of a given grammar. It