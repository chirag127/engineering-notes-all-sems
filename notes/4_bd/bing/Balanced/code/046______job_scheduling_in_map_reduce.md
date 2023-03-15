Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write code for job scheduling in map reduce. Here is a possible solution in Python:

#### Job scheduling in map reduce

```python
# Import the mrjob library
from mrjob.job import MRJob

# Define a class that inherits from MRJob
class JobScheduler(MRJob):

    # Define a mapper function that takes a line of input and yields a key-value pair
    def mapper(self, _, line):
        # Split the line by whitespace
        fields = line.split()
        # Extract the job ID, start time, and duration
        job_id = fields[0]
        start_time = int(fields[1])
        duration = int(fields[2])
        # Yield the start time as the key and the job ID and duration as the value
        yield start_time, (job_id, duration)

    # Define a reducer function that takes a key and a list of values and yields the scheduled jobs
    def reducer(self, start_time, values):
        # Sort the values by duration in ascending order
        values = sorted(values, key=lambda x: x[1])
        # Initialize the current time as the start time
        current_time = start_time
        # Loop through the values
        for value in values:
            # Extract the job ID and duration
            job_id, duration = value
            # Yield the job ID, the current time, and the duration
            yield job_id, (current_time, duration)
            # Update the current time by adding the duration
            current_time += duration

# Run the job
if __name__ == '__main__':
    JobScheduler.run()
```