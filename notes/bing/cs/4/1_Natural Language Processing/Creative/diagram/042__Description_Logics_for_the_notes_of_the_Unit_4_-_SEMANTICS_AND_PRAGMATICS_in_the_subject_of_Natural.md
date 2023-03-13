Description Logics (DL) are a family of formal knowledge representation languages that are widely used in AI applications for representing and reasoning about the properties of concepts and individuals . They are closely related to first-order logic, but with a more restricted syntax that makes them more suitable for automated reasoning. They can be used for configuration knowledge representation, especially for the design of component type hierarchies (ontologies) and for coherence analysis. They also provide one of the main underpinnings for the OWL Web Ontology Language as standardized by the World Wide Web Consortium (W3C) .

The following diagram illustrates the basic architecture of a DL system:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Knowledge Base |     |  Reasoner       |     |  Query Answerer |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  TBox           |     |  Classification |     |  Query          |
|  ABox           |     |  Consistency    |     |  Answer         |
|                 |     |  Satisfiability |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Concepts       |     |  Subsumption    |     |  Concept        |
|  Roles          |     |  Equivalence    |     |  Role           |
|  Individuals    |     |  Disjointness   |     |  Individual     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

A knowledge base (KB) consists of two components: a TBox and an ABox. A TBox contains the terminological knowledge, which defines the concepts and roles used in the domain of interest. An ABox contains the assertional knowledge, which states facts about individuals and their relationships. Concepts, roles and individuals are the basic building blocks of DLs. Concepts represent sets of objects, roles represent binary relations between objects, and individuals represent specific objects.

A reasoner is a software component that performs logical inference on the knowledge base. It can perform various reasoning tasks, such as classification, consistency checking, and satisfiability checking. Classification is the process of organizing the concepts in the TBox into a hierarchy based on their subsumption relationships. Consistency checking is the process of verifying that the knowledge base does not contain any contradictions. Satisfiability checking is the process of determining whether a concept has any instances in the domain.

A query answerer is a software component that allows users to query the knowledge base and obtain answers. It can perform various query tasks, such as concept, role and individual queries. Concept queries ask for the instances of a given concept. Role queries ask for the pairs of individuals that are related by a given role. Individual queries ask for the properties of a given individual.