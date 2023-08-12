const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin", "utf8").split("\n");
let [a, b] = inputs;

const candidates = ["a", "t", "c", "o", "d", "e", "r", "@"];

const aArray = a.split("").sort();
const bArray = b.split("").sort();

for (let i = 0; i < aArray.length; i++) {
  if (aArray[i] === "@") {
    continue;
  }
  for (let j = 0; j < bArray.length; j++) {
    if (bArray[j] === "@") {
      continue;
    }
    if (aArray[i] === bArray[j]) {
      aArray.splice(i, 1);
      bArray.splice(j, 1);
      i--;
      j--;
      break;
    }
    if (!candidates.includes(aArray[i - 1])) {
      console.log("No");
      process.exit(0);
    }
  }
}

console.log("Yes");
