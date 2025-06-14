// 1: Print Numbers from 1 to 10 using a for loop
function printNumbers1To10() {
    let result = "";
    for (let i = 1; i <= 10; i++) {
        result += i + "\n";
    }
    document.getElementById("numbers1To10Result").innerText = result;
}

// 2: Print Even Numbers from 2 to 20 using a while loop
function printEvenNumbers() {
    let result = "";
    let i = 2;
    while (i <= 20) {
        result += i + "\n";
        i += 2;
    }
    document.getElementById("evenNumbersResult").innerText = result;
}

// 3: Print Numbers from 10 Down to 1 using a for loop
function printNumbers10To1() {
    let result = "";
    for (let i = 10; i >= 1; i--) {
        result += i + "\n";
    }
    document.getElementById("numbers10To1Result").innerText = result;
}

// 4: Print the First 5 Multiples of 3 using a while loop
function printMultiplesOf3() {
    let result = "";
    let count = 1;
    while (count <= 5) {
        result += (count * 3) + "\n";
        count++;
    }
    document.getElementById("multiplesOf3Result").innerText = result;
}

// 5: Print Each Character of a String using a for loop
function printStringCharacters() {
    const str = "Example";
    let result = "";
    for (let i = 0; i < str.length; i++) {
        result += str[i] + "\n";
    }
    document.getElementById("stringCharactersResult").innerText = result;
}

// 6: Change Text Content of a Paragraph when a button is clicked
function changeText() {
    const p = document.getElementById("textParagraph");
    p.textContent = "The text has been changed!";
}

// 7: Change Background Color of a Div when a button is clicked
function changeBackgroundColor() {
    const div = document.getElementById("colorDiv");
    div.style.backgroundColor = "#10b981"; // Emerald green
}

// 8: Change Font Size of a Heading when a button is clicked
function changeFontSize() {
    const heading = document.getElementById("fontSizeHeading");
    heading.style.fontSize = "3rem"; // Increase font size
}

// 9: Hide a Div by setting its display style to none when a button is clicked
function hideDiv() {
    const div = document.getElementById("hideDiv");
    div.style.display = "none";
}

// 10: Show an Alert with a Custom Message when a button is clicked
function showAlert() {
    alert("This is a custom alert message!");
}