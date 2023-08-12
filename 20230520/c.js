const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin", "utf8").split("\n");
let [a, ...charArrays] = inputs;

let = [amount, length] = a.split(" ");
const before = [...charArrays];

const matched = [];

for (let i = 0; i < charArrays.length; i++) {
  const [chars] = before.splice(i, 1);
  for (let j = 0; j < before.length; j++) {
    if (j === 0) {
      matched.push([]);
    }
    if (isMatch(chars, before[j], length)) {
      matched[i] = [...matched[i], before[j]];
    }
  }
  if (matched[i].length === 0) {
    console.log("No");
    process.exit(0);
  } else {
    before.splice(i, 0, chars);
  }
}
let count = 0;
for (let i = 0; i < matched.length; i++) {
  if (matched[i].length === 1) {
    count++;
  }

  if (count > length / 2) {
    console.log("No");
    process.exit(0);
  }
}

console.log("Yes");

// 文字列a,bに対し、length - 1 文字が一致するかどうかを返す。
function isMatch(a, b, length) {
  let count = 0;
  for (let i = 0; i < length; i++) {
    if (a[i] === b[i]) {
      count++;
    }
  }
  return count === length - 1;
}
