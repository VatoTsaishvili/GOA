// საკლასო დავალება:

// შექმენით ფუნქცია სახელად userLoop. ამ ფუნქციაში მომხმარებელს შემოატანინეთ ორი რიცხვი და შეინახეთ ისინი ცვლადებში, number მონაცემთა ტიპში.

// თქვენი დავალებაა, რომ პირველი რიცხვიდან მეორე რიცხვამდე ყველა რიცხვი დაბეჭდოთ კონსოლში. გამოიყენეთ ნებისმიერი ციკლი.

// ეს ფუნქცია გაუშვით მაშინ, როდესაც ვებსაიტი ჩაიტვირთება

// function userLoop() {
//   let firstNumber = Number(prompt("შეიყვანეთ პირველი რიცხვი:"));
//   let secondNumber = Number(prompt("შეიყვანეთ მეორე რიცხვი:"));

//   for (let i = firstNumber; i <= secondNumber; i++) {
//     console.log(i);
//   }
// }

function changeElements() {
  let input = document.getElementById('input');
  let btn = document.getElementById('btn');
  let header = document.getElementById('header');

  console.log(input.value);

  btn.style.backgroundColor = 'black';
  btn.style.color = 'white';

  header.style.textAlign = 'center';

  document.body.style.backgroundColor = 'green';
}
