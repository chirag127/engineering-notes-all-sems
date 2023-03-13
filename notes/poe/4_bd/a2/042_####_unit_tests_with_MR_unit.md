 Here is the content in markdown format on the topic #### unit tests with MR unit:

#### Unit tests with MR unit

MR unit is a JavaScript testing framework for unit testing Meteor apps. It has the following advantages:

- Integrates well with Meteor's asynchronous code. MR unit handles the asynchronous nature of Meteor seamlessly.
- Provides useful assertions for testing Meteor data structures like Mongo cursors and Meteor collections.
- Runs tests in an actual Meteor environment, so you can test with real Meteor APIs.
- Fast and simple to set up.

Some tips for writing good unit tests with MR unit:

- Focus on testing one unit of code at a time, like a single function.
- Give tests descriptive names, like "Calculates total price including tax".
- Avoid complex assertions or conditional logic in tests.
- Isolate the unit under test from dependencies using stubs and spies when possible.
- Use mock data to test edge cases.
- Keep tests short and fast.

A basic example of a unit test with MR unit:

```js
Tinytest.add('calculateTotal - with tax', function (test) {
  var calculateTotal = function (price) {
    return price * 1.07;
  };
  test.equal(calculateTotal(10), 107);
});
```

Some useful MR unit assertions for Meteor:

- `instanceOf` - Assert an object is an instance of a given class.
- `isArray` - Assert that a value is an array.
- `isObject` - Assert that a value is an object.
- `isUndefined` - Assert that a value is undefined.
- `notEqual` - Assert that two values are not equal.
- `throws` - Assert that a function throws an exception when called.

Overall, MR unit is a great choice for unit testing Meteor apps. By writing small, focused tests and utilizing the useful Meteor-specific assertions, you can achieve good test coverage and catch bugs early. Unit testing leads to more robust, reliable apps and is worth the investment.