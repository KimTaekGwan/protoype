const btn = document.getElementById("search_btn");
const result = document.getElementById("result");
const fastapi_res = document.getElementById("fastapi_res");
let num = 1;

btn.addEventListener("click", async function () {
  console.log(num);
  num += 1;
  changeNum(num);
  changeText(result, num);
  await output_fastapi(fastapi_res);
});

function changeNum(num) {
  console.log(num);
}

function changeText(result, num) {
  //   alert(result.innerText);
  result.innerText = num;
}

function changefastapi_res(fastapi_res, num) {
  //   alert(result.innerText);
  fastapi_res.innerText = num;
}

async function output_fastapi(fastapi_res) {
  const url = "http://127.0.0.1:8000/image/items/222?q=2";

  const data = "s";

  const response = await fetch(url, {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: data,
  });

  const res = await response.text();

  console.log(res);
  changefastapi_res(fastapi_res, res);
}
