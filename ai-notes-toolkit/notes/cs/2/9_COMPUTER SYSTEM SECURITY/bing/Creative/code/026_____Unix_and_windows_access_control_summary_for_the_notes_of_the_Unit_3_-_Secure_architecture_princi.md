### Unix and windows access control summary

- Access control is the mechanism that determines who can access what resources in a system.
- Unix and Windows have different access control models and mechanisms.
- Unix uses access control lists (ACLs) on each file and directory. An ACL consists of three sets of mode bits that specify the permissions for the owner, the group, and the others (world) respectively. The permissions are read, write, and execute.
- Windows uses security descriptors on each object (file, directory, registry key, etc.). A security descriptor consists of an owner, a group, a discretionary access control list (DACL), and a system access control list (SACL). A DACL contains access control entries (ACEs) that grant or deny permissions to security principals (users and groups). A SACL contains audit entries that specify what actions should be logged.
- Unix and Windows also differ in how they handle inheritance of permissions. In Unix, permissions are not inherited by default, but can be set with the sticky bit or the setgid bit. In Windows, permissions are inherited by default, but can be blocked or modified with inheritance flags and propagation flags.