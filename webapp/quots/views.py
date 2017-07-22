# -*- coding: utf8 -*-

#from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from quots.forms import *
from django.contrib.auth import authenticate, login
from quots.models import *
#from thirdparty.coolsms import coolsms

#from fbregister import initialize
#from firebase import firebase
'''
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
'''
#db = firebase.FirebaseApplication("https://yjms-ad1e5.firebaseio.com", None)

def memdepart(types):
    interests=""
    for type in types:
        interests+=(type+"|")
    return interests

def fbput(subdir,title,key,value):
    pass
    #dest=subdir+'/'+title
    #db.put(dest,key,value)
'''
def sms(pn,usr,mode):
    # 객체 생성
    cs = coolsms.sms()

    # 프로그램명과 버젼을 입력합니다. (생략가능)
    cs.appversion("TEST/1.0")

    # 한글인코딩 방식을 설정합니다.  (생략시 euckr로 설정)
    # 지원 인코딩: euckr, utf8
    cs.charset("utf8")

    # 아이디와 패스워드를 입력합니다.
    # 쿨에스엠에스에서 회원가입시 입력한 아이디/비밀번호를 입력합니다.
    cs.setuser("cova", "abc123")

    # add("받는사람 폰번호", "보내는사람 폰번호", "문자 내용", "예약전송시간")
    # "예약전송시간"을 생략 하거나 현재 시간보다 이전시간으로 설정하면 즉시 전송 됨
    # 예약전송 표기법 : YYYYMMDDhhmmss (YYYY=년, MM=월, DD=일, hh=시, mm=분, ss=초)
    # String 으로 표기하며 ss(초)는 생략 가능

    # 즉시 전송시
    if mode=="register":
        cs.addsms(pn,"01028429981", usr+ "님 견적넷 가입을 환영합니다. 300포인트가 충전되었습니다.")
    # 예약 전송시
    # cs.addsms("01012341234", "0212341234", "80바이트 이내로 문자내용을 입력하세요. 80바이트 이후의 내용은 자동으로 잘립니다.", "YYYYMMDDhhmm")
    # cs.addsms 메소드를 계속 호출하여 메시지를 추가 할 수 있음.

    nsent = 0
    if cs.connect():
        # add 된 모든 메세지를 서버로 보냅니다.
        nsent = cs.send()
    else:
        # 오류처리
        print ("서버에 접속할 수 없습니다. 네트워크 상태를 확인하세요.")

    # 연결 해제
    cs.disconnect()

    # 결과를 출력합니다.
    print ("%d 개를 전송한 결과입니다." % nsent)
    cs.printr()

    # 메모리 초기화
    cs.emptyall()
'''
# Create your views here.
def updateInnerNum(innerobj):
    totalins=In.objects.filter(orderer=innerobj)
    innerobj.nums=len(totalins)
    innerobj.save(update_fields=["nums"])

def updateOuterNum(outerobj):
    totalouts=Out.objects.filter(handler=outerobj)
    outerobj.nums=len(totalouts)
    outerobj.save(update_fields=["nums"])

def updateInNum(inobj):
    totalouts=Out.objects.filter(parent=inobj)
    inobj.outnums=len(totalouts)
    inobj.save(update_fields=["outnums"])

def index(request):
    #initialize()
    allpr=None
    allclo=None
    allmed=None

    mypr = None
    myclo = None
    mymed = None
    if request.user.is_authenticated:
        if request.user.first_name == 'inner':
            allpr=In.objects.filter(orderer=get_object_or_404(Inner,username=request.user.username),type='pr',done=0)
            allclo=In.objects.filter(orderer=get_object_or_404(Inner,username=request.user.username),type='clo',done=0)
            allmed=In.objects.filter(orderer=get_object_or_404(Inner,username=request.user.username),type='med',done=0)
        elif request.user.first_name == 'outer':
            allpr = In.objects.filter(type='pr',done=0)
            allclo = In.objects.filter(type='clo',done=0)
            allmed = In.objects.filter(type='med',done=0)

            mypr = Out.objects.filter(handler=get_object_or_404(Outer,username=request.user.username),type='pr')
            myclo = Out.objects.filter(handler=get_object_or_404(Outer, username=request.user.username), type='clo')
            mymed = Out.objects.filter(handler=get_object_or_404(Outer, username=request.user.username), type='med')
        context = {'user': request.user, 'allpr': allpr, 'allclo': allclo, 'allmed': allmed,'mypr': mypr, 'myclo': myclo, 'mymed': mymed}
    else:
        context = {'user': request.user}
    return render(request, 'index.html', context)

def handle_uploaded_file(f,name):
    with open('static/img/'+name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def ImglistChker(imglist,request,type):
    for img in imglist:
        if img[1] is not None:
            fname = type + '/' + str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]) + '.png'
            handle_uploaded_file(request.FILES[img[0]], fname)


def inorder(request,type):
    if request.method == 'POST':
        form = inorderForm(request.POST,request.FILES)
        if form.is_valid():
            innerobj=get_object_or_404(Inner,username=request.user.username)
            inmodel = In.objects.update_or_create(orderer=innerobj,done=False,jumun=form.cleaned_data['jumun'],type=type,content=form.cleaned_data['content'],
                                            pic1=form.cleaned_data['pic1'], pic2=form.cleaned_data['pic2'],pic3=form.cleaned_data['pic3'],pic4=form.cleaned_data['pic4'],
                                            pic5=form.cleaned_data['pic5'],pic6=form.cleaned_data['pic6'])
            imglist=[['pic1',form.cleaned_data['pic1']],['pic2',form.cleaned_data['pic2']],['pic3',form.cleaned_data['pic3']],['pic4',form.cleaned_data['pic4']],['pic5',form.cleaned_data['pic5']],['pic6',form.cleaned_data['pic6']]]
            ImglistChker(imglist,request,str(type))
            updateInnerNum(innerobj)
            return HttpResponseRedirect('/')
        else:
            context={'form': form}
            return render(request,'inorder.html',context)
    form = inorderForm()
    context={'form': form}
    return render(request,'inorder.html',context)

def outorder(request,type,ordernum):
    if request.method == 'POST':
        form = outorderForm(request.POST, request.FILES)
        if form.is_valid():
            handler = get_object_or_404(Outer, username=request.user.username)
            parent = get_object_or_404(In, id=ordernum)
            outmodel = Out.objects.update_or_create(parent=parent, handler=handler, dapbyun=form.cleaned_data['dapbyun'],
                                                  type=type, content=form.cleaned_data['content'],suggest=form.cleaned_data['suggest'],
                                                  pic1=form.cleaned_data['pic1'], pic2=form.cleaned_data['pic2'],
                                                  pic3=form.cleaned_data['pic3'], pic4=form.cleaned_data['pic4'],
                                                  pic5=form.cleaned_data['pic5'], pic6=form.cleaned_data['pic6'])
            imglist = [['pic1', form.cleaned_data['pic1']], ['pic2', form.cleaned_data['pic2']],
                       ['pic3', form.cleaned_data['pic3']], ['pic4', form.cleaned_data['pic4']],
                       ['pic5', form.cleaned_data['pic5']], ['pic6', form.cleaned_data['pic6']]]
            ImglistChker(imglist, request, str(type))
            updateOuterNum(handler)
            updateInNum(parent)
            return HttpResponseRedirect('/')
        else:
            context = {'form': form}
            return render(request, 'outorder.html', context)
    form = outorderForm()
    context = {'form': form}
    return render(request, 'outorder.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            interests=memdepart(form.cleaned_data['depart'])
            if str(form.cleaned_data['memtype']) =="in":
                user = User.objects.create_user(username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password1'],
                                                email=form.cleaned_data['email'], first_name='inner',
                                                last_name=interests)
                innermodel=Inner.objects.create(username=form.cleaned_data['username'],rname=form.cleaned_data['rname'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'],phone=form.cleaned_data['phone'],type=interests,nums=0,date=user.date_joined,update=timezone.now(),newnums=0)

                fbput('inner',str(form.cleaned_data['username']),'id',str(form.cleaned_data['username']))
                fbput('inner', str(form.cleaned_data['username']), 'pw', str(form.cleaned_data['password1']))
                fbput('inner', str(form.cleaned_data['username']), 'email', str(form.cleaned_data['email']))
                fbput('inner', str(form.cleaned_data['username']), 'phone', str(form.cleaned_data['phone']))
                fbput('inner', str(form.cleaned_data['username']), 'interests', interests)
                fbput('inner', str(form.cleaned_data['username']), 'newsnum', 0)
                fbput('inner', str(form.cleaned_data['username']), 'news', '')

            elif str(form.cleaned_data['memtype']) =="out":
                user = User.objects.create_user(username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password1'],
                                                email=form.cleaned_data['email'], first_name='outer',
                                                last_name=interests)
                outermodel = Outer.objects.create(username=form.cleaned_data['username'],rname=form.cleaned_data['rname'], password=form.cleaned_data['password1'],
                                   email=form.cleaned_data['email'], phone=form.cleaned_data['phone'],
                                   type=interests, nums=0, credit=0, date=user.date_joined, update=timezone.now(), newnums=0)

                fbput('outer',str(form.cleaned_data['username']),'id',str(form.cleaned_data['username']))
                fbput('outer', str(form.cleaned_data['username']), 'pw', str(form.cleaned_data['password1']))
                fbput('outer', str(form.cleaned_data['username']), 'email', str(form.cleaned_data['email']))
                fbput('outer', str(form.cleaned_data['username']), 'phone', str(form.cleaned_data['phone']))
                fbput('outer', str(form.cleaned_data['username']), 'interests', interests)
                fbput('outer', str(form.cleaned_data['username']), 'newsnum', 0)
                fbput('outer', str(form.cleaned_data['username']), 'news', '')
            #sms(str(form.cleaned_data['phone']),(str(form.cleaned_data['username'])),"register")
            login(request,user)

            return HttpResponseRedirect('/')
        else:
            context={'form': form}
            return render(request, 'registration/register.html',context)
    form = RegistrationForm()
    context={'form': form}
    return render(request, 'registration/register.html',context)