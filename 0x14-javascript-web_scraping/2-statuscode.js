#!/usr/bin/node
const args = process.argv;

const request = require('request');

request(args[2], (error, response) => {
  if (error) console.log(error);

  console.log('code: ', response.statusCode);
});
