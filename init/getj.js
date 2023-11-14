function getData(xy){
    let x="stock"+xy+".json";
    fetch(x).then(function(response){
      return response.json();}).then(function(data){
      let ans=document.querySelector("#an");
      for (let i=0;i<data.data.list.length;i++){
      let result=data.data.list[i];
      ans.innerHTML+="<li><div class='price' style=''><span>"+result.symbol+"</span>"+"<span>"+result.symbolName+"</span>"+"<span>"+result.price+"</span>"+"<span>"+result.change+"</span>"+"<span>"+result.regularMarketPreviousClose+"</span>"+"</div></li>";
    }})
    }
let currentIndex = 0;
document.addEventListener("wheel",function(event){
    if(event.deltaY>0,currentIndex<=5){
        getData(currentIndex);
        currentIndex++;
    }
})
// function nextFile() {
// getData(currentIndex);
// currentIndex++; 
// }