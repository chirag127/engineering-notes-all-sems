Hello, I am Sydney, your AI assistant. I can help you with your notes on web page designing. Here is the DTD for the notes of Unit 2:

```xml
<!DOCTYPE notes [
<!ELEMENT notes (unit+)>
<!ELEMENT unit (title, topic+, summary)>
<!ATTLIST unit number CDATA #REQUIRED>
<!ELEMENT title (#PCDATA)>
<!ELEMENT topic (heading, content)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT content (#PCDATA | list | table | image)*>
<!ELEMENT list (item+)>
<!ATTLIST list type (ordered | unordered) #REQUIRED>
<!ELEMENT item (#PCDATA)>
<!ELEMENT table (row+)>
<!ATTLIST table border CDATA #IMPLIED>
<!ELEMENT row (cell+)>
<!ELEMENT cell (#PCDATA)>
<!ATTLIST cell colspan CDATA #IMPLIED>
<!ELEMENT image EMPTY>
<!ATTLIST image src CDATA #REQUIRED
                 alt CDATA #IMPLIED
                 width CDATA #IMPLIED
                 height CDATA #IMPLIED>
<!ELEMENT summary (#PCDATA)>
]>
```