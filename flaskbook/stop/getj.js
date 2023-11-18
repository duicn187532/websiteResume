var sect ='';
var iframeDocument='';
var answ='';

function getData(xy,sect){
        let x="/json?batch="+xy+"&sectid="+sect;
        return new Promise((resolve)=>{
            fetch(x).then(function(response){
            return response.json();}).then(function(data){
            let ans=document.querySelector("#an");
            for (let i=0;i<data.data.list.length;i++){
            let result=data.data.list[i];
            ans.innerHTML+="<div class='price' style=''><span>"+result.symbol+"</span>"+"<span>"+result.symbolName+"</span>"+"<span>"+result.price+"</span>"+"<span>"+result.change+"</span>"+"<span>"+result.regularMarketPreviousClose+"</span>"+"</div>";
            resolve();
            }})
            })}



function load(cate){
    sect=cate;
    let frame = document.querySelector("#space");
    let iframe = document.createElement('iframe');
    iframe.style.flex=3;
    iframe.style.width = '100%';
    iframe.height = '400';
    iframe.src = '/TAI1';
    frame.innerHTML = '';
    frame.appendChild(iframe);
    iframe.onload = async function() {
        for(r=0;r<=5;r++){
       await iframe.contentWindow.getData(r,sect);} // 將 iframe 的文檔作為參數傳遞給 getJ 函數
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
