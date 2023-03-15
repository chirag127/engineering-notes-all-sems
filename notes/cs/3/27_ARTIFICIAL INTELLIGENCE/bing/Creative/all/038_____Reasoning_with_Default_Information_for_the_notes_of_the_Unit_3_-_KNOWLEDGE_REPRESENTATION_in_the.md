Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of Reasoning with Default Information for the Unit 3 - Knowledge Representation in the subject of Artificial Intelligence KCS. Here are some points you can use:

# Reasoning with Default Information

- Reasoning with default information is a type of non-monotonic reasoning that allows us to draw conclusions based on incomplete or uncertain knowledge, using default rules or assumptions that can be overridden by more specific or reliable information.
- For example, if we know that birds can fly, we can use this as a default rule to infer that Tweety can fly, unless we have more specific information that Tweety is a penguin or has a broken wing.
- Default rules have the form: p : q / q, which means that if p is true, then we can assume q is true, unless there is evidence to the contrary. For example, bird : fly / fly is a default rule that says that if something is a bird, then we can assume it can fly, unless we have evidence to the contrary.
- Default logic is a formalism for reasoning with default information, proposed by Reiter in 1980. It consists of a set of facts, a set of default rules, and a set of integrity constraints that must be satisfied by any conclusion.
- A default theory is a pair (D, W), where D is a set of default rules and W is a set of facts. A default theory can have multiple extensions, which are consistent sets of conclusions that can be derived from the theory using the default rules and the facts.
- An extension is a set of formulas E such that:
  - E is consistent with W and the integrity constraints.
  - E is closed under logical consequence, i.e., if E entails a formula, then that formula is in E.
  - E contains the consequent of any default rule whose prerequisite is in E and whose justification is consistent with E.
- For example, consider the following default theory:

  - W = {bird(Tweety), bird(Polly), penguin(Polly)}
  - D = {bird : fly / fly, penguin : ¬fly / ¬fly}
  - This theory has two extensions: {bird(Tweety), bird(Polly), penguin(Polly), fly(Tweety)} and {bird(Tweety), bird(Polly), penguin(Polly), ¬fly(Polly)}.
- A default theory may have no extensions, if there is no consistent way to apply the default rules. For example, the following theory has no extensions:

  - W = {bird(Tweety)}
  - D = {bird : fly / fly, bird : ¬fly / ¬fly}
  - This theory is inconsistent, because applying either default rule leads to a contradiction.
- A default theory may have a unique extension, if there is only one consistent way to apply the default rules. For example, the following theory has a unique extension:

  - W = {bird(Tweety), penguin(Tweety)}
  - D = {bird : fly / fly, penguin : ¬fly / ¬fly}
  - The unique extension is {bird(Tweety), penguin(Tweety), ¬fly(Tweety)}.
- A default theory may have multiple extensions, if there are different consistent ways to apply the default rules. For example, the following theory has multiple extensions:

  - W = {bird(Tweety)}
  - D = {bird : fly / fly, bird : swim / swim}
  - The extensions are {bird(Tweety), fly(Tweety)} and {bird(Tweety), swim(Tweety)}.
- A default theory is normal if all the default rules have the same formula in the prerequisite and the consequent. For example, the following theory is normal:

  - W = {bird(Tweety), bird(Polly), penguin(Polly)}
  - D = {bird : fly / fly, penguin : ¬fly / ¬fly}
  - A normal default theory always has at least one extension, which is the smallest one that contains all the facts and the consequents of the default rules whose prerequisites are facts. This extension is called the normal extension. For example, the normal extension of the above theory is {bird(Tweety), bird(Polly), penguin(Polly), fly(Tweety), ¬fly(Polly)}.
- A default theory is semi-normal if all the default rules have the same formula or its negation in the prerequisite and the consequent. For example, the following theory is semi-normal:

  - W = {bird(Tweety)}
  - D = {bird : fly / fly, ¬bird : swim /