# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

class pplCommon:
    list_filter = ['username', 'rname', 'type', 'nums','update', 'date']
    search_fields = ['username', 'rname', 'type', 'nums', 'phone', 'email', 'update', 'date']

class innerAdmin(admin.ModelAdmin,pplCommon):
    fieldsets = [('아이디',{'fields':['username']}),('실명',{'fields':['rname']}),('분류',{'fields':['type']}),('제시수',{'fields':['nums']}),('휴대전화',{'fields':['phone']}),('이메일',{'fields':['email']}),('마지막로긴',{'fields':['update']}),('가입날짜',{'fields':['date']})]
    list_display = ['username','rname','type','nums','phone','email','update','date']

class outerAdmin(admin.ModelAdmin,pplCommon):
    fieldsets = [('아이디',{'fields':['username']}),('실명',{'fields':['rname']}),('분류',{'fields':['type']}),('응찰수',{'fields':['nums']}),('휴대전화',{'fields':['phone']}),('이메일',{'fields':['email']}),('적립금',{'fields':['credit']}),('마지막로긴',{'fields':['update']}),('가입날짜',{'fields':['date']})]
    list_display = ['username', 'rname', 'type', 'nums', 'phone', 'email','credit', 'update', 'date']
    list_filter = ['username', 'rname', 'type', 'nums','credit','update', 'date']

class inAdmin(admin.ModelAdmin):
    fieldsets=[('주문명',{'fields':['jumun']}),('주문자',{'fields':['orderer']}),('분류',{'fields':['type']}),('태그',{'fields':['tags']}),('응찰수',{'fields':['outnums']}),('낙찰자',{'fields':['answered']}),('낙찰가',{'fields':['setprice']}),('등록날짜',{'fields':['reg_date']}),('낙찰날짜',{'fields':['ans_date']}),('내용',{'fields':['content']}),('사진1',{'fields':['pic1']}),('사진2',{'fields':['pic2']}),('사진3',{'fields':['pic3']}),('사진4',{'fields':['pic4']}),('사진5',{'fields':['pic5']}),('사진6',{'fields':['pic6']})]
    list_display = ['jumun','orderer','type','tags','outnums','answered','setprice','reg_date','ans_date','content','pic1','pic2','pic3','pic4','pic5','pic6']
    list_filter = ['jumun', 'orderer', 'type','tags','outnums', 'answered', 'setprice', 'reg_date', 'ans_date']
    search_fields = ['jumun', 'orderer', 'type', 'tags', 'outnums', 'answered', 'setprice', 'reg_date', 'ans_date']

class outAdmin(admin.ModelAdmin):
    fieldsets=[('답변명',{'fields':['dapbyun']}),('주문모델',{'fields':['parent']}),('응찰자',{'fields':['handler']}),('제시가',{'fields':['suggest']}),('채택여부',{'fields':['inflag']}),('등록날짜',{'fields':['reg_date']}),('낙찰날짜',{'fields':['ans_date']}),('내용',{'fields':['content']}),('사진1',{'fields':['pic1']}),('사진2',{'fields':['pic2']}),('사진3',{'fields':['pic3']}),('사진4',{'fields':['pic4']}),('사진5',{'fields':['pic5']}),('사진6',{'fields':['pic6']})]
    list_display = ['dapbyun','parent','handler','suggest','inflag','reg_date','ans_date','content','pic1','pic2','pic3','pic4','pic5','pic6']
    list_filter = ['dapbyun', 'parent', 'handler','suggest','inflag', 'reg_date', 'ans_date']
    search_fields = ['dapbyun', 'parent', 'handler', 'suggest','content', 'inflag', 'reg_date', 'ans_date']

admin.site.register(In,inAdmin)
admin.site.register(Inner,innerAdmin)
admin.site.register(Out,outAdmin)
admin.site.register(Outer,outerAdmin)



