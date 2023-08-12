const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin", "utf8").split("\n");
const [n, results] = inputs;

let a = 0;
let t = 0;

for (let i = 0; i < n; i++) {
  if (results[i] === "A") {
    a++;
  } else {
    t++;
  }

  if (a >= n / 2) {
    console.log("A");
    break;
  }

  if (t >= n / 2) {
    console.log("T");
    break;
  }
}
