
// 2: Check if a Number is Positive or Negative
function checkNumber() {
    let number = prompt("Please enter a number:");
    number = Number(number); // Convert input to a number
    let resultMessage;

    if (number > 0) {
        resultMessage = "The number is positive.";
    } else if (number < 0) {
        resultMessage = "The number is negative.";
    } else {
        resultMessage = "The number is zero.";
    }

    document.getElementById("numberResult").innerText = resultMessage;
}

// 3: Check User’s Age for Voting Eligibility
function checkVotingEligibility() {
    let age = prompt("Please enter your age:");
    age = Number(age); // Convert input to a number
    let resultMessage;

    if (age >= 18) {
        resultMessage = "You can vote!";
    } else {
        resultMessage = "You are not eligible to vote.";
    }

    document.getElementById("votingResult").innerText = resultMessage;
}

// 4: Compare Two Numbers
function compareNumbers() {
    let num1 = prompt("Enter the first number:");
    let num2 = prompt("Enter the second number:");
    num1 = Number(num1); // Convert input to a number
    num2 = Number(num2); // Convert input to a number
    let resultMessage;

    if (num1 > num2) {
        resultMessage = "The first number is larger.";
    } else if (num1 < num2) {
        resultMessage = "The second number is larger.";
    } else {
        resultMessage = "Both numbers are equal.";
    }

    document.getElementById("comparisonResult").innerText = resultMessage;
}

