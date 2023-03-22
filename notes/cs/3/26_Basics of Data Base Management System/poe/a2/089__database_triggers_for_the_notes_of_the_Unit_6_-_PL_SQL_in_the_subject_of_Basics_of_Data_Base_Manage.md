 Here is the formal content in Markdown format without any external links or emojis:

### Database Triggers for Unit 6 - PL/SQL Notes

1. A database trigger is a PL/SQL block that is executed automatically whenever a specific event occurs.
2. Triggers are used to enforce business rules, derive column values, and restrict DML operations.
3. Triggers can be defined on a table or view to execute a block of code automatically when an event (e.g. INSERT, UPDATE, DELETE) occurs.
4. Syntax:

CREATE [ OR REPLACE ] TRIGGER trigger_name

{ BEFORE | AFTER }

{ INSERT | UPDATE | DELETE } ON table_name

[ FOR EACH ROW ]

BEGIN

-- trigger_body

END;

5. Types of Triggers:
- Before Triggers: Fire before the triggering DML statement is executed.
- After Triggers: Fire after the triggering DML statement is executed.
- Row Level Triggers: Fire once for every row affected by the triggering DML statement.
- Statement Level Triggers: Fire only once for the triggering DML statement.

6. Examples of common uses of triggers:
- Enforcing data integrity constraints (foreign keys, check constraints)
- Generating derived column values automatically
- Auditing data changes by logging information to another table
- Preventing invalid transactions (e.g. no account balance can go below zero)

7. Advantages of Triggers:
- Enforcement of business rules and complex security authorizations
- Automation of tasks
- Reduced amount of application code
- Increased data integrity

8. Disadvantages of Triggers:
- May impact performance if misused
- May introduce complex side effects that are hard to debug
- May break if not properly maintained when the underlying tables change
- Vendor differences and standards compliance issues