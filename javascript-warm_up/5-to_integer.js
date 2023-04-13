#!/usr/bin/node
if (parseInt(process.argv.slice(2)[0])) {
  console.log(parseInt(process.argv.slice(2)[0]));
} else {
  console.log('Not a number');
}
