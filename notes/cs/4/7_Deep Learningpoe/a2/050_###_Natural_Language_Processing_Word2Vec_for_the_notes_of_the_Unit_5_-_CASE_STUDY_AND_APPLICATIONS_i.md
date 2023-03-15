 Here is the content in markdown format for the topic ### Natural Language Processing Word2Vec for the notes of the Unit 5 - CASE STUDY AND APPLICATIONS in the subject of Deep Learning:

### Natural Language Processing Word2Vec

Word2Vec is a group of related models that are used to produce word embeddings. These embeddings can then be used as features for many NLP tasks like sentiment analysis, named entity recognition, parsing, etc.

Some key points about Word2Vec:

- It converts words to vectors of real numbers. Words with similar meanings will have vectors that are closer together.
- It uses a shallow neural network to train the word embeddings on a large corpus of text.
- It comes in two flavours: Continuous Bag-of-Words (CBOW) and Skip-Gram.
- CBOW predicts the current word from its context words. Skip-Gram predicts context words from the current word.
- The embeddings can capture semantic and syntactic meanings of words.
- They are efficient to train and have low memory footprint.
- It has many applications like sentiment analysis, machine translation, etc.

Advantages:

- Simple and efficient to train.
- Can capture semantic and syntactic meanings.
- Manifold uses in NLP applications.

Disadvantages:

- Requires large corpus of text to train on.
- Not good at capturing polysemy (words with multiple meanings) as it maps words to single vectors.
- Does not explicitly model word order / syntax.

Some examples and applications of Word2Vec:

- Predict sentiment of reviews and tweets.
- Translate between languages.
- Recommend similar products or words.
- Summarization.
- Question Answering.

Word2Vec has become a foundational technique in NLP and has inspired many later models. It is a great introduction to the power of neural networks and word embeddings.