# Reasoning with Default Information

- Reasoning with default information is a form of non-monotonic reasoning that allows for drawing plausible conclusions from incomplete or uncertain premises by using general rules that may have exceptions .
- Non-monotonic reasoning is a type of reasoning that does not follow the principle of monotonicity, which states that adding new information to a set of premises cannot reduce the set of conclusions that can be derived from them.
- Reasoning with default information is useful in artificial intelligence because it can model common sense reasoning and deal with situations where the available information is not sufficient to make definite inferences .
- Some examples of reasoning with default information are:
  - Default assignments to variables: assigning a default value to a variable unless there is evidence to the contrary. For example, if we have a variable x that represents the age of a person, we can assign a default value of 30 to x unless we have more specific information about the person's age.
  - Closed world assumption: assuming that the information given is complete and that anything not explicitly stated is false. For example, if we have a database of students and their courses, we can assume that any student not in the database is not taking any courses.
  - Frame default for causal worlds: assuming that the state of the world remains unchanged unless there is a cause for change. For example, if we have a rule that says that if a switch is turned on, a light bulb will light up, we can assume that the light bulb will remain lit unless the switch is turned off or the bulb is broken.
  - Exceptions as defaults: assuming that a general rule applies unless there is an exception to the rule. For example, if we have a rule that says that birds can fly, we can assume that any bird can fly unless it is a penguin or an ostrich or has some other reason to not fly.
  - Negation in artificial intelligence programming languages: using negation as a way of expressing default information or assumptions. For example, in Prolog, a logic programming language, we can use negation as failure to mean that something is false if it cannot be proven to be true.
- Reasoning with default information involves two main components: default rules and default logic .
  - Default rules are rules of the form: if p, then normally q, where p is the prerequisite, q is the consequent, and normally is a modal operator that indicates that the rule may have exceptions . For example, a default rule could be: if x is a bird, then normally x can fly.
  - Default logic is a formal system that defines how to apply default rules and how to handle inconsistencies and conflicts among them . Default logic consists of a set of facts (the background knowledge), a set of default rules, and a set of extensions (the possible sets of conclusions that can be derived from the facts and the rules) . For example, a default logic could be: {x is a bird, x is a penguin} (the facts), {if x is a bird, then normally x can fly} (the default rule), and {{x is a bird, x is a penguin, not x can fly}} (the extension).
- Reasoning with default information has some challenges and limitations, such as:
  - How to represent and acquire default information in a reliable and consistent way .
  - How to deal with multiple and conflicting default rules and extensions .
  - How to handle exceptions and revisions of default information .
  - How to evaluate the validity and usefulness of default information and reasoning .