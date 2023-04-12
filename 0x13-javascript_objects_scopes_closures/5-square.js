#!/usr/bin/node

// import the Rectangle class
const Rectangle = require('./4-rectangle');

// define the Square class that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    // call the constructor of Rectangle with the size argument for both width and height
    super(size, size);
  }
}

// export the Square class
module.exports = Square;
