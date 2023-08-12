const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin", "utf8");
let [hp, pw] = inputs.split(" ");

let divide = hp / pw;
let rest = hp % pw;
console.log(divide, rest);

if (rest !== 0) {
  divide++;
} else {
  divide--;
}

console.log(divide);
