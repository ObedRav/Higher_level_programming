#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);

    const dict = {};

    for (const obj of content) {
      if (obj.completed === true) {
        if (dict[obj.userId]) {
          dict[obj.userId] += 1;
        } else {
          dict[obj.userId] = 1;
        }
      }
    }

    console.log(dict);
  }
});
