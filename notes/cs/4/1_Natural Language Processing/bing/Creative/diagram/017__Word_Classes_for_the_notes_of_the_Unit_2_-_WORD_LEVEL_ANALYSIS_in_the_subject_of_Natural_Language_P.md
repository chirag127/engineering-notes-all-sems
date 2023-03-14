Word classes are categories of words that share some common characteristics, such as grammatical function, morphology, or meaning. In natural language processing, word classes are often used to label words in a text with their part-of-speech (POS) tags, which indicate the syntactic role and the possible meanings of each word. For example, nouns are words that can act as subjects or objects of verbs, and can usually take plural or possessive forms. Verbs are words that express actions or states, and can usually be modified by tense, aspect, mood, or voice. Adjectives are words that modify nouns, and can usually be compared or graded. Adverbs are words that modify verbs, adjectives, or other adverbs, and can usually indicate manner, degree, time, place, or frequency.

There are different ways to define and classify word classes, depending on the language and the level of detail needed for the task. Some word classes are more universal, such as nouns, verbs, adjectives, and adverbs, while others are more language-specific, such as articles, determiners, pronouns, prepositions, conjunctions, interjections, and particles. Some word classes are more fine-grained, such as subtypes of nouns (e.g., proper nouns, common nouns, count nouns, mass nouns), verbs (e.g., transitive verbs, intransitive verbs, auxiliary verbs, modal verbs), adjectives (e.g., attributive adjectives, predicative adjectives, gradable adjectives, non-gradable adjectives), and adverbs (e.g., manner adverbs, degree adverbs, time adverbs, place adverbs, frequency adverbs). Some word classes are more ambiguous, such as words that can belong to more than one word class depending on the context (e.g., book can be a noun or a verb, fast can be an adjective or an adverb).

The following diagram illustrates the basic word classes and some of their subtypes using ASCII art:

```
+-----------------+-----------------+-----------------+-----------------+
|     NOUNS      |     VERBS      |   ADJECTIVES    |    ADVERBS      |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
| +-------------+ | +-------------+ | +-------------+ | +-------------+ |
| | Proper Nouns| | | Transitive  | | | Attributive | | | Manner      | |
| +-------------+ | | Verbs       | | +-------------+ | | Adverbs     | |
| | e.g., Alice | | +-------------+ | | e.g., red    | | +-------------+ |
| +-------------+ | | e.g., eat   | | +-------------+ | | e.g., slowly | |
|                 | +-------------+ |                 | +-------------+ |
| +-------------+ | +-------------+ | +-------------+ | +-------------+ |
| | Common Nouns| | | Intransitive| | | Predicative | | | Degree      | |
| +-------------+ | | Verbs       | | +-------------+ | | Adverbs     | |
| | e.g., book  | | +-------------+ | | e.g., happy  | | +-------------+ |
| +-------------+ | | e.g., sleep | | +-------------+ | | e.g., very   | |
|                 | +-------------+ |                 | +-------------+ |
| +-------------+ | +-------------+ | +-------------+ | +-------------+ |
| | Count Nouns | | | Auxiliary   | | | Gradable    | | | Time        | |
| +-------------+ | | Verbs       | | +-------------+ | | Adverbs     | |
| | e.g., apple | | +-------------+ | | e.g., big    | | +-------------+ |
| +-------------+ | | e.g., be    | | +-------------+ | | e.g., now    | |
|                 | +-------------+ |                 | +-------------+ |
| +-------------+ | +-------------+ | +-------------+ | +-------------+ |
| | Mass Nouns  | | | Modal Verbs | | | Non-gradable| | | Place       | |
| +-------------+ | +-------------+ | +-------------+ | | Adverbs     | |
| | e.g., water | | | e.g., can   | | | e.g., unique | | +-------------+ |
| +-------------+ | +-------------+ | +-------------+ | | e.g., here   | |
|