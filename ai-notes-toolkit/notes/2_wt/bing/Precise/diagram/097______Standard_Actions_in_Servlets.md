#### Standard Actions in Servlets

```
+---------------------+
|   JSP Page          |
|  +---------------+  |
|  |  useBean      |  |
|  |  setProperty  |  |
|  |  getProperty  |  |
|  |  include      |  |
|  |  forward      |  |
|  |  param        |  |
|  |  plugin       |  |
|  +---------------+  |
+---------------------+
```

The diagram above shows the standard actions in servlets. These actions are used to perform common tasks in JSP pages. The `useBean` action is used to create or locate a JavaBean. The `setProperty` and `getProperty` actions are used to set and get the properties of a JavaBean. The `include` action is used to include the content of another JSP page or servlet. The `forward` action is used to forward the request to another JSP page or servlet. The `param` action is used to add parameters to a request. The `plugin` action is used to include a plugin, such as an applet or a JavaBean, in a JSP page. These actions provide a way to perform common tasks in a JSP page without having to write Java code.