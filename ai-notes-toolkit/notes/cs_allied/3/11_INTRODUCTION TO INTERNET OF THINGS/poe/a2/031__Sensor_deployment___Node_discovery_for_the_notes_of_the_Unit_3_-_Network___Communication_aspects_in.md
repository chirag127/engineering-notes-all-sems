 Here is the content in markdown format with points and without any emojis or external links:

### Sensor deployment & Node discovery

- Sensor deployment refers to the placement of sensors in a network to achieve desired coverage and connectivity. It depends on the application and its requirements.
- For monitoring large areas, a random deployment may be sufficient while for monitoring specific spots or points of interest, deliberate deployment is needed.
- Node discovery refers to the process by which nodes in a network detect the presence of and learn about other nodes.
- Node discovery is critical for network formation, routing, data aggregation, etc.
- Methods for node discovery:
-- Flooding: Nodes broadcast discovery messages periodically. This leads to high overhead and collisions.
-- Trie-based: Nodes use a trie data structure to store information about other nodes. Scalability is limited.
-- Location-based: If nodes know their location, they can limit discovery to neighboring nodes leading to lower overhead. Location information may not always be available.
-- Code-based: Nodes allocate and share codes to identify and discover each other. Extra mechanisms are needed to handle code conflicts and exhaustion.

The above content summarizes the key points around sensor deployment and node discovery in a formal tone without any emojis or external links as requested. Please let me know if you would like me to modify or add any other points.