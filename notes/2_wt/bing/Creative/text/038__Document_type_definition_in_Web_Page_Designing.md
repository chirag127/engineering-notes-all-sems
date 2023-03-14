### Document type definition in Web Page Designing

- A document type definition (DTD) is a set of rules that defines the structure and the legal elements and attributes of an XML document.
- A DTD can be declared inside the XML file using the <!DOCTYPE> definition, or in an external file that is referenced by the XML file.
- A DTD helps independent groups of people to agree on a standard DTD for interchanging data, and allows an application to verify that XML data is valid.
- A DTD is not an element or tag, but an instruction that tells the web browser about the markup language in which the current page is written.
- In HTML, the DOCTYPE declaration refers to the version or standard of HTML or any other markup language that is being used in the document.
- The DOCTYPE declaration ensures that the web page is parsed the same way by different web browsers, and prevents the browser from switching into quirks mode.
- The DOCTYPE declaration appears at the top of a web page before all other elements.
- The syntax of the DOCTYPE declaration varies depending on the HTML version, but the general format is:

```html
<!DOCTYPE html-version>
```

- For example, the DOCTYPE declaration for HTML5 is:

```html
<!DOCTYPE html>
```

- The DOCTYPE declaration for HTML 4.01 Strict is:

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
```

- The DOCTYPE declaration for XHTML 1.0 Transitional is:

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

- The DOCTYPE declaration is case-insensitive, but it is recommended to use uppercase for consistency and readability.