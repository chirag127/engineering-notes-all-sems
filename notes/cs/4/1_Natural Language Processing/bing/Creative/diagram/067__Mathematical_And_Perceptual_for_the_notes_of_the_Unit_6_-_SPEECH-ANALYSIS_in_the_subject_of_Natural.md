### Mathematical And Perceptual for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

Speech perception can be described as a pattern-recognition problem. Given some speech input, the perceiver must determine which message best describes the input. An auditory stimulus is transformed by the auditory receptor system and sets up a neurological code in a pre-perceptual auditory storage.

Each perceptual unit in speech must occur within the temporal span of pre-perceptual auditory storage and must be recognized before the following one occurs for accurate speech processing to take place. Therefore, the sequence of perceptual units in speech must be recognized one after the other in a successive and linear fashion.

One possible candidate for the perceptual unit in speech is the syllable. A syllable is a unit of speech that consists of a vowel or a vowel-like sound (the nucleus) and any consonants that precede or follow it (the onset and the coda). Syllables can be classified according to their structure, such as CV (consonant-vowel), CVC (consonant-vowel-consonant), V (vowel), etc.

The following diagram illustrates the basic architecture of a syllable:

```
  onset   nucleus   coda
    |       |        |
    C       V        C
    |       |        |
    /       /        /
   /       /        /
  /       /        /
 /       /        /
/       /        /
bat
```

The following diagram illustrates the basic architecture of a speech perception system that uses syllables as perceptual units:

```
  speech input
      |
      |
      V
  auditory receptor system
      |
      |
      V
  pre-perceptual auditory storage
      |
      |
      V
  syllable segmentation
      |
      |
      V
  syllable recognition
      |
      |
      V
  message output
```