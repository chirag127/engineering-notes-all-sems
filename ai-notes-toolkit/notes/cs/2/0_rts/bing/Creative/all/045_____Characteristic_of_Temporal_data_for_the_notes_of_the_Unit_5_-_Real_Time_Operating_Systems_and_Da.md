# Characteristic of Temporal Data

- Temporal data is the data that is **valid only for a prescribed time** and becomes **invalid or obsolete** after a certain period of time .
- Temporal data can represent **time in some form**, such as dates, timestamps, intervals, durations, or periods, and allow other data to be placed in a **chronological sequence** or to be analyzed **chronologically**.
- Temporal data can have different **temporal aspects**, such as valid time, transaction time, or decision time, depending on the **application domain** and the **purpose of the data**.
- Valid time is the time period during or event time at which a fact is **true in the real world**. For example, the date of birth of a person is a valid time attribute.
- Transaction time is the time period during or event time at which a fact is **stored in the database**. For example, the date of entry of a record in a database is a transaction time attribute.
- Decision time is the time period during or event time at which a fact is **decided or acted upon**. For example, the date of approval of a loan application is a decision time attribute.
- Temporal data can be **uni-temporal**, **bi-temporal**, or **tri-temporal**, depending on the number of temporal aspects involved.
- Uni-temporal data has **one temporal aspect**, either valid time, transaction time, or decision time. For example, a weather report that records the temperature at a given location and time is uni-temporal data with valid time aspect.
- Bi-temporal data has **two temporal aspects**, either valid time and transaction time, or valid time and decision time. For example, a customer account that records the balance and the date of change, as well as the date of entry in the database, is bi-temporal data with valid time and transaction time aspects.
- Tri-temporal data has **three temporal aspects**, valid time, transaction time, and decision time. For example, a legal document that records the facts, the dates of validity, the dates of storage, and the dates of decision, is tri-temporal data with all three temporal aspects.