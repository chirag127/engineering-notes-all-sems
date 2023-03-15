### Reasoning with Default Information

- Reasoning with default information is a form of non-monotonic reasoning that allows for drawing plausible conclusions from incomplete or uncertain premises by using general rules that may have exceptions .
- Non-monotonic reasoning is a type of reasoning that does not follow the principle of monotonicity, which states that adding new information to a set of premises cannot reduce the set of conclusions that can be derived from them.
- Reasoning with default information is useful in artificial intelligence because it can model common sense reasoning and handle situations where the information available is not sufficient or reliable to make definite conclusions .
- Some examples of reasoning with default information are:
  - Default assignments to variables: assigning a default value to a variable when no other value is given or known.
  - Closed world assumption: assuming that a statement is false if it cannot be proven to be true from the given information.
  - Frame default for causal worlds: assuming that the state of the world remains unchanged unless there is evidence of a change caused by an action or an event.
  - Exceptions as defaults: assuming that a general rule applies unless there is evidence of an exception.
  - Negation in artificial intelligence programming languages: using negation as a way of expressing default assumptions or expectations.
- Reasoning with default information requires two facilities: one that forces conclusions to be retracted in light of new refuting evidence and another that protects conclusions from retraction in light of new but irrelevant evidence.
- One of the most common formalisms for reasoning with default information is default logic, which consists of a set of facts, a set of default rules, and a set of consequences .
  - A fact is a statement that is known to be true.
  - A default rule is a statement of the form: p:q/r, which means that if p is true and q is consistent with the facts, then r can be assumed to be true, unless there is evidence to the contrary.
  - A consequence is a statement that can be derived from the facts and the default rules by applying a logical inference mechanism.
  - A default theory is a pair of a set of facts and a set of default rules.
  - An extension of a default theory is a set of consequences that is consistent with the facts and the default rules, and that satisfies the principle of specificity, which states that the more specific default rules should be preferred over the more general ones.
- Reasoning with default information is not a trivial task, as there may be multiple or conflicting extensions for a given default theory, or no extension at all. Different methods have been proposed to deal with these issues, such as circumscription, preferential logic, autoepistemic logic, and argumentation theory.