#### Job scheduling in MapReduce

Here is an example of a simple job scheduling algorithm in MapReduce:

```python
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRJobScheduling(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        # extract relevant data from input
        job_id, priority, duration = line.split()
        priority = int(priority)
        duration = int(duration)
        yield priority, (job_id, duration)

    def reducer(self, key, values):
        # sort jobs by priority
        sorted_jobs = sorted(values, key=lambda x: x[0])
        current_time = 0
        for job in sorted_jobs:
            job_id, duration = job
            start_time = current_time
            end_time = current_time + duration
            current_time = end_time
            yield job_id, (start_time, end_time)

if __name__ == '__main__':
    MRJobScheduling.run()
```

This code defines a MapReduce job that takes as input a list of jobs, each with an ID, priority, and duration. The mapper extracts the relevant data from the input and yields the priority as the key and the job ID and duration as the value. The reducer then sorts the jobs by priority and schedules them one by one, keeping track of the current time and calculating the start and end times for each job. The output is the job ID and the start and end times for each job.
