from django.shortcuts import redirect,render,HttpResponse
import pymysql
import hashlib
db = pymysql.connect("localhost","root","root",database="yishuo",cursorclass=pymysql.cursors.DictCursor)

def check(callback):
    def a(request):
        if request.session.get("aname") == "yes":
            return callback(request)
        else:
            return redirect(login)
    return a

def md5(str):
    md5=hashlib.md5()
    md5.update(str.encode("utf8"))
    return md5.hexdigest()


#用户登录页面
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        name = request.POST.get("aname")
        pass1 = md5(request.POST.get("apass"))
        save = request.POST.get("asave")
        if name == "" and pass1 == "":
            return render(request, "login.html")
        else:
            cursor = db.cursor()
            sql = "select * from admin where aname=%s and apass=%s"
            cursor.execute(sql,[name,pass1])
            result = cursor.fetchall()
            print("-result",result)
            if len(result) > 0:
                if save:
                    obj = redirect(index)
                    request.session["login"] = "yes"
                    request.session["aname"] = name
                    request.session.set_expiry(60 * 60 * 24 * 7)
                    return obj
                else:
                    obj = redirect(index)
                    request.session["login"] = "yes"
                    request.session["aname"] = name
                    request.session.set_expiry(0)
                    return obj
            else:
                return render(request, "login.html")

#主页
def index(request):
    if request.session.get("login") == "yes":
        result = request.session.get("aname")
        print(result)
        return render(request,"index.html",{"aname":result})
    else:
        return render(request,"login.html")

#头部
@check
def header(request):
    name = request.GET.get("aname")
    return render(request,"header.html",{"aname":name})
def exit(request):
    request.session.clear()
    return redirect(login)
#左侧栏
@check
def lefter(request):
    return render(request,"lefter.html")

#main

def main1(request):
    return render(request,"main1.html")
@check
def footer(request):
    return render(request,"footer.html")






