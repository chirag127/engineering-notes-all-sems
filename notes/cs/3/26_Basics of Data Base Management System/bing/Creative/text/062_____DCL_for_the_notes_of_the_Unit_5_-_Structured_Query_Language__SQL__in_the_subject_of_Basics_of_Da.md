### DCL

- Data Control Language (DCL) is a sublanguage of SQL that deals with the commands used to control access to data stored in a database (authorization).
- DCL allows the database owner to grant, revoke, or change the permissions for different users or roles on the database objects, such as tables, views, procedures, etc. .
- DCL is used to enforce data security and prevent unauthorized access or modification of data.
- The main DCL commands in SQL are:
  - **GRANT**: This command is used to grant (give access to) specific privileges to a user or a role on a database object. For example, `GRANT SELECT ON employees TO user1;` grants the privilege to select data from the employees table to user1 .
  - **REVOKE**: This command is used to revoke (take away) specific privileges from a user or a role on a database object. For example, `REVOKE UPDATE ON employees FROM user1;` revokes the privilege to update data in the employees table from user1 .
  - **DENY**: This command is used to deny (block) specific privileges to a user or a role on a database object. For example, `DENY INSERT ON employees TO user1;` denies the privilege to insert data into the employees table to user1.
- DCL commands can also be used to grant or revoke system-level privileges, such as creating or dropping tables, views, procedures, etc. For example, `GRANT CREATE TABLE TO user1;` grants the privilege to create tables to user1.
- DCL commands can also be used with the `WITH GRANT OPTION` clause to allow a user or a role to grant or revoke the same privileges to or from other users or roles. For example, `GRANT SELECT ON employees TO user1 WITH GRANT OPTION;` grants the privilege to select data from the employees table to user1 and also allows user1 to grant the same privilege to other users or roles.