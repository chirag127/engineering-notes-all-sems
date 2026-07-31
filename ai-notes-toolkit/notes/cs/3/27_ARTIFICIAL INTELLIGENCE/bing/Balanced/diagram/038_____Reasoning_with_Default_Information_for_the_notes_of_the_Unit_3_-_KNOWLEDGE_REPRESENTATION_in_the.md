# Reasoning with Default Information

- Reasoning with default information is a form of non-monotonic reasoning that allows for drawing plausible conclusions from incomplete or uncertain premises by using general rules that may have exceptions .
- Non-monotonic reasoning is a type of reasoning that does not follow the principle of monotonicity, which states that adding new information to a set of premises cannot reduce the set of conclusions that can be derived from them.
- Reasoning with default information is useful in artificial intelligence because it can model common sense reasoning and deal with situations where the available information is not sufficient to make definite conclusions .
- Some examples of default reasoning in artificial intelligence are:
  - Default assignments to variables: assigning a default value to a variable when no specific value is given or known, such as `color(x) = red` unless otherwise specified.
  - Closed world assumption: assuming that the facts that are not explicitly stated in a knowledge base are false, such as `bird(x) -> flies(x)` unless `x` is a penguin or an ostrich.
  - Frame default for causal worlds: assuming that the effects of an action are limited to those that are explicitly specified, such as `move(x,y) -> at(x,y)` and `~at(x,z)` unless `z = y` or `z` is affected by the move.
  - Exceptions as defaults: using default rules to handle exceptional cases, such as `bird(x) -> flies(x)` unless `abnormal(x)`.
  - Negation in artificial intelligence programming languages: using negation as failure to infer the negation of a predicate when it cannot be proven, such as `~flies(x)` if `flies(x)` fails.
- The main features of default reasoning are :
  - Default rules: rules that have the form `p : q / r`, which means that if `p` is true and `q` is consistent with the current knowledge, then `r` can be assumed to be true, unless there is evidence to the contrary.
  - Default theories: sets of default rules and facts that form the basis of default reasoning.
  - Extensions: sets of conclusions that can be derived from a default theory by applying default rules as long as they are consistent.
  - Skeptical and credulous reasoning: two modes of default reasoning that differ in how they handle multiple extensions. Skeptical reasoning only accepts conclusions that are common to all extensions, while credulous reasoning accepts conclusions that are true in at least one extension.
- A simple example of default reasoning is:

  - Default theory: `{bird(x) -> flies(x) : flies(x) / flies(x), bird(tweety), abnormal(polly)}`
  - Extensions: `{bird(tweety), flies(tweety), abnormal(polly)}` and `{bird(tweety), abnormal(polly), ~flies(tweety)}`
  - Skeptical reasoning: `bird(tweety)` and `abnormal(polly)` are true, but `flies(tweety)` is unknown.
  - Credulous reasoning: `bird(tweety)` and `abnormal(polly)` are true, and `flies(tweety)` is either true or false depending on the extension.