import os
from os import path
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()
mycursor.execute("USE dbms")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt,mpld3
import matplotlib.pylab as plt1
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from getpass import getpass
import mpld3
from accounts.forms import new
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms


def admin(ae):
    lt=[]
    if(path.exists(r'D:\dbms_project\dbmsc2\static\images\0.png')):
    	os.remove(r'D:\dbms_project\dbmsc2\static\images\0.png')
    if(path.exists(r'D:\dbms_project\dbmsc2\static\images\1.png')):
    	os.remove(r'D:\dbms_project\dbmsc2\static\images\1.png')
    if(path.exists(r'D:\dbms_project\dbmsc2\static\images\2.png')):
    	os.remove(r'D:\dbms_project\dbmsc2\static\images\2.png')
    if(path.exists(r'D:\dbms_project\dbmsc2\static\images\3.png')):
    	os.remove(r'D:\dbms_project\dbmsc2\static\images\3.png')
    l=0
    l1=[]
    x=0
    for lx in range(0,4):
        ld='''drop table if exists try'''
        mycursor.execute(ld)
        ld='''create table try (year varchar(32),people int)'''
        mycursor.execute(ld)
        f=lx+1
        c='Q'+str(f)
        for l in range(0,4):
            mycursor.execute("select {} from year_201{} where states='{}'".format(c,l+4,ae))
            for db in mycursor:
            	c1='201'+str(l+4)
            	c1=int(c1)
            	ld='''insert into try values('%d','%d')'''%(c1,db[0])
            	mycursor.execute(ld)
            	mydb.commit()
        if(path.exists(r'C:\xampp\mysql\data\dbms\oneoo.csv')):
        	os.remove(r'C:\xampp\mysql\data\dbms\oneoo.csv')
        ld='''select * into outfile 'oneoo.csv' fields terminated by ',' optionally enclosed by '"' lines terminated by '\n' from dbms.try'''
        mycursor.execute(ld)
        mydb.commit()
        import pandas as pd
        	#df.to_csv('test_with_col.csv', index=False)
        read=pd.read_csv(r'C:\xampp\mysql\data\dbms\oneoo.csv',header=None)
        read.rename(columns={0: 'year', 1: 'people'}, inplace=True)
        print(read.head())
        ax=sns.lmplot(x="year",y="people",data=read)
        x=read[['year']]
        y=read['people']
        plt.savefig('D:\dbms_project\dbmsc2\static\images\{}.png'.format(lx))
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1,random_state=101)
        lm=LinearRegression()
        lm.fit(x_train,y_train)
        pr=lm.predict([[2018]])
        lt=lt+[int(pr[0])]
    return(lt)


    # Create your views here.




class Signup(CreateView):
    form_class=forms.usercreateform
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'


def other(request):
    return render(request,'other.html')

def relurl(request):
    return render(request,'relurl.html')

def one(request):
    return render(request,'one.html')

def test(request):
    return render(request,'accounts/test.html')

def thanks(request):
    return render(request,'accounts/thanks.html')

def bihar(request):
    t=admin('bihar')
    print(t)
    return render(request,'accounts/bihar.html',{'POP':t[0],'POP1':t[1],'POP2':t[2],'POP3':t[3]})

def up(request):
    t=admin('up')
    print(t)
    return render(request,'accounts/up.html',{'POP':t[0],'POP1':t[1],'POP2':t[2],'POP3':t[3]})

def jammukashmir(request):
    t=admin('jammukashmir')
    print(t)
    return render(request,'accounts/jammukashmir.html',{'POP':t[0],'POP1':t[1],'POP2':t[2],'POP3':t[3]})


def karnataka(request):
    t=admin('karnataka')
    print(t)
    return render(request,'accounts/karnataka.html',{'POP':t[0],'POP1':t[1],'POP2':t[2],'POP3':t[3]})

def tamilnadu(request):
    t=admin('tamilnadu')
    print(t)
    return render(request,'accounts/karnataka.html',{'POP':t[0],'POP1':t[1],'POP2':t[2],'POP3':t[3]})


def home(request):
    return render(request, 'accounts/home.html')

def new_page(request):
    data = request.GET['fulltextarea']
    return render(request, 'accounts/newpage.html', {'data':data})

def users(request):
    form=new()
    if request.method=="POST":
        form=new(request.POST)
        form.save(commit=True)
        return render(request,'accounts/tamilnadu.html')
    return render(request,'accounts/users.html',{'form':form})
