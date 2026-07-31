```markdown
### Reasoning with Default Information

- Reasoning with default information is a form of non-monotonic reasoning that allows for drawing plausible conclusions from incomplete or uncertain premises by using general rules that may have exceptions .
- Non-monotonic reasoning is a type of reasoning that does not follow the principle of monotonicity, which states that adding new information to a set of premises cannot reduce the set of conclusions that can be derived from them.
- Reasoning with default information is useful in artificial intelligence because it can model common sense reasoning and deal with situations where the information available is not sufficient or reliable to make definite conclusions .
- Some examples of reasoning with default information are:
  - Default assignments to variables: assigning a default value to a variable when its actual value is unknown or irrelevant.
  - Closed world assumption: assuming that a statement is false if it cannot be proven to be true from the given information.
  - Frame default for causal worlds: assuming that the effects of an action are limited to those explicitly specified and that everything else remains unchanged.
  - Exceptions as defaults: assuming that a general rule applies unless there is evidence that the case at hand is exceptional.
  - Negation in artificial intelligence programming languages: using negation as failure or negation by default to represent the absence of positive information.
- One of the most influential formalisms for reasoning with default information is default logic, which was proposed by Raymond Reiter in 1980 .
- Default logic consists of a set of facts (the background theory) and a set of default rules, each of which has the form:

  ```
  p : q / r
  ```

  where p, q, and r are logical formulas. This means that if p is true and q is consistent with the facts, then r can be concluded by default .
- A default theory is a pair (D, W), where D is a set of default rules and W is a set of facts. A default theory can have multiple extensions, which are sets of conclusions that can be derived from the theory by applying the default rules in a consistent way .
- An extension is said to be normal if it contains the consequent of every default rule whose prerequisite is in the extension and whose justification is consistent with the extension .
- An extension is said to be skeptical if it is a subset of every other extension of the same default theory. A skeptical extension represents the conclusions that are common to all possible extensions .
- An extension is said to be credulous if it is not a subset of any other extension of the same default theory. A credulous extension represents the conclusions that are specific to one possible extension .
- An example of a default theory is:

  ```
  D = {bird : flies / flies, penguin : ¬flies / ¬flies}
  W = {bird(tweety), penguin(tweety)}
  ```

  This means that birds usually fly, but penguins do not fly, and tweety is a bird and a penguin. The default theory has two extensions:

  ```
  E1 = {bird(tweety), penguin(tweety), ¬flies(tweety)}
  E2 = {bird(tweety), penguin(tweety), flies(tweety)}
  ```

  E1 is the normal and skeptical extension, because it follows the more specific default rule for penguins and it is a subset of E2. E2 is the credulous extension, because it follows the more general default rule for birds and it is not a subset of E1 .
```