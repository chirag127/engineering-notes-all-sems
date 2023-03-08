 Here is the content in markdown format for the given topic:

### Write programs using Java script for Web Page to display browsers information

1. JavaScript can be used to detect the browser information of the user such as:
- Browser name and version
- Operating system
- Screen resolution
- Plugins installed

2. This can be done using JavaScript objects and methods like:
- navigator object - to get browser name, version, OS, etc.
- screen object - to get screen resolution
- Plugins array - to check for installed plugins

3. For example, to get browser name and version:
navigator.appName + ' ' + navigator.appVersion

4. To get OS:
navigator.platform

5. To get screen resolution:
screen.width + 'x' + screen.height

6. Advantages:
- Tailor web pages according to user browser for optimal viewing
- Provide different code paths for different browsers if needed
- Check for plugin support and provide alternate content if not supported

7. Disadvantages:
- Additional overhead of browser detection scripts
- Might not detect newer or less popular browsers accurately
- Might affect page load time

8. Examples and codes can be included to demonstrate how to display browser information on a web page using JavaScript.

9. This can be useful to learn and use in projects/assignments related to customizing web pages based on user browser. It can also be included in exams to test understanding of JavaScript and its usage.