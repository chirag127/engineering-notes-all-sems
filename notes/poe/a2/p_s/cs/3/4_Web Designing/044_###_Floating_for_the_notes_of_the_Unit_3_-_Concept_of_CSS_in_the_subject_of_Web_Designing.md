 Here is the content in markdown format for the given topic:

### Floating

- Floating is a CSS positioning property that allows elements to float horizontally left or right, allowing text and other elements to wrap around it.
- The floated element is taken out of the normal flow of the document and is shifted to the left or right as far as possible.
- The elements after the floating element will behave as if the floating element does not exist and will occupy the space as if the floating element is not there.
- This is used to create entire web layouts and also used to make shapes and images.
- #### Advantages:
-- Allows content to wrap around floating elements.
-- Commonly used for creating sidebars and layouts.
-- Uses less markup as compared to other layout methods.
- #### Disadvantages:
-- Can easily lead to confusion and unintended effects if not used properly.
-- May cause elements to behave unexpectedly if not cleared properly.
-- Does not work well with vertical centering.
- #### Code Example:
<style>
.floating-box {
  float: left;
  width: 150px;
  height: 100px;
  background-color: yellow;
}
</style>
<div class="floating-box"></div>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>

- This will make the div with class floating-box float left, and the paragraph text will wrap around it.

- #### Applications:
-- Creating entire web layouts with header, sidebar and content.
-- Displaying images side by side in a webpage.
-- Creating shape divs and placing them in webpages.
-- And more.