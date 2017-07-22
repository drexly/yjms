#-*- coding: utf-8 -*-
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from quots.models import *
class inorderForm(forms.Form):
    jumun = forms.CharField(label=u'주문명',min_length=1, max_length=200,help_text=("주문하실 상품의 명칭 혹은 제목을 입력해주세요"))  # 주문명
    many=forms.IntegerField(label=u'수량',initial=1,help_text=("주문하실 상품의 수량을 입력해주세요"))  # 주문수량
    tags = forms.CharField(label=u'태그', max_length=300,help_text=("#팜플렛#광고지 처럼 띄어쓰기를 하지 마시고 #을 붙여 구분해주세요"),required=False)  # 상품태그
    content = forms.CharField(label=u'내용',min_length=1,widget=forms.Textarea, max_length=200,help_text=("주문하실 상품의 상세 상품내역을 입력하세요"))  # 주문개인내역
    pic1 = forms.ImageField(label=u'사진1', max_length=200,help_text=("사진첨부는 선택사항입니다"),required=False)  # 주문개인내역
    pic2 = forms.ImageField(label=u'사진2', max_length=200,help_text=("사진첨부는 선택사항입니다"),required=False)  # 주문개인내역
    pic3 = forms.ImageField(label=u'사진3', max_length=200,help_text=("사진첨부는 선택사항입니다"),required=False)  # 주문개인내역
    pic4 = forms.ImageField(label=u'사진4', max_length=200,help_text=("사진첨부는 선택사항입니다"),required=False)  # 주문개인내역
    pic5 = forms.ImageField(label=u'사진5', max_length=200,help_text=("사진첨부는 선택사항입니다"),required=False)  # 주문개인내역
    pic6 = forms.ImageField(label=u'사진6', max_length=200,help_text=("사진첨부는 선택사항입니다"),required=False)  # 주문개인내역
    def clean_tags(self):
        tagall=self.cleaned_data['tags']
        if str(tagall).__contains__('#'):
            return tagall
        else:
            raise forms.ValidationError('#을 태그 앞에 입력하셔야합니다.')


class outorderForm(forms.Form):
    dapbyun = forms.CharField(label=u'답변명',min_length=1, max_length=200,help_text=("구매자의 요구에 맞는 응찰 제목을 입력해주세요"))  # 답변명
    suggest = forms.IntegerField(label=u'제시가',initial=0,help_text=("구매자가 만족할 만한 응찰가를 숫자만으로 입력해주세요"))  # 제시가
    content = forms.CharField(label=u'내용',min_length=1, max_length=200,widget=forms.Textarea,help_text=("구매자의 요구에 맞는 응찰 상세를 입력해주세요"))  # 응찰상세내역
    pic1 = forms.ImageField(label=u'사진1', max_length=200,help_text=("사진첨부는 선택사항입니다"),required=False)  # 응찰상세내역
    pic2 = forms.ImageField(label=u'사진2', max_length=200,help_text=("사진첨부는 선택사항입니다"),required=False)  # 응찰상세내역
    pic3 = forms.ImageField(label=u'사진3', max_length=200,help_text=("사진첨부는 선택사항입니다"),required=False)  # 응찰상세내역
    pic4 = forms.ImageField(label=u'사진4', max_length=200,help_text=("사진첨부는 선택사항입니다"),required=False)  # 응찰상세내역
    pic5 = forms.ImageField(label=u'사진5', max_length=200,help_text=("사진첨부는 선택사항입니다"),required=False)  # 응찰상세내역
    pic6 = forms.ImageField(label=u'사진6', max_length=200,help_text=("사진첨부는 선택사항입니다"),required=False)  # 응찰상세내역



class RegistrationForm(forms.Form):
    acctype = [('in', u'입찰자'),
               ('out', u'응찰자')]
    interest=[('pr', u'판촉물'),
               ('med', u'의료기기'),
               ('clo', u'의류'),]

    memtype = forms.ChoiceField(label='회원종류' ,choices=acctype, widget=forms.RadioSelect())

    depart = forms.MultipleChoiceField(label='관심분야(복수가능)', choices=interest,widget=forms.CheckboxSelectMultiple)

    username = forms.CharField(label='사용자 이름(ID)',min_length=8, max_length=30,help_text=("8~30자의 쉽지 않은 영문+숫자 조합입니다"))
    rname = forms.CharField(label='예금주(실명)', min_length=2, max_length=4, help_text=("2~4자의 한글실명입니다."))
    email = forms.EmailField(label='이메일',help_text=('회원정보 수정시 필요한 이메일 주소입니다.'))
    password1 = forms.CharField(label='비밀번호(PW)',widget=forms.PasswordInput(),help_text=("8~30자 입니다."),min_length=8,max_length=30)
    password2 = forms.CharField(label='비밀번호 재입력',widget=forms.PasswordInput())
    phone = forms.CharField(
        label=u'휴대전화',
        help_text=('01X-YYYY-ZZZZ 형식으로 숫자와 하이픈으로만 기입하세요.'),
    )
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'[가-힣]+', username):
            raise forms.ValidationError('아이디에 잘못된 문자가 들어가 있습니다. 한글 불가 합니다.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('이미 등록된 이름입니다. 다른 이름을 쓰세요')

    def clean_phone(self):
        phraw=self.cleaned_data['phone']
        if not str(phraw).__contains__('-'):
            raise forms.ValidationError('휴대전화번호에 하이픈이 없습니다.-로 구분해주세요.')
        else:
            comp=str(phraw).split('-')
            if len(comp) is not 3:
                raise forms.ValidationError('올바른 휴대전화번호 형식이 아닙니다.')
            else:
                for num in comp:
                    try:
                        int(num)
                    except:
                        raise forms.ValidationError('휴대전화번호에 문자가 있습니다.')
            try:
                Outer.objects.get(phone=phraw)
            except ObjectDoesNotExist:
                return phraw
            raise forms.ValidationError('이미 등록된 업체의 휴대전화번호입니다. 다른 번호를 기입하하세요')
    def clean_rname(self):
        nameraw=self.cleaned_data['rname']
        if re.search(r'^[A-Za-z0-9_-]*$', nameraw):
            raise forms.ValidationError('예금주는 순한글로만 입력하셔야 합니다.')
        else:
            return nameraw

