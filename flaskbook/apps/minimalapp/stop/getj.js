<<<<<<< HEAD
var sect ='';
var iframeDocument='';
var answ='';

function getData(xy,sect){
        let x="/json?batch="+xy+"&sectid="+sect;
            fetch(x).then(function(response){
            return response.json();}).then(function(data){
            let ans=document.querySelector("#an");
            for (let i=0;i<data.data.list.length;i++){
            let result=data.data.list[i];
            ans.innerHTML+="<li><div class='price' style=''><span>"+result.symbol+"</span>"+"<span>"+result.symbolName+"</span>"+"<span>"+result.price+"</span>"+"<span>"+result.change+"</span>"+"<span>"+result.regularMarketPreviousClose+"</span>"+"</div></li>";
            }})
            }

function getJ(iframeDoc) {
    // 使用 iframeDoc 來查找和操作 iframe 內的元素
     answ = iframeDoc.querySelector("#an"); // 假設 iframe 內有一個 id 為 'an' 的元素
    if (answ) {console.log("有ㄟ") // 更改 iframe 內部元素的內容
    }
    else {console.log("沒東西")}
}

function load(cate){
    sect=cate;
    let frame = document.querySelector("#space");
    let iframe = document.createElement('iframe');
    iframe.width = '720';
    iframe.height = '600';
    iframe.src = '/TAI1';
    frame.innerHTML = '';
    frame.appendChild(iframe);
    iframe.onload = function() {
    iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
        // 現在 iframeDocument 包含了 iframe 的內容
        for(r=0;r<=5;r++){
        iframe.contentWindow.getData(r,sect);} // 將 iframe 的文檔作為參數傳遞給 getJ 函數
    };
}

function changeColor(element){ 
    element.style.color="blue"
}
function resetColor(element){
    element.style.color="green"
}

// document.addEventListener("touchend", function(event) {
//     endY = event.changedTouches[0].clientY;

//     // 檢查滑動方向
//     if (startY > endY && currentIndex <= 5) {
//         getData(currentIndex);
//         currentIndex++;
//     }
// }, false);
=======
function getData(xy){
    let x="/json"+xy;
    fetch(x).then(function(response){
      return response.json();}).then(function(data){
      let ans=document.querySelector("#an");
      for (let i=0;i<data.data.list.length;i++){
      let result=data.data.list[i];
      ans.innerHTML+="<li><div class='price' style=''><span>"+result.symbol+"</span>"+"<span>"+result.symbolName+"</span>"+"<span>"+result.price+"</span>"+"<span>"+result.change+"</span>"+"<span>"+result.regularMarketPreviousClose+"</span>"+"</div></li>";
    }})
    }
let currentIndex = 0;
let startY, endY;

document.addEventListener("wheel", function(event) {
    if (event.deltaY > 0 && currentIndex <= 5) {
        getData(currentIndex);
        currentIndex++;
    }
});

document.addEventListener("touchstart", function(event) {
    startY = event.touches[0].clientY;
}, false);

document.addEventListener("touchend", function(event) {
    endY = event.changedTouches[0].clientY;

    // 檢查滑動方向
    if (startY > endY && currentIndex <= 5) {
        getData(currentIndex);
        currentIndex++;
    }
}, false);
>>>>>>> 2ff17551b492f51f838d2cb9be250db0bdb0af44
