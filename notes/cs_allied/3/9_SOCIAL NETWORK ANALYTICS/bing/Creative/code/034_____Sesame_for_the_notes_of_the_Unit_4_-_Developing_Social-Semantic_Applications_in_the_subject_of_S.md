### Sesame

- Sesame is an open source framework for storing, querying and reasoning with RDF data.
- RDF (Resource Description Framework) is a standard model for data interchange on the Web that allows representing information as a graph of resources and properties.
- Sesame provides a Java API and a RESTful HTTP protocol for accessing and manipulating RDF data.
- Sesame supports various RDF serialization formats, such as RDF/XML, Turtle, N-Triples, N-Quads, TriG and JSON-LD.
- Sesame also supports different query languages, such as SPARQL, SeRQL and RQL.
- Sesame can be used to build semantic web applications that leverage the power of RDF and RDF Schema to model and integrate heterogeneous data sources.
- Sesame can also be used to add social network features to semantic web applications, such as discovering and analyzing relationships among resources, users and communities.
- Sesame has a modular architecture that consists of four main components:
  - SAIL (Storage And Inference Layer): a set of interfaces and implementations for storing and querying RDF data, with optional support for RDFS inferencing and transaction management.
  - Repository API: a high-level API for accessing and manipulating RDF data in a SAIL, with support for contexts, namespaces, transactions and query evaluation.
  - Rio (RDF I/O): a set of parsers and writers for various RDF serialization formats, with support for validation, error handling and data conversion.
  - HTTP Server: a web application that exposes a RESTful HTTP protocol for accessing and manipulating RDF data in a Repository, with support for content negotiation, authentication and authorization.

- Sesame can be extended with additional components, such as:
  - Elmo: a Java annotation framework that allows mapping Java objects to RDF resources and vice versa, with support for CRUD operations, transactions and queries.
  - GraphUtil: a utility class that provides methods for manipulating RDF graphs, such as extracting subgraphs, merging graphs, finding shortest paths and computing centrality measures.
  - Flink: a web application that uses Sesame, Elmo and GraphUtil to discover and analyze the social networks of the semantic web community, based on the extraction and integration of data from various sources, such as FOAF, SIOC, DOAP and SWRC .

: https://www.w3.org/2001/sw/wiki/Sesame
: https://www.w3.org/RDF/
: https://www.gbv.de/dms/mpib-toc/526896248.pdf
: https://corescholar.libraries.wright.edu/knoesis/196/
: https://www.researchgate.net/publication/324511430_Introduction_to_Semantic_Applications