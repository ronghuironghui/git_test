from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def login(request):
    #request包含了用户提交的所有的信息
    # print(request.method)
    error_msg = ''
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)

        if user == 'root' and pwd == '123':
            #跳转就是return 重定向redirect
            return redirect('http://www.baidu.com')
        else:
            #用户名密码不匹配
            error_msg = '用户名或密码错误'

    return render(request,'login.html',{'error_msg':error_msg})

USER_LIST = [
    { 'username': 'alex', 'email': 'asdfasdf', "gender": '男'},
    { 'username': 'eriuc', 'email': 'asdfasdf', "gender": '男'},
    {'username': 'seven', 'email': 'asdfasdf', "gender": '男'},
]
# for index in range(20):
#     temp={'username':'alex'+str(index),'email':'alex@163.com','gender':'男'}
#     USER_LIST.append(temp)

def home(request):
    if request.method == "POST":
        u = request.POST.get('username')
        e = request.POST.get('email')
        g = request.POST.get('gender')
        temp = {'username':u,'email':e,'gender':g}
        USER_LIST.append(temp)
    return render(request,'home.html',{'user_list':USER_LIST})
