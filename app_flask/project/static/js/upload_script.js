function uploadFile() {
  const fileUpload = document.getElementById("fileUpload");
  const fileList = document.getElementById("fileList");

  const file = fileUpload.files[0];
  const fileName = file.name;

  // Perform API call with the fileName as a variable
  performAPICall(fileName);

  const fileItem = document.createElement("div");
  fileItem.className = "fileItem";

  const fileNameElement = document.createElement("span");
  fileNameElement.className = "fileName";
  fileNameElement.textContent = fileName;

  const fileButton = document.createElement("button");
  fileButton.className = "fileButton";
  fileButton.textContent = "Use";
  fileButton.addEventListener("click", function () {
    performAPICall(fileName);
  });

  fileItem.appendChild(fileNameElement);
  fileItem.appendChild(fileButton);

  fileList.appendChild(fileItem);
}

function performAPICall(fileName) {
  // Implement your API call logic here
  console.log("Performing API call with fileName:", fileName);
}

document.getElementById("upload").addEventListener("change", handleFileUpload);

function handleFileUpload(event) {
  const files = event.target.files;
  const fileList = document.getElementById("file-list");

  // 기존 목록 초기화
  fileList.innerHTML = "";

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const listItem = document.createElement("li");
    const button = document.createElement("button");

    button.textContent = "API 사용";
    button.className = "button";
    button.addEventListener("click", () => {
      // 클릭한 버튼에 해당하는 파일 이름을 API에 전달
      callAPI(file.name);
    });

    listItem.textContent = file.name;
    listItem.appendChild(button);

    fileList.appendChild(listItem);
  }
}

function callAPI(filename) {
  // 여기에 파일 이름을 사용하는 API 호출 코드 작성
  // 예시: console.log(filename);
}

// const btnClick = document.getElementById("btnAppend");

// btnClick.addEventListener("click", function () {
//   const ulNode = document.getElementById("category");
//   const liNode = document.createElement("li");

//   liNode.textContent = "li 요소";
//   ulNode.appendChild(liNode);
// });

// const btnUpload = document.getElementById("btnUpload");
// btnClick.addEventListener("click", function () {
//   console.log(1);
// });

// const inputfile = document.getElementById("inputfile");
