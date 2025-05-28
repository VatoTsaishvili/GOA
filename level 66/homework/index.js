// 2-6) Number Comparisons
// 1) Check if Two Numbers Are Equal
const num1 = 10;
const num2 = 10;
console.log("Are the two numbers equal? " + (num1 == num2));

// 2) Check if a Number is Greater Than Another Number
const num3 = 15;
const num4 = 10;
console.log("Is the first number greater than the second? " + (num3 > num4));

// 3) Check if a Number is Less Than or Equal to Another Number
const num5 = 5;
const num6 = 10;
console.log("Is the first number less than or equal to the second? " + (num5 <= num6));

// 4) Check if Two Numbers Are Not Equal
const num7 = 20;
const num8 = 25;
console.log("Are the two numbers not equal? " + (num7 != num8));

// 5) Check if a Number is Greater Than or Equal to 100
const num9 = 150;
console.log("Is the number at least 100? " + (num9 >= 100));

// 7-9) Confirm Boxes
// 1) Show a confirm box asking a question
const confirmResult1 = confirm("Do you want to proceed?");
console.log("Confirm result: " + confirmResult1);

// 2) Show a confirm box when a button is clicked
document.getElementById('confirmButton').addEventListener('click', () => {
    const confirmResult2 = confirm("Are you sure you want to continue?");
    console.log("Confirm result: " + confirmResult2);
});

// 3) Display a confirm box on page load
window.onload = () => {
    const confirmResult3 = confirm("Welcome! Do you accept the terms?");
    alert("You accepted: " + confirmResult3);
};

// 10-12) Form Interactions
// Assuming you have a form with inputs named "username", "email", and "phone"
document.getElementById('myForm').addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent form submission
    const username = event.target.username.value;
    console.log("Username: " + username);
});

// Clear the value of the input with name="email"
document.getElementById('clearEmailButton').addEventListener('click', () => {
    document.querySelector('input[name="email"]').value = '';
});

// Alert the value of the input with name="phone"
document.getElementById('alertPhoneButton').addEventListener('click', () => {
    const phoneValue = document.querySelector('input[name="phone"]').value;
    alert("Phone number: " + phoneValue);
});
