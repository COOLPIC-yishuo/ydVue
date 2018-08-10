from django.shortcuts import render,redirect,HttpResponse
from django.views import View
import pymysql
import math
from .page import *
db = pymysql.connect("localhost","root","root",database="yishuo",cursorclass=pymysql.cursors.DictCursor)

class zan(View):
    def get(self,request):
        page = request.GET.get("page") if request.GET.get("page") else 0
        page = int(page)
        num = 3
        cursor = db.cursor()
        sql = "select zid,zname,cid,cname,ctext from dianzan LEFT JOIN content on zcid=ctext limit %s,%s"
        cursor.execute(sql,(num*page,num))
        result = cursor.fetchall()
        sqls = "select count(*) as t from dianzan"
        cursor.execute(sqls)
        nums = cursor.fetchone()
        nums = nums["t"]
        nums = math.ceil(nums/num)
        return render(request, "zan/zan.html", {"data":result,"page":getpages(nums,page,"/zan")})
class zanadd(View): #???
    def get(self,request):
        cursor = db.cursor()
        sql = "select * from content"
        cursor.execute(sql)
        result = cursor.fetchall()
        return render(request,"zan/zanadd.html",{"data":result})
    def post(self,request):
        zname = request.POST.get("zname")
        cid = request.POST.get("zcid")
        cursor = db.cursor()
        sql = "insert into dianzan(zname,zcid) VALUES (%s,%s)"
        cursor.execute(sql,[zname,cid])
        db.commit()
        return redirect("/zan/")
class zandel(View):
    def get(self,request):
        zid = request.GET.get("zid")
        cursor = db.cursor()
        sql = "delete from dianzan where zid=%s"
        cursor.execute(sql,[zid])
        db.commit()
        return redirect("/zan/")
class zanedit(View):
    def get(self,request):
        zid = request.GET.get("zid")
        cursor = db.cursor()
        sql = "select zid,zname,cid,cname,ctext from dianzan LEFT JOIN content on zcid=ctext where zid=%s"
        cursor.execute(sql,[zid])
        result = cursor.fetchone()
        sqls = "select * from content"
        cursor.execute(sqls)
        zanInfo = cursor.fetchall()
        return render(request,"zan/zanedit.html",{"data":result,"zanInfo":zanInfo})
    def post(self,request):
        zid = request.POST.get("zid")
        zname = request.POST.get("zname")
        zcid = request.POST.get("zcid")
        cursor = db.cursor()
        sql = "update dianzan set zname=%s,zcid=%s where id=%s"
        cursor.execute(sql,[zname,zcid,zid])
        db.commit()
        return redirect("/zan/")


