#!/usr/bin/node

const [arg] = process.argv.slice(2); // Ignore first two arguments (node executable and script file)

const num = parseInt(arg);

if (isNaN(num) || num === undefined) {
  console.log('Not a Number');
} else {
  console.log(`My number: ${num}`);
}
