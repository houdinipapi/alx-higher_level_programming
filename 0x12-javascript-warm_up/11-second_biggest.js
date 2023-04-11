#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const n = args.length;

if (n === 0 || n === 1) {
  console.log(0);
} else {
  let max = args[0];
  let secondMax = args[1];

  if (secondMax > max) {
    [max, secondMax] = [secondMax, max];
  }

  for (let i = 2; i < n; i++) {
    const current = args[i];
    if (current > max) {
      secondMax = max;
      max = current;
    } else if (current > secondMax) {
      secondMax = current;
    }
  }

  console.log(secondMax);
}
