Pig Latin is a language game or argot in which words in English are altered, usually by adding a fabricated suffix or by moving the onset or initial consonant or consonant cluster of a word to the end of the word and adding a vocalic syllable to create such a suffix. 

The rules used by Pig Latin are as follows:

- If a word begins with a vowel, just add "yay" to the end. For example, "out" is translated into "outyay".
- If it begins with a consonant, then we take all consonants before the first vowel and we put them on the end of the word. For example, "which" is translated into "ichwhay".

#### Pig Latin

The following diagram illustrates the basic architecture of a Pig Latin word:

```
+-----------------+-----------------+-----------------+
| Consonant(s)    | Vowel(s)        | Consonant(s)    |
+-----------------+-----------------+-----------------+
| w               | i               | ch              |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
| Consonant(s)    | Vowel(s)        | Suffix          |
+-----------------+-----------------+-----------------+
|                 | i               | ch + w + ay     |
+-----------------+-----------------+-----------------+
```

The word "which" is split into two parts: the onset (w) and the rime (ich). The onset is moved to the end of the word, and the suffix "ay" is added. The result is "ichwhay".