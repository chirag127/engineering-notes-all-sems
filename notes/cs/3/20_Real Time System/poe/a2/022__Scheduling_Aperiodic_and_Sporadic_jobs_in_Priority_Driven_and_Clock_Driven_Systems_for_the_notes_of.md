 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

Priority Driven System:
- Aperiodic and sporadic jobs are scheduled based on their priority. Higher priority jobs preempt lower priority jobs.
- A job with higher priority will always get the CPU before a job with lower priority.
- Priority can be assigned based on job criticality. More critical jobs are given higher priority.
- Issue: Priority inversion - A high priority job can be blocked by a low priority job leading to deadline miss. Priority inheritance protocol can be used to resolve this.

Clock Driven System:
- Jobs are scheduled based on their deadlines. Shorter deadline jobs get scheduled first.
- The scheduling is done based on the clock interrupt. The scheduler runs at every clock tick and schedules the jobs based on their deadlines.
- Issue: Jitter can affect the deadlines. The scheduler has to account for the worst case jitter to ensure all deadlines are met.
- Clock driven systems are simpler to implement but can suffer from load fluctuations and schedulability issues.

In conclusion, both priority driven and clock driven systems have their pros and cons. The selection of a scheduling system depends on the requirements and characteristics of the real time system and the jobs in the system. An optimal balance of the two approaches can also be used based on the system needs.

How's this? I have written the content in points in a formal tone without any emojis or external links as you requested. Please let me know if you would like me to modify or expand the answer.