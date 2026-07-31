# Concepts in Backward and Forward Recovery

- Backward recovery and forward recovery are two techniques for restoring the system to a consistent state after a failure in a distributed system.
- Backward recovery involves rolling back the system to a previous error-free state by using checkpoints and logs. Forward recovery involves correcting the errors in the current state and continuing the execution.
- The main difference between backward and forward recovery is that backward recovery discards the work done after the error, while forward recovery preserves the work done before and after the error.
- Backward recovery is more general and independent of the nature of faults, but it may incur more overhead and waste of resources. Forward recovery is more efficient and avoids unnecessary rollbacks, but it requires accurate assessment and removal of errors.
- Some examples of backward recovery protocols are checkpointing, message logging, and rollback-dependency trackback. Some examples of forward recovery techniques are error masking, retry, and compensation.