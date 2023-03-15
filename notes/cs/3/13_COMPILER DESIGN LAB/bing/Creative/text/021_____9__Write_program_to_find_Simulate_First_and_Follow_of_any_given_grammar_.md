### 9. Write program to find Simulate First and Follow of any given grammar.

- First and Follow are two sets of symbols that are used to determine the parsing table of a grammar.
- First(X) is the set of terminals that can appear at the beginning of a string derived from X, where X is a non-terminal or a string of grammar symbols.
- Follow(X) is the set of terminals that can appear immediately after X, where X is a non-terminal.
- To find First and Follow of any given grammar, we can use the following algorithm:

  - For each terminal a, First(a) = {a}.
  - For each production X -> Y1Y2...Yn, add First(Y1) - {epsilon} to First(X). If First(Y1) contains epsilon, then add First(Y2) - {epsilon} to First(X), and so on. If all of Y1, Y2, ..., Yn can derive epsilon, then add epsilon to First(X).
  - Repeat the previous step until no more terminals can be added to any First set.
  - Initialize Follow(S) = {$}, where S is the start symbol and $ is the end-of-input marker.
  - For each production X -> Y1Y2...Yn, for each i such that 1 <= i < n, add First(Yi+1) - {epsilon} to Follow(Yi). If First(Yi+1) contains epsilon, or if i = n, then add Follow(X) to Follow(Yi).
  - Repeat the previous step until no more terminals can be added to any Follow set.

- To write a program to find First and Follow of any given grammar, we can use a data structure such as a dictionary or a map to store the First and Follow sets for each non-terminal, and iterate over the productions using the algorithm described above. We can also use a list or a set to store the terminals and non-terminals of the grammar, and check if a symbol is terminal or non-terminal by looking up in the list or set.
- Here is an example of a Python program that finds First and Follow of any given grammar:

```python
# A function to compute First of a symbol
def first(symbol, grammar, terminals, non_terminals):
  # If the symbol is a terminal, return a set containing the symbol
  if symbol in terminals:
    return {symbol}
  # If the symbol is epsilon, return a set containing epsilon
  elif symbol == "epsilon":
    return {"epsilon"}
  # If the symbol is a non-terminal, iterate over its productions
  elif symbol in non_terminals:
    result = set() # Initialize an empty set to store the result
    for production in grammar[symbol]: # For each production of the form symbol -> body
      body = production.split() # Split the body into a list of symbols
      first_of_body = first(body[0], grammar, terminals, non_terminals) # Compute First of the first symbol of the body
      result = result.union(first_of_body - {"epsilon"}) # Add First of the first symbol of the body to the result, excluding epsilon
      # If the first symbol of the body can derive epsilon, then continue with the next symbol of the body, and so on
      i = 1
      while "epsilon" in first_of_body and i < len(body):
        first_of_body = first(body[i], grammar, terminals, non_terminals) # Compute First of the next symbol of the body
        result = result.union(first_of_body - {"epsilon"}) # Add First of the next symbol of the body to the result, excluding epsilon
        i += 1
      # If all symbols of the body can derive epsilon, then add epsilon to the result
      if "epsilon" in first_of_body:
        result.add("epsilon")
    return result # Return the result
  else:
    # If the symbol is not valid, return an empty set
    return set()

# A function to compute Follow of a symbol
def follow(symbol, grammar, terminals, non_terminals, start_symbol):
  # If the symbol is the start symbol, return a set containing the end-of-input marker $
  if symbol == start_symbol:
    return {"$"}
  # If the symbol is a terminal, return an empty set
  elif symbol in terminals:
    return set()
  # If the symbol is a non-terminal, iterate over all productions of the grammar
  elif symbol in non_terminals:
    result = set() # Initialize an empty set to store the result
    for head in grammar: # For each head of a production
      for production in grammar[head]: # For each production