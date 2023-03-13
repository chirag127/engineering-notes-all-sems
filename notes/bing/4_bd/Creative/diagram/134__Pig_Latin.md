Pig Latin is a language game in which words in English are altered by moving the initial consonant or consonant cluster of a word to the end of the word and adding a suffix, usually "ay". For example, "pig" becomes "igpay" and "latin" becomes "atinlay". If a word begins with a vowel, the suffix "way" or "yay" is added. For example, "out" becomes "outway" or "outyay".

The following diagram illustrates the basic architecture of a Pig Latin word:

#### Pig Latin

```
+-----------------+     +-----------------+     +-----------------+
| English word    |     | Pig Latin word  |     | Suffix          |
+-----------------+     +-----------------+     +-----------------+
| consonant(s)    | --> | vowel(s)        | --> | consonant(s)    |
| vowel(s)        | --> | consonant(s)    | --> | "ay"            |
| consonant(s)    | --> | vowel(s)        | --> | consonant(s)    |
+-----------------+     +-----------------+     +-----------------+
| vowel(s)        | --> | vowel(s)        | --> | "way" or "yay"  |
| consonant(s)    | --> | consonant(s)    | --> |                 |
+-----------------+     +-----------------+     +-----------------+
```
