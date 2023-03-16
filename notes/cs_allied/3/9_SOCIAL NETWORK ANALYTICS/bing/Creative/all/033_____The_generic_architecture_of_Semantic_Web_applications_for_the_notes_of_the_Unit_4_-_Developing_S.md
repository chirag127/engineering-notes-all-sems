# The generic architecture of Semantic Web applications

Semantic Web applications are software systems that use Semantic Web technologies to provide intelligent and interoperable services on the Web. Semantic Web technologies include standards and languages for representing and querying data, such as RDF, OWL, SPARQL, etc. Semantic Web applications can also use ontologies, which are formal and explicit specifications of the concepts and relationships in a domain of interest.

The generic architecture of Semantic Web applications can be described by the following layers:

- **URI and Unicode layer**: This layer follows the existing features of the Web, such as using Uniform Resource Identifiers (URIs) to identify resources and Unicode to encode international character sets.
- **XML layer**: This layer provides a common syntax for data exchange and validation, using Extensible Markup Language (XML), XML namespaces, and XML Schema definitions.
- **RDF layer**: This layer provides a data model and a syntax for representing and exchanging data as graphs of resources and properties, using Resource Description Framework (RDF), RDF Schema, and RDF serializations (such as RDF/XML, Turtle, JSON-LD, etc.).
- **Ontology layer**: This layer provides a language and a logic for defining and reasoning about the concepts and relationships in a domain, using Web Ontology Language (OWL) and its profiles (such as OWL 2 EL, OWL 2 QL, OWL 2 RL, etc.).
- **Query and Inference layer**: This layer provides a language and a mechanism for querying and inferring data from RDF graphs and ontologies, using SPARQL Protocol and RDF Query Language (SPARQL) and its extensions (such as SPARQL 1.1 Federated Query, SPARQL 1.1 Update, SPARQL 1.1 Entailment Regimes, etc.).
- **Rules layer**: This layer provides a language and a mechanism for defining and executing rules on RDF graphs and ontologies, using Rule Interchange Format (RIF) and its dialects (such as RIF Basic Logic Dialect, RIF Production Rule Dialect, RIF Core, etc.).
- **Trust and Proof layer**: This layer provides a framework and a mechanism for establishing and verifying the trustworthiness and provenance of data and services on the Semantic Web, using Web of Trust, digital signatures, certificates, etc.
- **User Interface and Applications layer**: This layer provides the tools and the methods for developing and interacting with Semantic Web applications, such as browsers, editors, visualizers, annotators, etc.

The following diagram illustrates the generic architecture of Semantic Web applications:

![Semantic Web Stack](https://upload.wikimedia.org/wikipedia/commons/4/4e/Semantic_web_stack.svg)

Some examples of Semantic Web applications are:

- **DBpedia**: A Semantic Web application that extracts structured data from Wikipedia and makes it available as RDF graphs and SPARQL endpoints.
- **Bio2RDF**: A Semantic Web application that integrates and interlinks biological data from various sources and provides a unified access point for querying and exploring the data.
- **LinkedGeoData**: A Semantic Web application that transforms OpenStreetMap data into RDF and provides a SPARQL endpoint and a map interface for querying and visualizing the data.
- **MusicBrainz**: A Semantic Web application that provides a comprehensive music database and a service for identifying and tagging music files.
- **Semantic MediaWiki**: A Semantic Web application that extends the functionality of MediaWiki by allowing users to annotate and query wiki pages using RDF and SPARQL.