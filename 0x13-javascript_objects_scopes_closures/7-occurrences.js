#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  let nOccurrences = 0;

  // iterate over the list and increment count if the element is found
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      nOccurrences++;
    }
  }

  return nOccurrences;
};
