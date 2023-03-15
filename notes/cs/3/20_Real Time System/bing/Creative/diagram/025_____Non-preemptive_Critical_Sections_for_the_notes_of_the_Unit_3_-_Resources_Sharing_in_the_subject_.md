Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on Non-preemptive Critical Sections for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System.

### Non-preemptive Critical Sections

- Non-preemptive Critical Sections (NPCS) is a protocol for controlling access to shared resources in a real-time system .
- The main idea of NPCS is that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs .
- This means that no job can preempt another job that is using a resource, and thus deadlock can never occur .
- However, NPCS has some disadvantages, such as:
  - It may cause priority inversion, where a high-priority job is blocked by a low-priority job that holds a resource .
  - It may cause blocking, where a job has to wait for a resource that is held by another job .
  - It may cause long response times, where a job has to wait for a long critical section to finish before it can access a resource .
- Therefore, NPCS is only suitable for systems where the critical sections are short and the resource contention is low .