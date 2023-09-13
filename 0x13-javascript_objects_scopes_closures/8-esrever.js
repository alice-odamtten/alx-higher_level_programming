#!/usr/bin/node

exports.esrever = function (list) {
  const reveList = [];
  for (let i = 1; i <= list.length; i++) {
    reveList.push(list[list.length - i]);
  }
  return reveList;
};
