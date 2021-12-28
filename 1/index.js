const fs = require("fs");
// Change the callback to specify what challenge you want to run.
fs.readFile("Input.txt", {encoding: "utf-8"}, Challenge2)

function Challenge1 (err, data) {
  if(err) console.error(err);

  let depthArray = data.split("\r\n");
  let depthIncrease = 0;
  let depthDecrease = 0;


  depthArray.forEach((element, index) => {
    if(index === 0) return;
    
    let num1 = Number(element);
    let num2 = Number(depthArray[index - 1]);
    if(num1 > num2) depthIncrease++;
    if(num1 < num2) depthDecrease++;
  });

  console.log(`The depth was increased ${depthIncrease} times!`);
  console.log(`The depth was decreased ${depthDecrease} times!`);
}

function Challenge2 (err, data) {
  if(err) console.error(err);

  let depthArray = data.split("\r\n");
  let depthIncrease = 0;
  let depthDecrease = 0;

  depthArray.forEach((element, index) => {
    let sum1 = Number(element) + Number(depthArray[index + 1]) + Number(depthArray[index + 2]);
    let sum2 = Number(depthArray[index + 1]) + Number(depthArray[index + 2]) + Number(depthArray[index + 3]);

    if(sum1 < sum2) depthIncrease++;
    if(sum1 > sum2) depthDecrease++;
  });

  console.log(`The depth was increased ${depthIncrease} times!`);
  console.log(`The depth was decreased ${depthDecrease} times!`);
}

