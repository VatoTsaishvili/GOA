function addNewElement() {
    const divBlock = document.getElementById("myDiv");

    const button = document.createElement("button");

    const buttonText = document.createTextNode("ჩემი ღილაკი");
    button.appendChild(buttonText);

    divBlock.appendChild(button);
}
