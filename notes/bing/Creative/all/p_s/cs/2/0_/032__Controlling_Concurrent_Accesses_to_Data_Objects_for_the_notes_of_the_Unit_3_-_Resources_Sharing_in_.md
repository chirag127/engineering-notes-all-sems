### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs or transactions in a real-time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, which can cause data inconsistency or violation of temporal constraints.
- To ensure data integrity and timeliness, it is common to require that reads and writes be serializable, meaning that the effect of concurrent accesses is equivalent to some sequential execution of the accesses.
- Concurrency control is the technique that manages concurrent accesses to data objects by enforcing some rules or protocols that prevent or resolve conflicts among accesses.
- Concurrency control can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control prevents conflicts from occurring by locking data objects before accessing them. A lock is a mechanism that grants exclusive or shared access to a data object to a job or transaction. A lock can be acquired or released by a job or transaction, and can be blocked or suspended by a lock manager if the requested lock is not available.
  - Optimistic concurrency control allows conflicts to occur and detects them at the end of the access. A conflict occurs when two or more jobs or transactions access the same data object and at least one of them modifies it. A conflict can be resolved by aborting or restarting one or more of the conflicting jobs or transactions, or by compensating the effect of the conflict.
- Concurrency control can also be classified into two levels: database level and application level.
  - Database level concurrency control is implemented by a database management system (DBMS) that provides a set of predefined locking protocols or conflict resolution methods. A DBMS can also support different types of data objects, such as relational tables, object-oriented classes, or temporal data.
  - Application level concurrency control is implemented by an application program that defines its own locking protocols or conflict resolution methods. An application program can also customize the types and properties of data objects, such as priority, deadline, or validity.
- Some examples of concurrency control protocols are:
  - Two-phase locking (2PL): a database level pessimistic protocol that requires a job or transaction to acquire all the locks it needs before releasing any lock. 2PL ensures serializability, but may cause deadlock or priority inversion.
  - Timestamp ordering (TO): a database level optimistic protocol that assigns a timestamp to each job or transaction and orders the accesses according to the timestamps. TO ensures serializability, but may cause abortion or restart of jobs or transactions.
  - Priority ceiling protocol (PCP): an application level pessimistic protocol that assigns a priority ceiling to each data object and blocks a job or transaction from acquiring a lock if its priority is lower than the system ceiling, which is the maximum of the priority ceilings of all the locked data objects. PCP ensures serializability and prevents deadlock and priority inversion.
  - Affected set priority ceiling protocol (ASPCP): an application level pessimistic protocol that extends PCP to support object-oriented systems. ASPCP assigns a priority ceiling to each method of a class and blocks a job or transaction from invoking a method if its priority is lower than the system ceiling, which is the maximum of the priority ceilings of all the invoked methods. ASPCP ensures serializability and prevents deadlock and priority inversion.

Mnemonics are techniques that can help you remember information better by linking it to something you already know or something that is easy to recall. There are different types of mnemonics, such as:

- **Acronyms**: Using the first letter of each word in a phrase or list to form a new word. For example, HOMES is an acronym for the Great Lakes: Huron, Ontario, Michigan, Erie, and Superior.
- **Acrostics**: Using the first letter of each word in a phrase or list to form a sentence. For example, Every Good Boy Does Fine is an acrostic for the notes on the lines of the treble clef: E, G, B, D, F.
- **Rhymes**: Using words that sound alike to help you remember something. For example, In 1492, Columbus sailed the ocean blue is a rhyme that helps you remember the year of his voyage.
- **Chunking**: Breaking down a large piece of information into smaller, manageable units. For example, you can chunk a phone number into three parts: area code, prefix, and suffix.
- **Imagery**: Using mental pictures or associations to help you remember something. For example, you can imagine a giant sun to remember that the word "son" is spelled with an o, not a u.
- **Peg words**: Using words that rhyme with numbers to help you remember a list of items in order. For example, you can use one-bun, two-shoe, three-tree, etc. to remember a list of words that you associate with each peg word.
- **Method of loci**: Using a familiar place or route to help you remember a list of items in order. For example, you can use your home or your way to school to remember a list of words that you place in each location mentally.
- **Story**: Using a narrative or a sequence of events to help you remember a list of items or facts. For example, you can make up a story that involves the presidents of the United States in chronological order to remember their names and terms.
- **Spelling mnemonics**: Using words or phrases to help you remember how to spell a word. For example, you can use Big Elephants Can Always Understand Small Elephants to remember how to spell "because".

To use mnemonics effectively, you should follow these guidelines:

- Choose the appropriate mnemonic for your situation. For example, if your goal is to learn how to spell a word, you may want to use the spelling mnemonic technique.
- Practice the technique. You may want to practice your mnemonic several times to help you remember it.
- Repeat the mnemonic to others. You may find it helpful to share your mnemonic with someone else or teach it to someone else. This can reinforce your memory and help you recall it better.

Mnemonics are not easy to remember if they are too long, complex, or unrelated to the information you want to learn. You should try to make your mnemonics simple, catchy, and meaningful. You can also use humor, creativity, or personalization to make your mnemonics more memorable. For example, you can use a joke, a song, or a personal experience to create your mnemonic.