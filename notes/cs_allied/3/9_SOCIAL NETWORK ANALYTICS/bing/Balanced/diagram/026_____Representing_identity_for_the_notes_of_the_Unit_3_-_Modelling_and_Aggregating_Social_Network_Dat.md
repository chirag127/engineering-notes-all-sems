### Representing identity

- Identity is a key concept in social network analysis, as it refers to the way individuals or entities are identified and distinguished in a network.
- Identity can be represented by various attributes, such as name, email, phone number, location, gender, age, occupation, etc.
- Identity can also be represented by multiple identifiers, such as URIs, URLs, IDs, usernames, etc.
- Identity can be influenced by the context and the purpose of the network analysis, as different attributes or identifiers may be more relevant or useful for different scenarios or questions.
- Identity can be challenging to represent in a consistent and accurate way, as individuals or entities may have multiple or changing identities, or may use different identifiers in different platforms or domains.
- Identity can be represented in RDF (Resource Description Framework), a standard model for data interchange on the Web, using two main approaches:
  - One can introduce a separate resource and use the identifiers as URIs for these resources, and then link them to the main resource using properties such as `owl:sameAs` or `foaf:account`.
  - The other alternative is to choose one of the identifiers and use it as a URI for the main resource, and then add the other identifiers as literals using properties such as `foaf:homepage` or `foaf:mbox`.
- Identity can be visualized in a social network graph, where nodes represent individuals or entities, and edges represent relationships or interactions among them. The nodes can be labeled or colored by different attributes or identifiers, depending on the focus of the analysis. The edges can also be labeled or weighted by different types or strengths of relationships or interactions.