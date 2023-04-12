#!/usr/bin/node

// import the Square class
const ParentSquare = require('./5-square');

// define the Square class that inherits from Square
class Square extends ParentSquare {
  charPrint (c) {
    // if c is undefined, use X as default
    if (c === undefined) {
      c = 'X';
    }

    // print the square using the character c
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

// export the Square class
module.exports = Square;
