// 我的家庭用JS //
/* 存放變數 */
// let pig="董事長";
// let dollm="社畜";
// const pigpig="老闆";
// const dollmm="打工人";
// const pang=true;
// const wang=false;
// var wong=1;
// var yang=2;
/* 我是底線 */
/*console.log("Hello Family");
console.log("Hello 豬董");
console.log(pig)
console.log(pig,"雇用了",dollm)
console.log(pigpig)
console.log(dollmm)
console.log(wong-yang)
console.log(pang,wang)
var wong=2+wong;
if (wong+yang==3&&pang==true) {console.log("王宥辰");}
    else{console.log("王有陳",wong);};*/
// let n1=prompt("請輸入帳號","AC");
// let n2=prompt("請輸入ID","ID");
// console.log(n1,n2);
// var x=0;
// while(x<=5){console.log(x);x++;};
// for(x=0;x<10;x++){console.log(x);}
// let x=0
// let r=0
// while (x<=10){r=r+x;x=x+1;}
// console.log(r);
// let obj=new Object();
// obj.x=2;
// obj.y=4
// obj.show= function() {console.log(this.x,this.y);};
// obj.show();
// let obj1={};
// let obj2={
//     x:1,
//     y:5,
//     show:function(){console.log(this.x,this.y);}
// }
// obj2.show();
// console.log(obj2);
// console.log(obj2.x);

// let arr=[];
// arr.push(3,4,5);
// console.log(arr.length);
// arr.push(6);
// console.log(arr.length)
// let total=0;
// for (let i=0;i<arr.length;i++){
//     total=total+arr[i]
// }
// console.log(total/arr.length)
// console.log(document.body)
// window.location.href="http://www.google.com/";
// console.log(window.document);
// console.dir(document);
// console.log(document.title);
// document.title="我家";
// console.log(document.title);
// console.log(document.body);
// console.log(document.body.innerHTML);
// document.body.innerHTML="Hello DOM"
// window.alert("歡迎參觀")
// console.log(window.screen.height,window.screen.width)
// console.dir(window.document)

let cat=document.querySelector("#hachiman");
cat.style.color="red";
function mycat(){
                let changecolor=document.querySelector("#hachiman");
                changecolor.style.color="green";
                let hachi=document.createElement("img");
                hachi.src="IMG_6237.jpeg"
                hachi.id="backgroundimg"
                document.body.appendChild(hachi)
                var invisible=document.getElementById("color")
                invisible.innerHTML="ol{list-style-type:cjk-ideographic;}ul li{padding: 1;margin:0;list-style-position: outside;}.cat{cursor: pointer;}"
                }
function yourcat(){
                let changecolor=document.querySelector("#olet");
                changecolor.style.color="blue";
                let oulet=document.getElementById("backgroundimg");
                oulet.src="IMG_6806.jpeg"
                    }
                    
fetch().then(function(){
    return Response.text();
}).then(function(data){
    console.log(data);
});