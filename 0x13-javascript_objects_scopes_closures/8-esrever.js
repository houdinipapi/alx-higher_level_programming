#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  // iterate over the list in reverse order and push each element to the new list
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
