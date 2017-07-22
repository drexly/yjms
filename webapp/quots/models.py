#-*- coding: utf-8 -*-
# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import datetime
from django.db import models
from django.utils import timezone


class Inner(models.Model):
    username = models.CharField(u'아이디',  max_length=30,default='null')
    rname = models.CharField(u'예금주(실명)', max_length=4, default='null')
    email = models.EmailField(u'이메일',default='devestack@gmail.com')
    password = models.CharField(u'비밀번호',max_length=30,default='null')
    phone = models.CharField(u'휴대전화',max_length=30,default='null')
    type=models.CharField(u'분류',max_length=200)#분류
    nums=models.IntegerField(u'제시수',default=0)#작성글수

    date=models.DateTimeField(u'가입날짜' ,default=timezone.now)#등록날짜
    update = models.DateTimeField(u'로그인날짜', default=timezone.now)  # 최종업데이트 날짜
    newnums = models.IntegerField(u'업데이트수',default=0)  # 업데이트 개수
    def __str__(self):
        return self.username
    '''
    def delete(self, using=None, keep_parents=False):
        ins=In.objects.filter(orderer=self)
        if ins:
            for i in ins:
                i.delete()
        self.delete()
    '''

class Outer(models.Model):
    username = models.CharField(u'아이디',  max_length=30,default='null')
    rname = models.CharField(u'예금주(실명)', max_length=4, default='null')
    email = models.EmailField(u'이메일',default='devestack@gmail.com')
    password = models.CharField(u'비밀번호',max_length=30,default='null')
    phone = models.CharField(u'휴대전화',max_length=30,default='null')
    type=models.CharField(u'분류',max_length=200)#분류
    nums=models.IntegerField(u'응찰수',default=0)#작성글수

    credit=models.IntegerField(u'적립금',default=0)#크레딧

    date=models.DateTimeField(u'가입날짜' ,default=timezone.now)#등록날짜
    update = models.DateTimeField(u'로그인날짜', default=timezone.now)  # 최종업데이트 날짜
    newnums = models.IntegerField(u'업데이트수',default=0)  # 업데이트 개수
    def __str__(self):
        return self.username

class In(models.Model):
    orderer = models.ForeignKey(Inner,default=None,null=True,blank=True,on_delete=models.CASCADE)#외부키-주문자
    jumun= models.CharField(u'주문명',max_length=200)#주문명
    type = models.CharField(u'분류',max_length=200)#주문타입

    outnums = models.IntegerField(u'응찰수',default=0)  # 응찰건수

    #answered = models.CharField(max_length=200)#결정된 응찰자

    answered= models.ForeignKey(Outer,default=None,null=True,blank=True,on_delete=models.CASCADE) #외부키-결정된 응찰자
    setprice=models.IntegerField(u'낙찰가',default=0)#결정된 낙찰가격

    reg_date=models.DateTimeField('등록날짜' ,default=timezone.now)#등록날짜
    ans_date = models.DateTimeField('낙찰날짜', default=timezone.now)  # 낙찰날짜

    content = models.CharField(u'내용',max_length=200)  # 주문개인내역

    tags = models.CharField(u'태그',max_length=300)  # 상품태그
    many = models.IntegerField(u'수량', default=1)  # 상품수량io

    pic1 = models.ImageField(u'사진1',max_length=200)  # 주문개인내역
    pic2 = models.ImageField(u'사진2',max_length=200)  # 주문개인내역
    pic3 = models.ImageField(u'사진3',max_length=200)  # 주문개인내역
    pic4 = models.ImageField(u'사진4',max_length=200)  # 주문개인내역
    pic5 = models.ImageField(u'사진5',max_length=200)  # 주문개인내역
    pic6 = models.ImageField(u'사진6',max_length=200)  # 주문개인내역
    done = models.BooleanField(u'거래완료',default=False)  # 본 거래 완료 여부
    def __str__(self):
        return self.jumun

class Out(models.Model):
    parent = models.ForeignKey(In,default=None,null=True,blank=True,on_delete=models.CASCADE)#외부키-주문모델
    dapbyun = models.CharField(u'답변명',max_length=200)  # 답변명
    #handler = models.CharField(max_length=200)  # 응찰자
    handler = models.ForeignKey(Outer,null=True,blank=True,on_delete=models.CASCADE)#외부키-응찰자
    type = models.CharField(u'분류',max_length=200)#주문타입

    inflag = models.BooleanField(u'채택여부',default=False)  # 본 답별낙찰여부
    suggest=models.IntegerField(u'제시가',default=0)#제시가

    reg_date = models.DateTimeField('등록날짜', default=timezone.now)  # 등록날짜
    ans_date = models.DateTimeField('낙찰날짜', default=timezone.now)  # 낙찰날짜

    content = models.CharField(u'내용',max_length=200)  # 응찰상세내역

    pic1 = models.ImageField(u'사진1',max_length=200)  # 응찰상세내역
    pic2 = models.ImageField(u'사진2',max_length=200)  # 응찰상세내역
    pic3 = models.ImageField(u'사진3',max_length=200)  # 응찰상세내역
    pic4 = models.ImageField(u'사진4',max_length=200)  # 응찰상세내역
    pic5 = models.ImageField(u'사진5',max_length=200)  # 응찰상세내역
    pic6 = models.ImageField(u'사진6',max_length=200)  # 응찰상세내역
    def __str__(self):
        return self.dapbyun