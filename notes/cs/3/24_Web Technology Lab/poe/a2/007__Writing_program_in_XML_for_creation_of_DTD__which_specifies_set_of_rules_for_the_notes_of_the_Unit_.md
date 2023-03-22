 Here is the content in markdown format without any emojis or external links:

### Writing program in XML for creation of DTD, which specifies set of rules for the notes of the Unit 3 - Design dynamic web pages using Javascript and XML in the subject of Web Technology Lab.

1. Start with the declaration of XML.
<?xml version="1.0"?>

2. Then define the root element. Here it will be 'notes'.
<notes>

3. Now define the elements inside root element. Here the elements will be title, topic, point1, point2, etc. for different points.
<title>Writing program in XML for creation of DTD</title>
<topic>Which specifies set of rules for the notes of the Unit 3</topic>
<point1>Javascript</point1>
<point2>XML</point2>

4. Close the root element.
</notes>

5. Then define the DTD which will validate the XML document.
<!DOCTYPE notes [
<!ELEMENT notes (title, topic, point1, point2)>
<!ELEMENT title  (#PCDATA)>
<!ELEMENT topic  (#PCDATA)>
<!ELEMENT point1 (#PCDATA)>
<!ELEMENT point2 (#PCDATA)>
]>

6. Save the XML file with .xml extension.

The XML file will contain the structure of notes with title, topic and points specified inside the root element 'notes'. The DTD defines the set of rules for the elements and their content in the XML file.