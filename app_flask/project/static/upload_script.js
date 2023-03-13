const btnClick = document.getElementById("btnAppend");

btnClick.addEventListener("click", function () {
  const ulNode = document.getElementById("category");
  const liNode = document.createElement("li");

  liNode.textContent = "li 요소";
  ulNode.appendChild(liNode);
});

const btnUpload = document.getElementById("btnUpload");
btnClick.addEventListener("click", function () {
  console.log(1);
});

const inputfile = document.getElementById("inputfile");
