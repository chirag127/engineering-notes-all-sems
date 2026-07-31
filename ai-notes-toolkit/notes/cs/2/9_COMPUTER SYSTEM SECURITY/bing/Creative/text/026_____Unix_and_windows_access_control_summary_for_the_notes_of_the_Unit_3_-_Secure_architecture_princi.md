### Unix and windows access control summary

- Access control is the mechanism that determines who can access what resources in a system.
- Unix and Windows have different access control models and methods.
- Unix uses access control lists (ACLs) and mode bits to assign permissions to files and directories.
- Windows uses security identifiers (SIDs) and access control entries (ACEs) to assign permissions to files, directories, and other objects.
- Unix ACLs consist of three sets of permissions: owner, group, and others. Each set has three mode bits: read, write, and execute.
- Windows ACEs consist of a principal (user or group), a set of operations (read, write, execute, etc.), and a type (allow or deny).
- Unix permissions are checked by comparing the user ID and group ID of the process with the owner and group of the file or directory.
- Windows permissions are checked by evaluating the SIDs and ACEs of the user and the object.
- Unix permissions are inherited by default from the parent directory, unless the setuid or setgid bit is set.
- Windows permissions can be inherited or explicitly set, and can be overridden by deny ACEs or owner rights.