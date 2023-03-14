 Here is the content in markdown format for ### Word Sense Disambiguation for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing:

### Word Sense Disambiguation

- Words in language can have multiple meanings (senses). For example, the word *bank* can refer to a financial institution or the land alongside a river. The process of identifying the correct sense of a word based on the context is called **Word Sense Disambiguation (WSD)**.
- WSD is a major challenge in NLP as the same word can have multiple meanings (homonymy) or a meaning can have multiple words (polysemy). Ambiguity leads to problems in machine translation, information retrieval, etc.
- Some approaches for WSD:
	- Dictionary-based: Match the context words with the definitions of the senses of the ambiguous word. The sense with the most matching words is selected.
	- Supervised learning: Manually annotate data with correct senses, train a classifier using features like context words, POS tags, etc. and use the trained model for new data.
	- Unsupervised learning: Cluster occurrences of the ambiguous word based on context similarity and assign cluster centroids as word senses.
	- Knowledge-based: Use external knowledge sources like ontologies or thesauri to determine the sense.
- Applications of WSD include:
	- Improving machine translation
	- Improving question answering systems
	- Improving information retrieval
	- Word sense induction (identifying word senses from unannotated corpus)

Some mnemonics for remembering WSD:

- Disambiguate word: Determine the one true sense
- Context is key: Context words help select the sense
- Supervise the senses: Classify senses using supervised learning
- Cluster and label: Group similar contexts and assign senses (unsupervised)
- Know it all: Use knowledge sources for disambiguation

Does this help? Let me know if you would like me to modify or expand the content.