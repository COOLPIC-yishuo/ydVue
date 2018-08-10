from django.shortcuts import render,redirect,HttpResponse
from django.views import View
import pymysql
from .login import md5
import math
from .page import *
from django import forms
import time
import random
db = pymysql.connect("localhost","root","root",database="yishuo",cursorclass=pymysql.cursors.DictCursor)

class user(View):
    def get(self,request):
        page = request.GET.get("page") if request.GET.get("page") else 0
        page = int(page)
        num = 3
        cursor = db.cursor()
        sql = "select * from user limit %s,%s"
        cursor.execute(sql,(page*num,num))
        result = cursor.fetchall()
        sqls = "select count(*) as t from user"
        cursor.execute(sqls)
        nums = cursor.fetchone()
        nums = nums["t"]
        nums = math.ceil(nums/num)
        return render(request, "user/user.html", {"data":result,"page":getpages(nums,page,"/user")})

class mycheck(forms.Form):
    uimage = forms.FileField(required=True,error_messages={"required": "必须选择文件"})
class useradd(View):
    def get(self,request):
        return render(request,"user/useradd.html")
    def post(self,request):
        obj = mycheck(request.POST,request.FILES)
        if obj.is_valid():
            cursor = db.cursor()
            uname = request.POST.get("uname")
            upass = md5(request.POST.get("upass"))
            uaddr = request.POST.get("uaddr")
            uposition = request.POST.get("uposition")
            ulabel = request.POST.get("ulabel")
            umotto = request.POST.get("umotto")
            ugrade = request.POST.get("ugrade")
            uimage = request.FILES["uimage"]
            filepath = "static/upload/"+str(int(time.time()*1000))+str(random.randint(1,1000))+".png"
            obj = open(filepath,"wb")
            for item in uimage.chunks():
                obj.write(item)
            obj.close()
            sql = "insert into user(uname,upass,uaddr,uposition,ulabel,umotto,ugrade,uimage) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            localhost = "http://localhost:8000/"
            filepath = localhost + filepath
            cursor.execute(sql,[uname,upass,uaddr,uposition,ulabel,umotto,ugrade,filepath])
            db.commit()
            return redirect("/user/")
class userdel(View):
    def get(self,request):
        id = request.GET.get("uid")
        cursor = db.cursor()
        sql = "delete from user where uid=%s"
        cursor.execute(sql,[id])
        db.commit()
        return redirect("/user/")
    def post(self,request):
        pass
class useredit(View):
    def get(self,request):
        uid = request.GET.get("uid")
        cursor = db.cursor()
        sql = "select * from user where uid=%s"
        cursor.execute(sql,[uid])
        result = cursor.fetchone()
        return render(request,"user/useredit.html",{"data":result})
    def post(self,request):
        uid = request.POST.get("uid")
        uname = request.POST.get("uname")
        upass = request.POST.get("upass")
        uaddr = request.POST.get("uaddr")
        uposition = request.POST.get("uposition")
        ulabel = request.POST.get("ulabel")
        umotto = request.POST.get("umotto")
        ugrade = request.POST.get("ugrade")
        uimage = request.POST.get("uimage")
        cursor = db.cursor()
        sql = "update user set uname=%s,upass=%s,uaddr=%s,uposition=%s,ulabel=%s,umotto=%s,ugrade=%s,uimage=%s where uid=%s"
        cursor.execute(sql,[uname,upass,uaddr,uposition,ulabel,umotto,ugrade,uimage,uid])
        db.commit()
        return redirect("/user/")
