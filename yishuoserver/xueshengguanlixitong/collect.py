from django.shortcuts import render,redirect,HttpResponse
from django.views import View
import pymysql
import math
from .page import *

db = pymysql.connect("localhost","root","root",database="yishuo",cursorclass=pymysql.cursors.DictCursor)

class collect(View):
    def get(self,request):
        page = request.GET.get("page") if request.GET.get("page") else 0
        page = int(page)
        num = 3
        cursor = db.cursor()
        sql = "select coid,cocid,cid,coname,ctext from collect LEFT JOIN content on ctext=cocid limit %s,%s"
        cursor.execute(sql,(page*num,num))
        result = cursor.fetchall()
        sqls = "select count(*) as t from collect"
        cursor.execute(sqls)
        nums = cursor.fetchone()
        nums = nums["t"]
        nums = math.ceil(nums/num)
        return render(request, "collect/collect.html", {"data": result,"page":getpages(nums,page,"/collect")})

class collectadd(View):
    def get(self,request):
        cursor = db.cursor()
        sql = "select * from content"
        cursor.execute(sql)
        result = cursor.fetchall()
        return render(request,"collect/collectadd.html",{"data":result})
    def post(self,request):
        cursor = db.cursor()
        coname = request.POST.get("coname")
        cocid = request.POST.get("cocid")
        sql = "insert into collect (coname,cocid) VALUES (%s,%s)"
        cursor.execute(sql,[coname,cocid])
        db.commit()
        return redirect("/collect/")

class collectdel(View):
    def get(self,request):
        coid = request.GET.get("coid")
        cursor = db.cursor()
        sql = "delete from collect where coid=%s"
        cursor.execute(sql,[coid])
        db.commit()
        return redirect("/collect/")

class collectedit(View):
    def get(self,request):
        cursor = db.cursor()
        coid = request.GET.get("coid")
        sql = "select coid,cocid,cid,coname,ctext from collect LEFT JOIN content on ctext=cocid where coid=%s"
        cursor.execute(sql,[coid])
        result = cursor.fetchone()
        sqls = "select * from content"
        cursor.execute(sqls)
        collectInfo = cursor.fetchall()
        return render(request,"collect/collectedit.html",{"data":result,"collectInfo":collectInfo})
    def post(self,request):
        coid = request.POST.get("coid")
        coname = request.POST.get("coname")
        cocid = request.POST.get("cocid")
        cursor = db.cursor()
        sql = "update collect set coname=%s,cocid=%s where coid=%s"
        cursor.execute(sql,[coname,cocid,coid])
        db.commit()
        return redirect("/collect/")