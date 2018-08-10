from django.shortcuts import render,redirect,HttpResponse
from django.views import View
import pymysql
from .page import *
from django import forms
db = pymysql.connect("localhost","root","root",database="yishuo",cursorclass=pymysql.cursors.DictCursor)

class types(View):
    def get(self,request):
        page = request.GET.get("page") if request.GET.get("page") else 0
        page = int(page)
        num = 3
        cursor = db.cursor()
        sql = "select * from types limit %s,%s"
        cursor.execute(sql,(page*num,num))
        result = cursor.fetchall()
        sqls = "select count(*) as t from types"
        cursor.execute(sqls)
        nums = cursor.fetchone()
        nums = nums["t"]
        nums = math.ceil(nums/num)
        return render(request, "types/types.html", {"data": result,"page":getpages(nums,page,"/types")})
    def post(self,request):
        pass
class typeadd(View):
    def get(self,request):
        return render(request,"types/typeadd.html")
    def post(self,request):
        tname = request.POST.get("tname")
        ttid = request.POST.get("ttid")
        cursor = db.cursor()
        sql = "insert into types(tname,ttid) VALUES (%s,%s)"
        cursor.execute(sql,[tname,ttid])
        db.commit()
        return redirect("/types/")
class typedel(View):
    def get(self,request):
        tid = request.GET.get("tid")
        cursor = db.cursor()
        sql = "delete from types WHERE tid=%s"
        cursor.execute(sql,[tid])
        db.commit()
        return redirect("/types/")
class typeedit(View):
    def get(self,request):
        tid = request.GET.get("tid")
        cursor = db.cursor()
        sql = "select * from types WHERE tid=%s"
        cursor.execute(sql,[tid])
        result = cursor.fetchone()
        return render(request,"types/typeedit.html",{"data":result})
    def post(self,request):
        tid = request.POST.get("tid")
        tname = request.POST.get("tname")
        ttid = request.POST.get("ttid")
        print(tname,ttid,tid)
        cursor = db.cursor()
        sql = "update types set tname=%s,ttid=%s where tid=%s"
        cursor.execute(sql,[tname,ttid,tid])
        db.commit()
        return redirect("/types/")