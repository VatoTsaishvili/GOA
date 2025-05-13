// 6) Create an external JavaScript file and link it to an HTML file.

// 7) Move a function from the HTML file’s <script> tag into an external .js file.

    // 2) Create a function that displays an alert saying "Hello, world!".

    function alert(){
        alert('Hello, World')
    }

    // 3) Write a function that takes a name as a parameter and logs "Hello, [name]!" to the console.

    function greet(name) {
        console.log("Hello, " + name + "!");
    }

    greet("Alice");


    // 4) Create a function that adds two numbers and returns the result.

    function calculator(num1, num2){
        console.log(num1 + num2)
    }

    // 5) Write a function that multiplies a number by 10 and returns the value.

    function multiplies(num1){
        console.log(num1 * 10)
    }

// 8) Create multiple functions in an external JS file and call them from different buttons in your HTML page.

    function alert(){
        alert('Hello, World')
    }

// 9) In your external JS file, write a function that changes the text of a paragraph when a button is clicked.

    let p = document.getElementById("p-1")

    p.style.fontSize = "10px"
    p.textContent("VatoTsaishvili")



function concStrings() {
    let str1 = prompt("Enter string1:");
    let str2 = prompt("Enter string2:");
    let result = str1 + str2;
    alert("result: " + result);
}