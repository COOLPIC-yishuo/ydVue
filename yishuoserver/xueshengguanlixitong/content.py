from django.shortcuts import render,redirect,HttpResponse
from django.views import View
import pymysql
import math
from .page import *
from django import forms
import random
import time
db = pymysql.connect("localhost","root","root",database="yishuo",cursorclass=pymysql.cursors.DictCursor)

class content(View):
    def get(self,request):
        page = request.GET.get("page") if request.GET.get("page") else 0
        page = int(page)
        num = 3
        cursor = db.cursor()
        sql = "select * from content LEFT JOIN types on types.ttid = content.ctypes limit %s,%s"
        cursor.execute(sql,(page*num,num))
        result = cursor.fetchall()
        sqls = "select count(*) as t from content"
        cursor.execute(sqls)
        nums = cursor.fetchone()
        nums = nums["t"]
        nums = math.ceil(nums/num)
        return render(request, "content/content.html", {"data": result,"page":getpages(nums,page,"/content")})
    def post(self,request):
        pass

class mycheck(forms.Form):
    cimage = forms.FileField(required=True,error_messages={"required": "必须选择文件"})

class contentadd(View):
    def get(self,request):
        cursor = db.cursor()
        sql = "select * from types"
        cursor.execute(sql)
        result = cursor.fetchall()
        return render(request,"content/contentadd.html",{"data":result})
    def post(self,request):
        obj = mycheck(request.POST, request.FILES)
        if obj.is_valid():
            cname = request.POST.get("cname")
            ctitle = request.POST.get("ctitle")
            ctext = request.POST.get("ctext")
            ctypes = request.POST.get("ctypes")
            cimage = request.FILES["cimage"]
            cstart = request.POST.get("cstart")
            filepath = "static/upload/" + str(int(time.time() * 1000)) + str(random.randint(1, 1000)) + ".png"
            obj = open(filepath, "wb")
            for item in cimage.chunks():
                obj.write(item)
            obj.close()
            cursor = db.cursor()
            sql = "insert into content(cname,ctitle,ctext,ctypes,cimage,cstart) values(%s,%s,%s,%s,%s,%s)"
            localhost = "http://localhost:8000/"
            filepath = localhost + filepath
            cursor.execute(sql,[cname,ctitle,ctext,ctypes,filepath,cstart])
            db.commit()
            return redirect("/content/")

class contentdel(View):
    def get(self,request):
        cid = request.GET.get("cid")
        cursor = db.cursor()
        sql = "delete from content where cid=%s"
        cursor.execute(sql,[cid])
        db.commit()
        return redirect("/content/")

class contentedit(View):
    def get(self,request):
        cid = request.GET.get("cid")
        cursor = db.cursor()
        sql = "select * from content WHERE cid=%s"
        cursor.execute(sql,[cid])
        result = cursor.fetchone()
        sqls = "select * from types"
        cursor.execute(sqls)
        contentInfo = cursor.fetchall()
        return render(request,"content/contentedit.html",{"data":result,"contentInfo":contentInfo})
    def post(self,request):
        obj = mycheck(request.POST, request.FILES)
        if obj.is_valid():
            cid = request.POST.get("cid")
            cname = request.POST.get("cname")
            ctitle = request.POST.get("ctitle")
            ctext = request.POST.get("ctext")
            cstart = request.POST.get("cstart")
            cimage = request.FILES["cimage"]
            filepath = "static/upload/" + str(int(time.time() * 1000)) + str(random.randint(1, 1000)) + ".png"
            obj = open(filepath, "wb")
            for item in cimage.chunks():
                obj.write(item)
            obj.close()
            cursor = db.cursor()
            sql = "update content set cname=%s,ctitle=%s,ctext=%s,cstart=%s,cimage=%s where cid=%s"
            localhost = "http://localhost:8000/"
            filepath = localhost + filepath
            cursor.execute(sql,[cname,ctitle,ctext,cstart,filepath,cid])
            db.commit()
            return redirect("/content/")