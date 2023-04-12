#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  // iterate over the list and increment count if the element is found
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }

  return count;
};
