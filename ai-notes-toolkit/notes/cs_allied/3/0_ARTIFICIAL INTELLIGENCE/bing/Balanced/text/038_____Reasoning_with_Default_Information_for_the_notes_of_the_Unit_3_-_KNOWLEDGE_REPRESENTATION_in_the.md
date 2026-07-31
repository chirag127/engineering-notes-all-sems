### Reasoning with Default Information

- Reasoning with default information is a form of non-monotonic reasoning that allows for drawing plausible conclusions from incomplete or uncertain information, based on general rules that may have exceptions .
- Non-monotonic reasoning is a type of reasoning that does not follow the principle of monotonicity, which states that adding new information to a set of premises cannot reduce the set of conclusions that can be derived from them. In other words, non-monotonic reasoning allows for revising or retracting conclusions when new information contradicts or invalidates them .
- Reasoning with default information is useful in artificial intelligence because it can model common sense reasoning and deal with situations where the knowledge base is not complete or consistent .
- One of the most influential formalisms for reasoning with default information is default logic, proposed by Raymond Reiter in 1980 . Default logic consists of a set of facts, a set of default rules, and a set of justifications. A default rule has the form:

  ```
  p : q / r
  ```

  which means that if p is true and q is consistent with the facts, then r can be concluded by default. However, this conclusion can be withdrawn if there is evidence that r is false or that the case is exceptional. A justification is a proof that shows why a default rule is applicable or not .

- An example of a default rule is:

  ```
  bird : flies / flies
  ```

  which means that if something is a bird and it is consistent with the facts that it flies, then it can be concluded by default that it flies. However, this conclusion can be withdrawn if there is evidence that the bird is a penguin or that it has a broken wing .

- A default theory is a pair of a set of facts and a set of default rules. A default theory can have multiple extensions, which are sets of conclusions that are consistent with the facts and the default rules. An extension is preferred if it contains more default conclusions than another extension. A default theory is normal if it has a unique preferred extension .
- An example of a default theory is:

  ```
  Facts: {bird(tweety), bird(polly), penguin(polly)}
  Default rules: {bird : flies / flies, penguin : ¬flies / ¬flies}
  ```

  This default theory has two extensions: {bird(tweety), bird(polly), penguin(polly), flies(tweety)} and {bird(tweety), bird(polly), penguin(polly), ¬flies(polly)}. The first extension is preferred because it contains more default conclusions than the second one .

- Reasoning with default information can be applied to various domains and problems in artificial intelligence, such as natural language understanding, planning, diagnosis, and commonsense reasoning . However, it also faces some challenges and limitations, such as computational complexity, non-uniqueness of extensions, and lack of expressiveness for some types of defaults .