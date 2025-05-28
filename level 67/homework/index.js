// 1. Create an empty object
let emptyObject = {};

// 2. Create an object with your name, age, and city
let person = {
    name: "Your Name",
    age: 25,
    city: "Your City"
};

// 3. Access the value of a property in an object
let name = person.name;
console.log(name); // Output: Your Name

// 4. Add a new property to an existing object
person.country = "Your Country";

// 5. Create a nested object
person.address = {
    street: "123 Main St",
    zipCode: "12345"
};

// 6. Change the value of an existing property
person.age = 30;


// 8. Check if two numbers are both greater than 10
let num1 = 15;
let num2 = 20;
let bothGreaterThanTen = (num1 > 10) && (num2 > 10);
console.log(bothGreaterThanTen); // Output: true

// 9. Check if at least one of two conditions is true
let condition1 = (num1 > 10);
let condition2 = (num2 < 5);
let atLeastOneTrue = condition1 || condition2;
console.log(atLeastOneTrue); // Output: true

// 10. Use the NOT operator to invert a boolean value
let isTrue = true;
let isFalse = !isTrue;
console.log(isFalse); // Output: false

// 11. Combine multiple logical operations in a single expression
let combinedExpression = (num1 > 10) && (num2 > 10) || (num1 < 5);
console.log(combinedExpression); // Output: true


// 12. Convert a number to a string using String()
let num = 123;
let numAsString = String(num);
console.log(numAsString); // Output: "123"
console.log(typeof numAsString); // Output: "string"

// 13. Convert a boolean value to a string using String()
let boolValue = true;
let boolAsString = String(boolValue);
console.log(boolAsString); // Output: "true"
console.log(typeof boolAsString); // Output: "string"

// 14. Convert a string containing a number to a number using Number()
let strNumber = "456";
let convertedNumber = Number(strNumber);
console.log(convertedNumber); // Output: 456
console.log(typeof convertedNumber); // Output: "number"

// 15. Use Number() to convert a boolean to a number
let trueAsNumber = Number(true);
let falseAsNumber = Number(false);
console.log(trueAsNumber); // Output: 1
console.log(falseAsNumber); // Output: 0

// 16. Check what happens when you use Number() on a non-numeric string
let nonNumericString = "Hello";
let result = Number(nonNumericString);
console.log(result); // Output: NaN
console.log(typeof result); // Output: "number"
