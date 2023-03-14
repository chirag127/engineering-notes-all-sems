## Unit 7 - SPEECH MODELING

Speech modeling is the process of creating mathematical representations of speech signals and speech units, such as words, syllables, phonemes, etc. Speech modeling is essential for speech recognition, speech synthesis, speech analysis, and speech enhancement applications.

One possible diagram for speech modeling is based on the speech chain model, which describes the stages of spoken communication from the speaker's intention to the listener's understanding. The diagram below shows the main components of the speech chain model and how they relate to speech modeling.

```
+-----------------+       +-----------------+       +-----------------+
| Speaker's       |       | Speech          |       | Listener's      |
| Intention       |       | Production      |       | Perception      |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| Grammatical     |       | Articulation    |       | Hearing         |
| Code            |       |                 |       |                 |
|                 |       |                 |       |                 |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | Syntax      | |       | | Vocal Tract | |       | | Ear         | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | Semantics   | |       | | Lungs       | |       | | Auditory    | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
| | Pragmatics  | |       | | Larynx      | |       | | Nerve       | |
| +-------------+ |       | +-------------+ |       | +-------------+ |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        +------------------------>|                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         +------------------------>|
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        +-------------------------------------------------->|
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        +------------------------>|                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         +------------------------>|
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        +-------------------------------------------------->|
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        +------------------------>|                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         +------------------------>|
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        +-------------------------------------------------->|
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        +------------------------>|                         |
        |                         |                         |
        |