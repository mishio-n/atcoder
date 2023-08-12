const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin", "utf8").split("\n");
let [n, arr] = inputs;
const array = arr.split(" ").map((x) => +x);

for (let i = 0; i < n; i++) {
  if (i === 0) {
    continue;
  }

  const diff = Math.abs(array[i] - array[i - 1]);
  if (diff === 1) {
    continue;
  }

  if (array[i] > array[i - 1]) {
    for (let j = 0; j < diff - 1; j++) {
      array.splice(i + j, 0, array[i - 1] + j + 1);
      n++;
    }
  } else {
    for (let j = 0; j < diff - 1; j++) {
      array.splice(i + j, 0, array[i - 1] - j - 1);
      n++;
    }
  }
}

console.log(array.join(" "));
