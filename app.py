from flask import Flask,render_template,render_template_string,flash,request,redirect,session
# from flask import url_for,jsonify
import moudule.Getjdata as Getjdata
import mongo
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

@app.route("/login")
def login():   
    session.clear()
    return render_template("login.html")

@app.route("/loginin",methods=['POST'])
def loginside():
    enum=request.form['enum']
    pwd=request.form['pwd']
    result=mongo.collection.find_one({
        "$and":[
            {"enum":enum},
            {"pwd":pwd}
        ]
        })
    if enum=="admin" and pwd=="pass":
      session["username"]=enum
      return redirect("/backendcontrol")
    elif result==None:
        return redirect("/loginnok")
    else:
        session["username"]=result['uname']
        return redirect("/loginok")

@app.route("/backendcontrol")
def control():
    username=session.get("username")
    if username=="admin":
        jdata=list(mongo.collection.find({},sort=[
    ('enum',mongo.pymongo.ASCENDING)
]))
        return render_template("systemcall.html",jdata=jdata)
    else:
        return redirect("/")

@app.route("/erase/<enum>")
def erase(enum):
    username=session.get("username")
    if username=="admin":
        mongo.collection.delete_one({"enum":enum})
        return redirect("/backendcontrol")
    else:
        return redirect("/")

@app.route("/modify/<enum>",methods=['get'])
def modify(enum):
    username=session.get("username")
    if username=="admin":
        jdata=mongo.collection.find_one({'enum':enum})
        if jdata:
            return render_template("modify.html",jdata=jdata)
        else:
            return 404
    else:
        return redirect("/")
    
@app.route("/update/<enum>",methods=['POST'])
def update(enum):
    username=session.get("username")
    if username=="admin":
        mongo.collection.update_one({'enum':enum},{"$set":{
        'uname':request.form.get("uname"),
        'enum':request.form.get("enum"),
        'email':request.form.get("email"),
        'email2':request.form.get("email2"),
        'bir':request.form.get("bir")}})
        return redirect("/backendcontrol")
    else:redirect("/")

@app.route("/loginnok")
def loginok():
    html_content = """
    <html>
    <body>
        <div style="text-align:center;color:blue;font-size:140%">登入失敗，即將返回...
        <br>
        </div>
        <script>
            setTimeout(function() {
                window.location.href = '/login';
            }, 2000); // 延迟时间为 1000 毫秒(1 秒)
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route("/loginok")
def loginnok():
    username=session["username"]
    html_content = """
    <html>
    <body>
        <div style="text-align:center;color:blue;font-size:140%">登入成功，即將跳轉...
        <br>
        {{ username }}你好
        </div>
        <script>
            setTimeout(function() {
                window.location.href = '/';
            }, 2000); // 延迟时间为 1000 毫秒(1 秒)
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content,username=username)

@app.route("/signup")
def signup():   
    return render_template("signup.html")

@app.route("/signupcheck",methods=['POST'])
def signupcheck():
    dataform={
    'uname':request.form.get("uname"),
    'enum':request.form.get("enum"),
    'pwd':request.form.get("pwd"),
    'sex':request.form.get("sex"),
    'email':request.form.get("email"),
    'email2':request.form.get("email2"),
    'bir':request.form.get("bir"),
    'licenses':request.form.getlist("licenses[]"),
    'intro':request.form.get("intro")}
    session.update(dataform)
    if not all([dataform['uname'], dataform['enum'], dataform['pwd'], dataform['sex'], dataform['email'], dataform['bir'], dataform['intro']]):
        flash("有字段是必填的，請確保填寫完畢。")
        return redirect("/signup")
    return render_template("signupcheck.html",**dataform)

@app.route("/signupdone")
def signdone():
    mongo.insertdata(session['uname'],session['enum'],session['pwd'],session['sex'],session['email'],session['email2'],session['bir'],session['licenses'])
    return  "hello"+ session['uname']

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

@app.route("/learning")
def learning():
    return render_template("learning.html")

if __name__=="__main__":
    app.run(use_reloader=False,debug=True)
