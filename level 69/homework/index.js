// 2: Determine if a Number is Even or Odd
function checkEvenOdd() {
    let number = prompt("Please enter a number:");
    number = Number(number); // Convert input to a number
    let resultMessage = (number % 2 === 0) ? "The number is even." : "The number is odd.";
    document.getElementById("evenOddResult").innerText = resultMessage;
}

// 3: Assign a Grade Based on a Score
function assignGrade() {
    let score = prompt("Please enter your score:");
    score = Number(score); // Convert input to a number
    let resultMessage;

    if (score >= 90) {
        resultMessage = "Grade A";
    } else if (score >= 80) {
        resultMessage = "Grade B";
    } else if (score >= 70) {
        resultMessage = "Grade C";
    } else if (score >= 60) {
        resultMessage = "Grade D";
    } else {
        resultMessage = "Fail";
    }

    document.getElementById("gradeResult").innerText = resultMessage;
}

// 4: Determine the Largest Among Three Numbers
function findLargestNumber() {
    let num1 = prompt("Enter the first number:");
    let num2 = prompt("Enter the second number:");
    let num3 = prompt("Enter the third number:");
    num1 = Number(num1);
    num2 = Number(num2);
    num3 = Number(num3);
    let resultMessage;

    if (num1 === num2 && num2 === num3) {
        resultMessage = "All three numbers are equal.";
    } else {
        let largest = Math.max(num1, num2, num3);
        resultMessage = "The largest number is " + largest + ".";
    }

    document.getElementById("largestResult").innerText = resultMessage;
}

// 5: Check if a Character is a Vowel or a Consonant
function checkVowelConsonant() {
    let char = prompt("Please enter a single character:").toLowerCase();
    let resultMessage;

    if ("aeiou".includes(char) && char.length === 1) {
        resultMessage = char + " is a vowel.";
    } else if (char.length === 1) {
        resultMessage = char + " is a consonant.";
    } else {
        resultMessage = "Please enter a valid single character.";
    }

    document.getElementById("vowelConsonantResult").innerText = resultMessage;
}

// 6: Check if a Number is Divisible by 3 and 5
function checkDivisibility() {
    let number = prompt("Please enter a number:");
    number = Number(number); // Convert input to a number
    let resultMessage;

    if (number % 3 === 0 && number % 5 === 0) {
        resultMessage = "The number is divisible by both 3 and 5.";
    } else if (number % 3 === 0) {
        resultMessage = "The number is divisible by 3 only.";
    } else if (number % 5 === 0) {
        resultMessage = "The number is divisible by 5 only.";
    } else {
        resultMessage = "The number is not divisible by either.";
    }

    document.getElementById("divisibilityResult").innerText = resultMessage;
}

// 7: Check if a person is a child, teenager, adult, or senior based on age
function checkAgeCategory() {
    let age = prompt("Please enter your age:");
    age = Number(age); // Convert input to a number
    let resultMessage;

    if (age >= 0 && age <= 12) {
        resultMessage = "Child";
    } else if (age >= 13 && age <= 19) {
        resultMessage = "Teenager";
    } else if (age >= 20 && age <= 59) {
        resultMessage = "Adult";
    } else if (age >= 60) {
        resultMessage = "Senior";
    } else {
        resultMessage = "Invalid age.";
    }

    document.getElementById("ageCategoryResult").innerText = resultMessage;
}

// 8: Print numbers from 1 to 5 using a while loop
function printNumbers1To5() {
    let result = "";
    let i = 1;
    while (i <= 5) {
        result += i + "\n";
        i++;
    }
    document.getElementById("numbers1To5Result").innerText = result;
}

// 9: Print even numbers from 2 to 10 using a while loop
function printEvenNumbers() {
    let result = "";
    let i = 2;
    while (i <= 10) {
        result += i + "\n";
        i += 2; // Increment by 2 to get even numbers
    }
    document.getElementById("evenNumbersResult").innerText = result;
}

// 10: Print numbers from 10 down to 1 using a while loop
function printNumbers10To1() {
    let result = "";
    let i = 10;
    while (i >= 1) {
        result += i + "\n";
        i--;
    }
    document.getElementById("numbers10To1Result").innerText = result;
}

// 11: Print numbers from 1 to 10 using a for loop
function printNumbers1To10() {
    let result = "";
    for (let i = 1; i <= 10; i++) {
        result += i + "\n";
    }
    document.getElementById("numbers1To10Result").innerText = result;
}

// 12: Print the first 5 multiples of 3 using a for loop
function printMultiplesOf3() {
    let result = "";
    for (let i = 1; i <= 5; i++) {
        result += (i * 3) + "\n";
    }
    document.getElementById("multiplesOf3Result").innerText = result;
}

// 13: Print numbers from 10 to 1 in reverse using a for loop
function printNumbers10To1ForLoop() {
    let result = "";
    for (let i = 10; i >= 1; i--) {
        result += i + "\n";
    }
    document.getElementById("numbers10To1ForLoopResult").innerText = result;
}

// 14: Print all even numbers between 1 and 20 using a for loop
function printEvenNumbers1To20() {
    let result = "";
    for (let i = 1; i <= 20; i++) {
        if (i % 2 === 0) {
            result += i + "\n";
        }
    }
    document.getElementById("evenNumbers1To20Result").innerText = result;
}

// 15: Print the sum of numbers from 1 to 5 using a for loop
function printSum1To5() {
    let sum = 0;
    for (let i = 1; i <= 5; i++) {
        sum += i;
    }
    document.getElementById("sumResult").innerText = "The sum of numbers from 1 to 5 is: " + sum;
}
