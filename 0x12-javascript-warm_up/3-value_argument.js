#!/usr/bin/node

const [arg] = process.argv.slice(2); // ignore the first two arguments

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
