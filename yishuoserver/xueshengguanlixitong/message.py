from django.shortcuts import render,redirect,HttpResponse
from django.views import View
import pymysql
import math
from .page import *
db = pymysql.connect("localhost","root","root",database="yishuo",cursorclass=pymysql.cursors.DictCursor)

class message(View):
    def get(self,request):
        page = request.GET.get("page") if request.GET.get("page") else 0
        page = int(page)
        num = 3
        cursor = db.cursor()
        sql = "select mid,mname,mcontent,content.ctext from message LEFT JOIN content on content.cid = message.mcid limit %s,%s"
        cursor.execute(sql,(page*num,num))
        result = cursor.fetchall()
        sqls = "select count(*) as t from message"
        cursor.execute(sqls)
        nums = cursor.fetchone()
        nums = nums["t"]
        nums = math.ceil(nums/num)
        return render(request, "message/message.html", {"data":result,"page":getpages(nums,page,"/message")})

class messageadd(View):
    def get(self,request):
        cursor = db.cursor()
        sql = "select cid,ctext from content"
        cursor.execute(sql)
        result = cursor.fetchall()
        return render(request,"message/messageadd.html",{"data":result})
    def post(self,request):
        cursor = db.cursor()
        mname = request.POST.get("mname")
        mcontent = request.POST.get("mcontent")
        cid = request.POST.get("cid")
        sql = "insert into message(mname,mcontent,mcid) VALUES (%s,%s,%s)"
        cursor.execute(sql,[mname,mcontent,cid])
        db.commit()
        return redirect("/message/")

class messagedel(View):
    def get(self,request):
        mid = request.GET.get("mid")
        cursor = db.cursor()
        sql = "delete from message where mid=%s"
        cursor.execute(sql,[mid])
        db.commit()
        return redirect("/message/")

class messageedit(View):
    def get(self,request):
        cursor = db.cursor()
        mid = request.GET.get("mid")
        sql = "select mid,mname,mcontent,content.ctext from message LEFT JOIN content on content.cid = message.mcid where mid=%s"
        cursor.execute(sql,[mid])
        result = cursor.fetchone()
        sqls = "select * from content"
        cursor.execute(sqls)
        messageInfo = cursor.fetchall()
        return render(request,"message/messageedit.html",{"data":result,"messageInfo":messageInfo})
    def post(self,request):
        cursor = db.cursor()
        mid = request.POST.get("mid")
        mname = request.POST.get("mname")
        mcontent = request.POST.get("mcontent")
        mcid = request.POST.get("mcid")
        sql = "update message set mname=%s,mcontent=%s,mcid=%s where mid=%s"
        cursor.execute(sql,[mname,mcontent,mcid,mid])
        db.commit()
        return redirect("/message/")
