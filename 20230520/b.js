const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin", "utf8").split("\n");
let [lines, ...chars] = inputs;

let = [height, width] = lines.split(" ");

console.log(height, width, chars);

for (let i = 0; i < height; i++) {
  for (let j = 0; j < width; j++) {
    if (chars[i][j] === "s") {
      if (n !== undefined) {
        isNeibor(`${i + 1} ${j + 1}`, n);
        s = `${i + 1} ${j + 1}`;
      }
    }
    if (chars[i][j] === "n") {
      n = `${i + 1} ${j + 1}`;
    }
    if (chars[i][j] === "u") {
      u = `${i + 1} ${j + 1}`;
    }
    if (chars[i][j] === "k") {
      k = `${i + 1} ${j + 1}`;
    }
    if (chars[i][j] === "e") {
      e = `${i + 1} ${j + 1}`;
    }
  }
}

const isNeibor = (a, b) => {
  let [ax, ay] = a.split(" ");
  let [bx, by] = b.split(" ");
  return Math.abs(ax - bx) + Math.abs(ay - by) === 1;
};
