from django.shortcuts import render,redirect,HttpResponse
from django.views import View
import pymysql
from .page import *

db = pymysql.connect("localhost","root","root",database="yishuo",cursorclass=pymysql.cursors.DictCursor)

class share(View):
    def get(self,request):
        page = request.GET.get("page") if request.GET.get("page") else 0
        page = int(page)
        num = 3
        cursor = db.cursor()
        sql = "select sid,sname,cname,ctext from share LEFT JOIN content on scid=cid limit %s,%s"
        cursor.execute(sql,(page*num,num))
        result = cursor.fetchall()
        sqls = "select count(*) as t from share"
        cursor.execute(sqls)
        nums = cursor.fetchone()
        nums = nums["t"]
        nums = math.ceil(nums/num)
        return render(request, "share/share.html", {"data": result,"page":getpages(nums,page,"/share")})
class shareadd(View):
    def get(self,request):
        cursor = db.cursor()
        sql = "select * from content"
        cursor.execute(sql)
        result = cursor.fetchall()
        return render(request,"share/shareadd.html",{"data":result})
    def post(self,request):
        cursor = db.cursor()
        sname = request.POST.get("sname")
        scid = request.POST.get("scid")
        print(sname,scid)
        sql = "insert into share(sname,scid) VALUES (%s,%s)"
        cursor.execute(sql,[sname,scid])
        db.commit()
        return redirect("/share/")
class sharedel(View):
    def get(self,request):
        sid = request.GET.get("sid")
        cursor = db.cursor()
        sql = "delete from share where sid=%s"
        cursor.execute(sql,[sid])
        db.commit()
        return redirect("/share/")
class shareedit(View):
    def get(self,request):
        sid = request.GET.get("sid")
        cursor = db.cursor()
        sql = "select sid,sname,cname,ctext from share LEFT JOIN content on scid=cid where sid=%s"
        cursor.execute(sql,[sid])
        result = cursor.fetchone()
        sqls = "select * from content"
        cursor.execute(sqls)
        shareInfo = cursor.fetchall()
        return render(request,"share/shareedit.html",{"data":result,"shareInfo":shareInfo})
    def post(self,request):
        sid = request.POST.get("sid")
        sname = request.POST.get("sname")
        scid = request.POST.get("scid")
        cursor = db.cursor()
        sql = "update share set sname=%s,scid=%s where sid=%s"
        cursor.execute(sql,[sname,scid,sid])
        db.commit()
        return redirect("/share/")