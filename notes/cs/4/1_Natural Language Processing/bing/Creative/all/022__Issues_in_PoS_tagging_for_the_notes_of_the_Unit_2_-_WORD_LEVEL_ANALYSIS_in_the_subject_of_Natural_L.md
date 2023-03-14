### Issues in PoS tagging for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

- Part-of-speech (PoS) tagging is the task of assigning each word in a sentence the proper syntactic tag in its context of appearance .
- PoS tagging is a fundamental problem in natural language processing (NLP) and a building block for many NLP applications, such as information retrieval, information extraction, machine translation, question-answering, speech synthesis and recognition, and so on  .
- PoS tagging is also a disambiguation task, as a word can have multiple PoS tags depending on how the word is used in a sentence. For example, the word "book" can be a noun when used as "I like to read books" or a verb when used as "Book the flight"  .
- The main issue that must be addressed in PoS tagging is that of ambiguity: words behave differently given different contexts in most languages, and thus the difficulty is to identify the correct tag of a word appearing in a particular sentence  .
- Some of the factors that contribute to the ambiguity in PoS tagging are:
  - Homographs: words that have the same spelling but different meanings and PoS tags, such as "lead" (noun or verb), "wind" (noun or verb), "bat" (noun or verb), etc.
  - Morphological variations: words that have different forms but the same root, such as "sing", "sang", "sung", "singer", "singing", etc.
  - Compound words: words that are formed by combining two or more words, such as "blackboard", "hotdog", "fireworks", etc.
  - Contractions: words that are shortened by omitting some letters, such as "don't", "can't", "I'm", etc.
  - Foreign words: words that are borrowed from other languages, such as "pizza", "sushi", "karaoke", etc.
  - Abbreviations: words that are shortened by using the initial letters, such as "NLP", "USA", "UN", etc.
  - Proper nouns: words that are used to name specific entities, such as "John", "London", "Microsoft", etc.
  - Collocations: words that are frequently used together, such as "red wine", "heavy rain", "make up", etc.
- Another issue that PoS tagging faces is the lack of standardization in the PoS tagsets. Different PoS taggers may use different sets of tags to label the words, depending on the level of granularity and the linguistic theory they adopt. For example, some PoS taggers may distinguish between singular and plural nouns, while others may not. Some PoS taggers may have separate tags for modal verbs, auxiliary verbs, and main verbs, while others may not. Some PoS taggers may have more than 100 tags, while others may have less than 50. This makes it difficult to compare the performance and accuracy of different PoS taggers  .
- A related issue is the lack of annotated data for PoS tagging. Annotated data is data that has been manually labeled with the correct PoS tags by human experts. Annotated data is essential for training and evaluating PoS taggers, especially those that use machine learning or deep learning techniques. However, annotating data is a time-consuming and labor-intensive process, and the availability and quality of annotated data may vary across languages, domains, and genres. Moreover, annotated data may be outdated or inconsistent, as languages evolve and change over time  .
- A final issue that PoS tagging faces is the trade-off between accuracy and efficiency. PoS tagging is often a subtask or a preprocessing step for other NLP tasks, and thus it needs to be fast and reliable. However, achieving high accuracy in PoS tagging may require complex and sophisticated models that use large amounts of data and computational resources. Therefore, PoS taggers need to balance the trade-off between accuracy and efficiency, depending on the requirements and constraints of the application  .

: Part of speech tagging: a systematic review of deep learning and machine learning approaches | Journal of Big Data | Full Text
: Part Of Speech (POS) tagging in NLP | by S