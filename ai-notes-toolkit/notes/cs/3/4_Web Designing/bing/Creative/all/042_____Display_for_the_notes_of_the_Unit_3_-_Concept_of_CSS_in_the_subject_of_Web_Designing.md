# Display for the notes of the Unit 3 - Concept of CSS in the subject of Web Designing

- CSS stands for **Cascading Style Sheets** and is used to **style and layout web pages** .
- CSS is a **rule-based language** that allows you to define the **presentation** of a document written in HTML or XML.
- CSS can alter the **font, color, size, and spacing** of your content, split it into **multiple columns**, or add **animations and other decorative features**.
- CSS can also control how your web page is **rendered** on different **media**, such as screen, print, speech, or other devices.
- CSS consists of two main components: **selectors** and **declarations**.
  - Selectors are used to **specify** which elements or groups of elements on your web page should be styled.
  - Declarations are used to **define** the styles that should be applied to the selected elements.
  - Declarations consist of two parts: **properties** and **values**.
    - Properties are the **aspects** of the elements that you want to change, such as color, font, width, etc.
    - Values are the **settings** that you want to assign to the properties, such as red, Arial, 50%, etc.
  - A selector and a declaration are combined to form a **rule**.
  - A rule is enclosed in **curly braces** and ends with a **semicolon**.
  - For example, the following rule sets the color of all paragraphs to blue:

    ```css
    p {
      color: blue;
    }
    ```

- CSS can be **embedded** in an HTML document using the `<style>` element, **linked** to an external file using the `<link>` element, or **imported** from another file using the `@import` rule.
- CSS follows the principle of **cascading**, which means that the **order** and **specificity** of the rules determine which styles are applied to the elements.
  - The order of the rules is based on the **source** and the **position** of the CSS.
    - The styles that are defined **later** in the source or position override the ones that are defined **earlier**.
    - The styles that are defined in the **external** or **imported** files have lower priority than the ones that are defined in the **embedded** or **inline** styles.
  - The specificity of the rules is based on the **type** and **number** of the selectors.
    - The more **specific** the selector is, the higher priority it has over the less specific ones.
    - The specificity of the selector is calculated by counting the **elements**, **classes**, **attributes**, **identifiers**, and **pseudo-classes** that it contains.
    - For example, the selector `#main p.red` has a higher specificity than the selector `p` because it contains an identifier (`#main`) and a class (`.red`).