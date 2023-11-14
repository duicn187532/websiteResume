from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import moudule.Getjdata as Getjdata
app= Flask(
    __name__,
    static_folder="stop", #靜態檔案資料夾的名稱
    static_url_path="/stop", #靜態檔案對應的網址路徑
    template_folder="html"

    )

@app.route("/")
def index():
    return "Hello, Flask"

@app.route("/hello/<name>",methods=["GET","POST"],endpoint="hello-endpoint")#也可以改成get
def hello(username):
    if username=="八萬":
        return f"Hello, {username} !"
    else:
        return f"你好"+username

@app.route("/data")
def getData():
    # print("請求方法",request.method)
    # print("通訊協定",request.scheme)
    # print("主機名稱",request.host)
    # print("路徑",request.path)
    # print("完整網址",request.url)
    # print("瀏覽器和作業系統",request.headers.get("user-agent"))
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hi"
    else:
        return "你好"

@app.route("/getSun")
def getSun():

    maxnum=request.args.get("max",100)
    maxnum=int(maxnum)
    minnum=request.args.get("min",1)
    minnum=int(minnum)
    result=0
    for i in range(minnum,maxnum+1):
        result+=i
    return "總和"+str(result)

@app.route("/login")
def login():   
    return render_template("login.html")

@app.route("/signup")
def signup():   
    return render_template("signup.html")

@app.route("/back")
def backlog():
    return redirect("/login")

@app.route("/stock")
def stock():
    return render_template("stockseacher.html")

@app.route("/json<int:n>")#11/14 json格式從yahoo股市API取得後轉換成文字檔寫在這個路由中
def jsondata(n):
    Sdata=Getjdata.run(n) 
    return Sdata #將此檔案用getjs.js帶入到TAI1中

@app.route("/stock1")
def stock1():
    return render_template("TAI1.html")

if __name__=="__main__":
    app.run(debug=True,port=3000)

