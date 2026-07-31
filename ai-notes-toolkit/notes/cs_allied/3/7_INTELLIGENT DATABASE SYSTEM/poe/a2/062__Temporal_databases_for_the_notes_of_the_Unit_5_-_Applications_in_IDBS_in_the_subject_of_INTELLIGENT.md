 Here is the content in markdown format without any emojis or external links as requested:

### Temporal databases for the notes of the Unit 5 - Applications in IDBS in the subject of INTELLIGENT DATABASE SYSTEM

1. A temporal database manages time-varying data. It keeps track of valid time, transaction time, and user-defined time.
- Valid time: The time when a fact was true in the real world. e.g. John was an employee of company X from 1 Jan 2019 to 31 Dec 2020.
- Transaction time: The time when a fact was inserted, updated or deleted in the database. e.g. The record for John's employment was entered on 10 Jan 2019.
- User-defined time: The time that is explicitly supplied by the user or application to record the time.

2. Temporal databases allow querying the state of data at a particular point in time or over a time interval. This enables seeing the data as it existed in the past or how it changed over time. Some example queries are:
- Retrieve the employees who were hired after 1 Jan 2018. (Using valid time)
- Show the salary updates made to John's record in 2019. (Using transaction time)
- Get the products that were ordered on 10 Oct 2018. (Using user-defined time)

3. Additional elements in temporal databases:
- Bitemporal: Data is tracked using both valid time and transaction time.
- Point in time: Data as per a particular timestamp.
- Interval: Data over a range of time.
- Previous, current and next versions: Previous, current and next values of an attribute based on time.

4. Challenges in temporal databases:
- Complexity in modeling time-varying data.
- Additional storage and computational costs to maintain the time-varying data.
- Transaction management gets more complex with temporality.
- Query performance can degrade due to the additional time-related processing.

The content is written in a formal tone with points and without any emojis or external links as requested. Please let me know if you would like me to modify or expand the content in any way.