 Here are the notes on Procedures in SQL/PL SQL for the Unit 2 - Relational data Model and Language in Database Management System:

### Procedures in SQL/PL SQL

1. A procedure is a set of SQL and PL/SQL statements that are grouped together as a unit to solve a specific task.
2. Procedures help reduce redundancy and improve modularity.
3. The keyword CREATE is used to create a procedure. The structure is:
CREATE [OR REPLACE] PROCEDURE procedure_name
[ (parameter [, parameter] ...) ]
IS / AS
begin
   -- procedure body
END;

4. IN parameters: Values are passed into the procedure. The procedure cannot modify them.
5. OUT parameters: The procedure can return values via such parameters.
6. IN OUT parameters: Value can be passed in and modified in the procedure.
7. A procedure is executed via the EXECUTE statement:
EXECUTE procedure_name;

8. Anonymous blocks: Procedures without a name. They are executed as a anonymous PL/SQL block.
9. advantages:
- Modular approach
- Code reuse
- Information hiding

10. Use cases:
- Complex validations
- Dashboards and reports
- Database triggers
- Batch processes

The notes are written in points and in a formal tone with no emojis or external links as per your instructions. Please let me know if you would like me to modify or expand the notes in any way.