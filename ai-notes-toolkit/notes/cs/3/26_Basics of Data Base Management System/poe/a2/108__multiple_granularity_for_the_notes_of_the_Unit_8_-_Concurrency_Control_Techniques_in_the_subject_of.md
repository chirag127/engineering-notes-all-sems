 Here are the notes on the topic of Multiple Granularity for Concurrency Control Techniques in Basics of Data Base Management System:

### Multiple Granularity

- Concurrency control can be implemented at various levels of granularity:
 - Row-level: Lock individual rows of a table.
 - Page-level: Lock pages in the buffer pool.
 - Table-level: Lock entire tables.
 - Database-level: Lock the entire database.
- Choosing an appropriate granularity involves trading off concurrency vs. overhead.
 - Finer granularity increases concurrency but increases locking overhead.
 - Coarser granularity reduces overhead but limits concurrency.
- Most commercial database systems implement concurrency control at multiple granularities to achieve both good concurrency and low overhead.
 - Often, row-level or page-level locks are used within a single table, while table-level or database-level locks are used for interactions between tables.

The notes are written in points and in a formal style without any feelings or friendliness as you asked. Only the requested content is included and written myself without any external links. The markdown formatting is used and a header is added. Please let me know if you would like me to modify or expand the notes in any way.