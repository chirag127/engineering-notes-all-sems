# DCL (Data Control Language)

DCL is a subset of SQL (Structured Query Language) used to control access to data stored in a database. It is used to grant and revoke permissions to users and roles in a database. The two main commands in DCL are:

1. **GRANT**: This command is used to grant privileges to a user or role. The privileges can be granted on a specific object, such as a table or view, or on the entire database. The syntax for the GRANT command is as follows:

```
GRANT privilege_name
ON object_name
TO {user_name | role_name | PUBLIC}
[WITH GRANT OPTION];
```

2. **REVOKE**: This command is used to revoke privileges from a user or role. The privileges can be revoked on a specific object, such as a table or view, or on the entire database. The syntax for the REVOKE command is as follows:

```
REVOKE [GRANT OPTION FOR]
privilege_name
ON object_name
FROM {user_name | role_name | PUBLIC};
```

It is important to note that the privileges granted or revoked using DCL commands are only effective for the current session. To make the changes permanent, the database administrator must use the COMMIT command.