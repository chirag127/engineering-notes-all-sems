### Waterfall Model in SDLC

The waterfall model is a linear, sequential approach to the software development lifecycle (SDLC) that is popular in software engineering and product development. The waterfall model uses a logical progression of SDLC steps for a project, similar to the direction water flows over the edge of a cliff. It sets distinct endpoints or goals for each phase of development. Those endpoints or goals can't be revisited after their completion.

The waterfall model was the first process model to be introduced. It is also referred to as a linear-sequential life cycle model. It is very simple to understand and use. In a waterfall model, each phase must be completed before the next phase can begin and there is no overlapping in the phases.

The waterfall model illustrates the software development process in a linear sequential flow. This means that any phase in the development process begins only if the previous phase is complete. In this waterfall model, the phases do not overlap.

The following illustration is a representation of the different phases of the waterfall model.

```
+-----------------+     +-----------------+     +-----------------+     +-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |     |                 |     |                 |     |                 |
| Requirement     |     | System Design   |     | Implementation  |     | Integration and |     | Deployment of   |     | Maintenance     |
| Gathering and   |     |                 |     |                 |     | Testing         |     | System          |     |                 |
| Analysis        |---->|                 |---->|                 |---->|                 |---->|                 |---->|                 |
|                 |     |                 |     |                 |     |                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+     +-----------------+     +-----------------+     +-----------------+
```

The sequential phases in the waterfall model are:

- Requirement Gathering and Analysis: All possible requirements of the system to be developed are captured in this phase and documented in a requirement specification document.
- System Design: The requirement specifications from the first phase are studied in this phase and the system design is prepared. This system design helps in specifying hardware and system requirements and helps in defining the overall system architecture.
- Implementation: With inputs from the system design, the system is first developed in small programs called units, which are integrated in the next phase. Each unit is developed and tested for its functionality, which is referred to as Unit Testing.
- Integration and Testing: All the units developed in the implementation phase are integrated into a system after testing of each unit. Post integration the entire system is tested for any faults and failures.
- Deployment of System: Once the functional and non-functional testing is done, the product is deployed in the customer environment or released into the market.
- Maintenance: There are some issues which come up in the client environment. To fix those issues, patches are released. Also to enhance the product some better versions are released. Maintenance is done to deliver these changes in the customer environment.

The waterfall model is suitable for projects that have:

- Fixed requirements
- Ample resources
- An established timeline
- A clear and stable vision
- No ambiguity or uncertainty
- Minimal changes or risks

Some of the advantages of the waterfall model are:

- It is easy to understand and implement
- It has a clear structure and well-defined stages
- It facilitates documentation and verification
- It ensures quality and reliability
- It allows for efficient management and control

Some of the disadvantages of the waterfall model are:

- It is rigid and inflexible
- It does not accommodate changes or feedback
- It does not involve the customer or end-user
- It does not support iterative or incremental development
- It can be costly and time-consuming

A possible mnemonic to remember the phases of the waterfall model is:

**R**equirements **S**pecify **I**mplementation **I**ntegration **D**eployment **M**aintenance

or

**R**ealize **S**ystem **I**n **I**ncrements **D**eliver **M**odifications