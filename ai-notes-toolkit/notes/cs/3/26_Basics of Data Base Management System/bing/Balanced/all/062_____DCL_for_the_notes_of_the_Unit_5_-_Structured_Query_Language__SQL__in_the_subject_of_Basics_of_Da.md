# DCL

- Data Control Language (DCL) is a sublanguage of SQL that deals with the commands used to control the access and privileges of users on the database .
- DCL is used for enforcing data security and ensuring that only authorized users can perform certain operations on the database .
- The main DCL commands in SQL are:
  - GRANT: This command is used to grant (give access to) security privileges to specific database users or roles . It can be used to allow users to perform operations such as INSERT, DELETE, SELECT, UPDATE, EXECUTE, ALTER, etc. on the database objects.
  - REVOKE: This command is used to revoke (take away) security privileges from specific database users or roles . It can be used to deny users from performing operations that they were previously granted.
  - DENY: This command is used to explicitly deny security privileges to specific database users or roles. It can be used to override any permissions that are granted or inherited by the users or roles.
- The syntax of the DCL commands is as follows :
  - GRANT privilege(s) ON object TO user(s) [WITH GRANT OPTION];
  - REVOKE [GRANT OPTION FOR] privilege(s) ON object FROM user(s) [CASCADE];
  - DENY privilege(s) ON object TO user(s);
- Some examples of the DCL commands are :
  - GRANT SELECT, UPDATE ON employees TO john, mary;
  - REVOKE UPDATE ON employees FROM john;
  - DENY DELETE ON employees TO mary;