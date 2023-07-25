#!/usr/bin/node

const https = require('https');

const url = process.argv[2];

https.get(url, (response) => {
  const statusCode = response.statusCode;

  console.log(`code: ${statusCode}`);
}).on('error', (error) => {
  console.error(error);
});
