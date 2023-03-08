 Here is the content in markdown format:

## Unit 5 - Creating cursor

- A cursor is a pointer to a specific location in a database table. It essentially marks a position which can be used to fetch the next row from the table.
- Cursors are used to process individual rows returned by a database query, especially when there are a large number of rows.
- Declaring a cursor:

```sql
DECLARE cursor_name CURSOR FOR select_statement;
```

- Opening a cursor:

```sql
OPEN cursor_name;
```

- Fetching rows from a cursor:

```sql
FETCH NEXT FROM cursor_name INTO variable_list;
```

- Closing a cursor:

```sql
CLOSE cursor_name;
```

- Advantages:
  - Reduce memory usage when fetching a large number of rows.
  - Allow to process rows one at a time, can perform some action in between the fetches.
- Disadvantages:
  - Execution plans may not be optimal as the database does not know the final purpose of the cursor.
  - Risk of cursors remaining open if not closed properly leading to performance issues.

### TCP Congestion control in transport layer

- TCP uses a congestion control mechanism to avoid congestion collapse. It controls the transmission rate of data to match the bandwidth available in the network.
- TCP monitors packet loss in the network to detect congestion. When there is no congestion and no loss, TCP aggressively increases the transmission rate. When losses occur, TCP interprets it as congestion and decreases the transmission rate.
- The primary algorithms used by TCP for congestion control are:
 - Slow start: The transmission rate is increased exponentially until congestion is detected.
 - Congestion avoidance: The transmission rate is increased linearly upon successful delivery to probe the network capacity while avoiding large losses.
 - Fast retransmit: Upon detection of losses, transmission rate is decreased and lost segments are retransmitted.
- Advantages: Prevents congestion in the Internet and ensures fair bandwidth utilization among flows.
- Disadvantages: Non-responsive to real-time applications and does not distinguish between losses due to corruption or congestion.