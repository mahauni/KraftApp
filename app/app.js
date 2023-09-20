

let action = document.getElementById("action");
let actionDesc = document.getElementById("desc-action");
let esg = document.getElementById("esg");
let esgDesc = document.getElementById("esg-desc");



document.querySelector('esgForm').addEventListener('submit', function () {
  console.log(action.value)
  console.log(actionDesc.value)
  console.log(esg.value)
  console.log(esgDesc.value)

});