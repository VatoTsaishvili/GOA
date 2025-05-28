const hobby = prompt("1) What is your favorite hobby?");
if (hobby) alert("Your favorite hobby is: " + hobby);

const firstName = prompt("2) Enter your first name:");
const lastName = prompt("3) Enter your last name:");
if (firstName && lastName) {
  alert("Your full name is: " + firstName + " " + lastName);
}

const message = prompt("4) Enter a message:");
if (message) {
  const p = document.querySelector('p');
  if (p) p.textContent = message;
}

const emoji = prompt("5) What is your favorite emoji?");
if (emoji) alert(emoji + " Thank you for sharing!");

const titleWord = prompt("6) Enter a word to set as the page title:");
if (titleWord) {
  document.title = titleWord;
  alert("Page title set to: " + titleWord);
}
