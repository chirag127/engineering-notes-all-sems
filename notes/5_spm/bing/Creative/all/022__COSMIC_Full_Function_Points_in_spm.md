### COSMIC Full Function Points in spm

- COSMIC stands for Common Software Measurement International Consortium, which is an organization that developed a standard method for measuring the functional size of software.
- Functional size is a measure of the amount of functionality that a software system provides to its users, based on the user requirements.
- COSMIC function points (CFPs) are the unit of functional size measurement in the COSMIC method. One CFP represents one unit of data movement across a boundary between the software and its functional users.
- Functional users are the senders or recipients of data to or from the software. They can be human users, other software systems, or hardware devices.
- The COSMIC method is applicable to any type of software, including business, real-time, and infrastructure software, and at any level of decomposition, such as a whole system, a component, or a user story.
- The COSMIC method is based on two main principles: the software context model and the generic software model.
- The software context model defines the scope and boundaries of the software to be measured, and identifies the functional users and the data groups that are exchanged with them.
- The generic software model defines the four types of data movements that can occur in any software: entry, exit, read, and write.
- An entry is a data movement from a functional user into the software that triggers a unique behavior of the software.
- An exit is a data movement from the software to a functional user that is the result of a unique behavior of the software.
- A read is a data movement from a persistent storage device to the software that is used by a unique behavior of the software.
- A write is a data movement from the software to a persistent storage device that is the result of a unique behavior of the software.
- The COSMIC method measures the functional size of software by counting the number of CFPs for each type of data movement, and summing them up.
- The COSMIC method also provides guidelines for identifying and measuring functional processes, sub-processes, data attributes, and data groups, which are the elements that make up the data movements.
- The COSMIC method can be used for various purposes, such as estimating development effort, project duration, quality, test effort, scope creep, replacement cost, maintenance cost, and defect removal rates.
- The COSMIC method is an ISO standard (ISO/IEC 19761:2011) and has been validated by several empirical studies .
- A possible mnemonic to remember the four types of data movements in the COSMIC method is EERW, which sounds like "earwax" and can be associated with the idea of data flowing in and out of the software.
- A possible learning trick to apply the COSMIC method is to use a table or a diagram to visualize the software context model and the data movements, and to label them with the corresponding CFPs. For example:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Human User     |       |  Software       |       |  Database       |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |  ^                      |  ^                      |  ^
       |  |                      |  |                      |  |
       |  |                      |  |                      |  |
       |  |                      |  |                      |  |
       |  |                      |  |                      |  |
       |  |                      |  |                      |  |
       |  |                      |  |                      |  |
       |  |                      |  |                      |  |
       |  |                      |  |                      |  |
       |  |                      |  |                      |  |
       |  |                      |  |                      |  |
       |  |                      |  |                      |  |
       |  |                      |  |                      |  |
       |  | 1 CFP (Entry)        |  | 1 CFP (Exit)         |  |
       |  +---------------------->  +---------------------->  |
       |                         |                         |  |
       |                         |                         |  |
       |                         |                         |  |
       |