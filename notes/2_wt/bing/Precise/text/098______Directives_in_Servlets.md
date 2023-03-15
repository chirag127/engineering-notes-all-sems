#### Directives in Servlets

Directives are instructions that are processed by the JSP engine when the page is compiled into a servlet. They are used to provide global information about the JSP page to the JSP engine. There are three types of directives in JSP: page, include, and taglib.

1. **Page directive:** The page directive is used to define page-specific attributes such as the scripting language, error page, and buffering requirements. It is specified using the following syntax: `<%@ page attribute="value" %>`. Multiple page directives can be used in a single JSP page.

2. **Include directive:** The include directive is used to include the contents of another file in the JSP page at the time of translation. It is specified using the following syntax: `<%@ include file="filename" %>`. The included file can be a static file or another JSP page.

3. **Taglib directive:** The taglib directive is used to declare a custom tag library that will be used in the JSP page. It is specified using the following syntax: `<%@ taglib uri="uri" prefix="prefix" %>`. The `uri` attribute specifies the location of the tag library descriptor, and the `prefix` attribute specifies the prefix that will be used to reference the custom tags in the JSP page.

These are the three types of directives in JSP that can be used to provide global information about the JSP page to the JSP engine. They are an important part of JSP development and can help to make JSP pages more modular and maintainable.