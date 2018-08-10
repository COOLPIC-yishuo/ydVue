from django.shortcuts import render,redirect,HttpResponse
from django.views import View
import pymysql
from django import forms
from .page import *
import math
import random
import time
db = pymysql.connect("localhost","root","root",database="yishuo",cursorclass=pymysql.cursors.DictCursor)

class rotate(View):
    def get(self,request):
        page = request.GET.get("page") if request.GET.get("page") else 0
        page = int(page)
        num = 3
        cursor = db.cursor()
        sql = "select rid,raddr,cname from rotate LEFT JOIN content on content.cid = rotate.rcid limit %s,%s"
        cursor.execute(sql,(page*num,num))
        result = cursor.fetchall()
        sqls = "select count(*) as t from rotate"
        cursor.execute(sqls)
        nums = cursor.fetchone()
        nums = nums["t"]
        nums = math.ceil(nums/num)
        return render(request, "rotate/rotate.html", {"data": result,"page":getpages(nums,page,"/rotate")})
class mycheck(forms.Form):
    raddr = forms.FileField(required=True,error_messages={"required": "必须选择文件"})
class rotateadd(View):
    def get(self,request):
        return render(request,"rotate/rotateadd.html")
    def post(self,request):
        obj = mycheck(request.POST,request.FILES)
        if obj.is_valid():
            file = request.FILES["raddr"]
            filepath = "static/upload/"+str(int(time.time()*1000))+str(random.randint(1,1000))+".jpg"
            obj = open(filepath,"wb")
            for item in file.chunks():
                obj.write(item)
            obj.close()
            cursor = db.cursor()
            sql = "insert into rotate(raddr) VALUES (%s)"
            localhost="http://localhost:8000/"
            filepath=localhost+filepath
            cursor.execute(sql,[filepath])
            db.commit()
            return redirect("/rotate/")

class rotatedel(View):
    def get(self,request):
        rid = request.GET.get("rid")
        cursor = db.cursor()
        sql = "delete from rotate where rid=%s"
        cursor.execute(sql,[rid])
        db.commit()
        return redirect("/rotate/")

class rotateedit(View):
    def get(self,request):
        cursor = db.cursor()
        rid = request.GET.get("rid")
        sql = "select * from rotate where rid=%s"
        cursor.execute(sql,[rid])
        result = cursor.fetchone()
        return render(request,"rotate/rotateedit.html",{"data":result})
    def post(self,request):
        obj = mycheck(request.POST, request.FILES)
        if obj.is_valid():
            rid = request.POST.get("rid")
            file = request.FILES["raddr"]
            filepath = "static/upload/" + str(int(time.time() * 1000)) + str(random.randint(1, 1000)) + ".jpg"
            obj = open(filepath, "wb")
            for item in file.chunks():
                obj.write(item)
            obj.close()
            cursor = db.cursor()
            sql = "update rotate set raddr=%s where rid=%s"
            localhost = "http://localhost:8000/"
            filepath = localhost + filepath
            cursor.execute(sql,[filepath,rid])
            db.commit()
            return redirect("/rotate/")

