### Dependency Grammar for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

Dependency grammar is a class of modern grammatical theories that are based on the dependency relation between words, as opposed to the constituency relation of phrase structure grammars. In dependency grammar, every word (or morpheme) in a sentence is either the root or depends on another word via a directed link. The link indicates the grammatical function and the hierarchical structure of the sentence. For example, in the sentence "She likes apples", the word "she" is the subject and depends on the word "likes", which is the root and the main verb. The word "apples" is the object and depends on the word "likes" as well. The dependency relation can be represented by a tree diagram, where the nodes are the words and the branches are the links. The following diagram illustrates the dependency grammar of the sentence "She likes apples":

```
    likes
   /    \
she    apples
```

The dependency grammar can also be represented by a table, where the columns are the words and the rows are the grammatical functions. The table shows which word depends on which word and by what function. The following table illustrates the dependency grammar of the sentence "She likes apples":

| | she | likes | apples |
| --- | --- | --- | --- |
| subject | - | she | - |
| root | - | - | - |
| object | - | - | apples |

Dependency grammar is useful for natural language processing because it can capture the syntactic structure and the semantic relations of a sentence in a simple and compact way. It can also be applied to different languages and different levels of analysis, such as morphology, syntax, and semantics. Dependency grammar is the basis of many dependency frameworks, such as Universal Dependencies, which is a cross-linguistic standard for annotating and parsing natural language texts. Dependency parsing is the task of automatically producing dependency grammar representations for natural language sentences. Dependency parsing is an important component of many natural language processing applications, such as machine translation, information extraction, and sentiment analysis.