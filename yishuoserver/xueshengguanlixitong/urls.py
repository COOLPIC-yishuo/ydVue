"""xueshengguanlixitong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path

from .login import *
from .user import *
from .types import *
from .content import *
from .message import *
from .zan import *
from .share import *
from .collect import *
from .rotate import *
from .page import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('getpages/',getpages),
    path('', index),
    path('login/',login),  #登录页     也可以使用正则re_path('^login/?$',login),
    path('header/',header),
    path('lefter/',lefter),
    path('main1/',main1),
    path('footer/',footer),
    path('exit/',exit),

    #用户管理
    path('user/',user.as_view()),
    path('useradd/',useradd.as_view()),
    path('userdel/',userdel.as_view()),
    path('useredit/',useredit.as_view()),
    #内容管理
    path('content/',content.as_view()),
    path('contentadd/',contentadd.as_view()),
    path('contentdel/',contentdel.as_view()),
    path('contentedit/',contentedit.as_view()),
    #留言管理
    path('message/',message.as_view()),
    path('messageadd/',messageadd.as_view()),
    path('messagedel/',messagedel.as_view()),
    path('messageedit/',messageedit.as_view()),
    #点赞管理
    path('zan/',zan.as_view()),
    path('zanadd/',zanadd.as_view()),  #????
    path('zandel/',zandel.as_view()),
    path('zanedit/',zanedit.as_view()),
    #分享管理
    path('share/',share.as_view()),
    path('shareadd/',shareadd.as_view()),
    path('sharedel/',sharedel.as_view()),
    path('shareedit/',shareedit.as_view()),
    #分类管理
    path('types/',types.as_view()),
    path('typeadd/',typeadd.as_view()),
    path('typedel/',typedel.as_view()),
    path('typeedit/',typeedit.as_view()),
    #收藏管理
    path('collect/',collect.as_view()),
    path('collectadd/',collectadd.as_view()),
    path('collectdel/',collectdel.as_view()),
    path('collectedit/',collectedit.as_view()),
    #广告管理
    path('rotate/',rotate.as_view()),
    path('rotateadd/',rotateadd.as_view()),
    path('rotatedel/',rotatedel.as_view()),
    path('rotateedit/',rotateedit.as_view()),
]
'''
1.登录时后台没有进行验证 
2.设置装饰器的时候无法进入到正常页面
3.用户名或者密码错误的情况下，不提示错误信息

1.内容添加的时候，没有写图片
2.广告图片无法上传
3.用户密码如何解密
4.装饰器无法被导入使用
'''
'''
1.vue 
2.获取后台数据的时候通过ajax获取
3.isscroll

'''
'''
前端vue
1.href中不加#代表向服务器发起请求
2.scoped  代表唯一
'''
