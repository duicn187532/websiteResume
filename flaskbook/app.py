from flask import Flask
from flask import request
from flask import render_template,render_template_string,flash,url_for
from flask import redirect
import moudule.Getjdata as Getjdata
app= Flask(
    __name__,
    static_folder="stop", #靜態檔案資料夾的名稱
    static_url_path="/stop", #靜態檔案對應的網址路徑
    template_folder="html"

    )
app.secret_key = 'some_secret_key'

@app.route("/")
def index():
    return render_template("index.html")

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

@app.route("/loginin",methods=['POST'])
def loginside():
    enum=request.form['enum']
    pwd=request.form['pwd']
    if enum=="admin" and pwd=="pass":
       return redirect("/loginok")
    else:
        return "登入失敗" 
    
@app.route("/loginok")
def loginok():
    html_content = """""
    <html>
    <body>
        <div style="text-align:center;color:blue;font-size:140%">登入成功，即將跳轉...</div>
        <script>
            setTimeout(function() {
                window.location.href = '/';
            }, 2000); // 延迟时间为 1000 毫秒(1 秒)
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

        

@app.route("/signup")
def signup():   
    return render_template("signup.html")

@app.route("/signupcheck",methods=['POST'])
def signupcheck():
    uname=request.form.get("uname")
    enum=request.form.get("enum")
    pwd=request.form.get("pwd")
    sex=request.form.get("sex")
    email=request.form.get("email")
    email2=request.form.get("email2")
    bir=request.form.get("bir")
    licenses=request.form.getlist("licenses[]")
    intro=request.form.get("intro")
    if not all([uname, enum, pwd, sex, email, bir, intro]):
        flash("有字段是必填的，請確保填寫完畢。")
        return redirect("/signup")
    return render_template("signupcheck.html",uname=uname,
    enum=enum,pwd=pwd,sex=sex,email=email,email2=email2,bir=bir,licenses=licenses
    ,intro=intro)   

@app.route("/back")
def backlog():
    return redirect("/login")

@app.route("/stock")
def stock():
    return render_template("stockseacher.html")

@app.route("/TAI1")
def stock1():
    return render_template("TAI1.html")

@app.route("/json")#11/14 json格式從yahoo股市API取得後轉換成文字檔寫在這個路由中
def jsondata():
    batch=request.args.get("batch")
    batch=int(batch)
    sect=request.args.get("sectid")
    sect=int(sect)
    Sdata=Getjdata.run(batch,sect)
    return Sdata #將此檔案用getjs.js帶入到TAI1中

if __name__=="__main__":
    app.run(use_reloader=False,debug=True)

