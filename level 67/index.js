// საკლასო დავალება:

// შექმენით ობიექტი, სადაც გექნებათ შემდეგი გასაღებები: name, surname, academy, city, role, favColor - აქ შეინახავთ მარტივ მონაცემებს (string, number, boolean). კიდევ გექნებათ ობიექტის მეთოდი, რომელიც გამოიტანს კონსოლში ობიექტის სახელს და გვარს ერთად. დაამატეთ კიდევ ერთი მეთოდი, რომელიც გამოიტანს ობიექტის favColor გასაღების მნიშვნელობას.

// მეთოდებზე მუშაობისას გამოიყენეთ this keyword.

// 1. კონსოლში დაბეჭდეთ მთლიანი ობიექტი.
// 2. კონსოლში დაბეჭდეთ ნებისმიერი კუთვნილება ობიექტის.
// 3. გამოიძახეთ ობიექტის რომელიმე მეთოდი.
// 4. შეცვალეთ ობიექტის რომელიმე მნიშვნელობა და შემდეგ კონსოლში დაბეჭდეთ ეს მნიშვნელობა

let student = {
  name: "Vato",
  surname: "Tsaishvili",
  academy: "GOA Academy",
  city: "Zugdidi",
  role: "Student",
  favColor: "Black",

getFullName: function() {
    return this.name + " " + this.surname;
},

getFavColor: function() {
    return this.favColor;
}
};

console.log(student);
console.log(student.city);
console.log(student.getFullName());

student.city = "Batumi";
console.log(student.city);


function userOperations() {
    let first = confirm("do you have phone: ");
    let second = confirm("do you have pc : ");
    
    console.log(first || second)
    console.log(first && second)
    }