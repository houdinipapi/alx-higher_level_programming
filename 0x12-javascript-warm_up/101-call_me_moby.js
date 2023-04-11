#!/usr/bin/node

// Using CommonJS modules
function executeXTimes (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = executeXTimes;
