# Architectural approaches for the notes of the Unit 3 - Knowledge-Based Systems- AI Context in the subject of INTELLIGENT DATABASE SYSTEM

- A knowledge-based system (KBS) is a computer system that uses artificial intelligence to solve problems within a specialized domain that ordinarily requires human expertise .
- The typical architecture of a KBS consists of two main components: a knowledge base and an inference engine .
- The knowledge base contains a collection of facts, rules, heuristics, and other forms of knowledge representation that capture the domain expertise .
- The inference engine is a software module that applies logical rules and reasoning methods to the knowledge base to derive new information or solutions .
- There are different types of KBS architectures, depending on the nature of the knowledge base, the inference engine, and the interaction with the user or other systems .
- Some of the common KBS architectures are:

  - Rule-based systems: These systems use a set of if-then rules to represent the knowledge base and a forward or backward chaining algorithm to perform the inference . An example of a rule-based system is MYCIN, a medical diagnosis system for infectious diseases .
  - Frame-based systems: These systems use a hierarchical network of frames to represent the knowledge base and a slot-and-filler mechanism to perform the inference . A frame is a data structure that contains a set of attributes and values that describe an entity or a concept . An example of a frame-based system is KEE, a knowledge engineering environment for building expert systems .
  - Logic-based systems: These systems use a formal logic language, such as propositional logic, predicate logic, or description logic, to represent the knowledge base and a theorem prover or a model checker to perform the inference . An example of a logic-based system is PROLOG, a programming language for logic programming .
  - Case-based systems: These systems use a database of past cases or examples to represent the knowledge base and a similarity measure or a retrieval algorithm to perform the inference . A case is a record of a problem and its solution that can be reused or adapted for new situations . An example of a case-based system is CHEF, a cooking system that generates recipes based on user preferences and ingredients .
  - Neural network systems: These systems use a network of interconnected nodes or neurons to represent the knowledge base and a learning algorithm or a activation function to perform the inference . A neural network is a computational model that mimics the structure and function of the biological brain . An example of a neural network system is ALVINN, a self-driving car system that learns from human drivers .

- Some of the challenges and issues in designing and developing KBS architectures are:

  - Knowledge acquisition: This is the process of eliciting, analyzing, and encoding the domain knowledge from human experts or other sources into a suitable form for the knowledge base . This is often a difficult and time-consuming task, as the knowledge may be tacit, incomplete, inconsistent, or evolving .
  - Knowledge representation: This is the process of choosing an appropriate language or format to express the domain knowledge in the knowledge base . This involves trade-offs between expressiveness, efficiency, and scalability of the representation .
  - Knowledge reasoning: This is the process of applying logical rules and methods to the knowledge base to infer new information or solutions . This requires a balance between soundness, completeness, and tractability of the reasoning .
  - Knowledge validation: This is the process of verifying and validating the correctness and reliability of the knowledge base and the inference engine . This involves testing, debugging, and evaluating the performance and accuracy of the KBS .
  - Knowledge maintenance: This is the process of