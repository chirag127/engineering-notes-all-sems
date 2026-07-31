### 9. Write program to find Simulate First and Follow of any given grammar

First and Follow are two important concepts in the construction of predictive parsers for context-free grammars. The First set of a symbol is the set of terminal symbols that can appear as the first symbol in a string derived from that symbol. The Follow set of a symbol is the set of terminal symbols that can appear immediately after that symbol in a sentential form.

Here is an example program to find the First and Follow sets of any given grammar:

```python
def first(symbol, productions):
    first_set = set()
    if symbol.isupper():
        for production in productions[symbol]:
            if production == 'epsilon':
                first_set.add('epsilon')
            else:
                for s in production:
                    first_set = first_set.union(first(s, productions))
                    if 'epsilon' not in first_set:
                        break
                    else:
                        first_set.discard('epsilon')
    else:
        first_set.add(symbol)
    return first_set

def follow(symbol, productions, start_symbol):
    follow_set = set()
    if symbol == start_symbol:
        follow_set.add('$')
    for key, value in productions.items():
        for production in value:
            if symbol in production:
                index = production.index(symbol)
                if index == len(production) - 1:
                    if key != symbol:
                        follow_set = follow_set.union(follow(key, productions, start_symbol))
                else:
                    first_set = first(production[index + 1], productions)
                    if 'epsilon' in first_set:
                        first_set.discard('epsilon')
                        if key != symbol:
                            follow_set = follow_set.union(follow(key, productions, start_symbol))
                    follow_set = follow_set.union(first_set)
    return follow_set

# Example grammar
productions = {
    'S': ['AB', 'BC'],
    'A': ['BA', 'a'],
    'B': ['CC', 'b'],
    'C': ['AB', 'a']
}

start_symbol = 'S'

# Find First sets
first_sets = {}
for symbol in productions.keys():
    first_sets[symbol] = first(symbol, productions)
print("First sets:")
for key, value in first_sets.items():
    print(key, value)

# Find Follow sets
follow_sets = {}
for symbol in productions.keys():
    follow_sets[symbol] = follow(symbol, productions, start_symbol)
print("Follow sets:")
for key, value in follow_sets.items():
    print(key, value)
```

This program defines two functions, `first` and `follow`, which take as input a symbol, the productions of the grammar, and the start symbol (in the case of the `follow` function), and return the First and Follow sets of the given symbol, respectively. The program then uses these functions to find the First and Follow sets of all the symbols in the given grammar.