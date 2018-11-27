from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# from models import StudentInfo,AlumniInfo,StaffInfo,Gift,user
from . import models
from django.contrib import auth
# import django_socketio
from .forms import StaffInfo_form,AlumniInfo_form,StudentInfo_form
import sqlite3
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

state=['Andaman and Nicobar (UT)','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu &amp; Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Punjab','Rajasthan','Sikkim','Tamil Nadu','Tripura','Uttar Pradesh','Uttarakhand','West Bengal','Delhi','Andhra Pradesh','Chandigarh (UT)','Dadra and Nagar Haveli (UT)','Daman and Diu (UT)','Lakshadweep (UT)','Pondicherry (UT)','Telangana','Others']
# Create your views here.
def Welcome(request): #This is Simple Start Welcome Page.........
    return HttpResponseRedirect('/Home')
    return render(request,"Welcome.html",{})
def LAuth(request,color,statement1,statement2='',iitbhu='AccessPage'):  #This is informative page for Redirect...........
    if request.user.id:
        return render(request,"LoginAuth.html",{'creg':'blue','hreg':'','reg':'Welcome, '+request.user.first_name,'log':'LOGOUT','color':color,'statement1':statement1,'statement2':statement2,'iitbhu':iitbhu})
    else:
        return render(request,"LoginAuth.html",{'creg':'22bb22','hreg':'../Register/','reg':'REGISTRATION','log':'LOGIN','color':color,'statement1':statement1,'statement2':statement2,'iitbhu':iitbhu})  
def Handle_Pages(request,PageName,title,shade):  #it Handel All Pages.....
    if request.user.id:
        return render(request,PageName,{'creg':'blue','hreg':'','reg':'Welcome, '+request.user.first_name,'log':'LOGOUT','iitbhu':title,shade:'homet'})
    else:
        return render(request,PageName,{'creg':'22bb22','hreg':'../Register/','reg':'REGISTRATION','log':'LOGIN','iitbhu':title,shade:'homet'})
def Home(request):
    return Handle_Pages(request,"Home.html",'IIT (BHU) VARANASI ALUMNI','home')       
def Reunion(request):
    if request.method=='POST':
        return Sendmail(request)    
    return Handle_Pages(request,"reunion.html","IIT (BHU) Varanasi- ALUMNI REUNION",'reunion')  
def Gallery(request):
    return Handle_Pages(request,"Gallery.html",'IIT (BHU) Varanasi- Gallery','gallery')
def AlumniMeet(request):
    return Handle_Pages(request,"alumnimeet.html",'IIT (BHU) Varanasi- ALUMNI MEET','meet')
def Sendmail(request):
    if request.method=='POST':
        sender    = 'anuj69984@gmail.com'
        password  = 'Anuj@196'
        receiever = ['anuj.kumar.cse15@itbhu.ac.in','arun.krpaswan.cse15@itbhu.ac.in']
        
        message            = MIMEMultipart('alternative')
        message['Form']    = sender
        message['To']      = str(receiever)
        message['Subject'] = request.POST.get('Subject','')
        text  = """%s\n\nDate Of Reunion : %s \nVENUE%s\n%s\n%s\n%s"""%(request.POST.get('Message',''),request.POST.get('DOR',''),request.POST.get('Addr1',''),request.POST.get('Addr2',''),request.POST.get('State',''),request.POST.get('Country','India'))
        html = """
        <html>
        <head></head>
        <body>
            %s<br/><br/>
            <b>Date Of Reunion : %s</b><br/> 
            <h2>VENUE</h2>
            %s<br/>
            %s<br/>
            %s<br/>
            %s
        </body>
        </head>
        """%(request.POST.get('Message','').replace('\n','<br/>'),request.POST.get('DOR',''),request.POST.get('Addr1',''),request.POST.get('Addr2',''),request.POST.get('State',''),request.POST.get('Country','India'))
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        message.attach(part1)
        message.attach(part2)
    
        try:
            ser=smtplib.SMTP('smtp.gmail.com',587)
            ser.ehlo()
            ser.starttls()
            ser.login(sender,password)
            ser.sendmail(sender,receiever,message.as_string())
            ser.quit()   
        except Exception as ex:
            print(ex)
            return LAuth(request,'red','Sorry Unable To Send Mail Now Check Internet Connection...','Please Try to Search Again....')
    else:
        return LAuth(request,'red','Sorry Unable To Send Mail Now Check Internet Connection...','Please Try to Search Again....')
    return LAuth(request,'green','Message Sent Successfully','Back To Home')

def AlumniProfile(request):
    try:
        data=models.AlumniInfo.objects.filter(First_Name=request.POST.get('searchbox').lower(),Passout_Year=request.POST.get('batch'),Department=request.POST.get('branch'))[0]
    except:
        return LAuth(request,'red','This Alumni Does not exist !','Search Again....')
    return render(request,'Profiles.html',{'data':data})
def ContactUs(request):
    return Handle_Pages(request,"contact us.html",'IIT (BHU) Varanasi- Contact Administrator','contact')  
def Register(request):
    return Handle_Pages(request,"Register.html",'IIT(BHU) Varanasi Registration','register')
'''def RegisterData(request,formField,users):
    data=[]
    if request.method == 'POST':
        usertype={'alumni':AlumniInfo,'staff':StaffInfo,'student':StudentInfo}[users]
        for name in formField:
            data.append(request.POST.get(name,''))
        usertype=user(EnrollmentNumber=int(data[0]),Campus=data[1],Department=data[2],Program=data[3],PassoutYear=int(data[4]),Fname=data[5],Lname=data[6],Gender=data[7],MartialStatus=data[8],DOB=data[9],Mob=int(data[10]),EmailId=data[11],CurrentStatus=data[12],Address=data[13]+'\n'+data[14],State=state[int(data[15])-1],Country=data[16],PinCode=int(data[17]),Organization=data[19],Designation=data[20])
        try: #Register Use in auth table............
                newuser=auth.models.User.objects.create_user(data[11],data[11],data[18])
                newuser.first_name=data[5]
                newuser.last_name='alumni'
                newuser.save()
        except:
            return LAuth(request,'red','This Email_Id Alrady Exist','Please Try Register As Another Email_Id')
        AI.save()
        AlumniLogin(info=AI,Username1=data[11],Username2=int(data[0])).save()
        return LAuth(request,'green','Welcome '+data[5]+' '+data[6],'You Are Registerd Successfuly')
    return render(request,"RegisterAlumni.html",{'iitbhu':'IIT(BHU) Varanasi Registration'})
def RAlumni(request):
    data=[]
    if request.method == 'POST':
        form=['EnrollmentNo','Campus','Department','Program','PassOutYear','Fname','Lname','sex','Marital','DOB','Mobile','Email','Status','Addr1','Addr2','State','Country','PinCode','Password','Organisation','Designation']
        for name in form:   
            data.append(request.POST.get(name,''))
        #save data into Alumni Info Table.........
        AI=AlumniInfo(EnrollmentNumber=int(data[0]),Campus=data[1],Department=data[2],Program=data[3],PassoutYear=int(data[4]),Fname=data[5],Lname=data[6],Gender=data[7],MartialStatus=data[8],DOB=data[9],Mob=int(data[10]),EmailId=data[11],CurrentStatus=data[12],Address=data[13]+'\n'+data[14],State=state[int(data[15])-1],Country=data[16],PinCode=int(data[17]),Organization=data[19],Designation=data[20])
        try: #Register Use in auth table............
            newuser=auth.models.User.objects.create_user(data[11],data[11],data[18])
            newuser.first_name=data[5]
            newuser.last_name='alumni'
            newuser.save()
        except:
            return LAuth(request,'red','This Email_Id Alrady Exist','Please Try Register As Another Email_Id')
        AI.save()
        AlumniLogin(info=AI,Username1=data[11],Username2=int(data[0])).save()
        return LAuth(request,'green','Welcome '+data[5]+' '+data[6],'You Are Registerd Successfuly')
    return render(request,"RegisterAlumni.html",{'iitbhu':'IIT(BHU) Varanasi Registration'})
'''
def RAll(request,user):
    forms={'alumni':AlumniInfo_form,'staff':StaffInfo_form,'student':StudentInfo_form}
    if request.method == 'POST':
        form=forms[user](data=request.POST)
        print('Getting form .............!')
        if form.is_valid():
            print('Saving ----------------- ',user)
            form.save()
            print('Saved ----------------- ',user)
            try:
                #StaffLogin(info=form,Username=request.POST.get('Email_Id')).save()
                newuser=auth.models.User.objects.create_user(request.POST.get('Email_Id'),request.POST.get('Email_Id'),request.POST.get('Password'))
                newuser.first_name=request.POST.get('First_Name')
                newuser.last_name=user
                newuser.save()
                models.user.objects.create(user=newuser)
            except:
                return LAuth(request,'red','This Email_Id Alrady Exist','Please Try Register As Another Email_Id')            
        return LAuth(request,'green','Welcome '+request.POST.get('First_Name')+' '+request.POST.get('Last_Name'),'Registered As : ' + user)
    form=forms[user]()
    # print(form)
    return render(request,'RegisterAll.html',{'form':form,'iitbhu':'IIT(BHU) Varanasi Registration','formname':user.capitalize()+' Registration form'})

def RAlumni(request):
    return RAll(request,'alumni')
def RStaff(request):
    return RAll(request,'staff')
def RStudent(request):
    return RAll(request,'student')

'''
def RStudent1(request):
    data=[]
    if request.method == 'POST':
        form=['EnrollmentNo','Campus','Department','Program','YearofJoin','Fname','Lname','sex','Marital','DOB','Mobile','Email','Status','Addr1','Addr2','State','Country','PinCode','Password']
        for name in form:
            data.append(request.POST.get(name,''))
        #save data into Student Info Table.........
        SI=StudentInfo(EnrollmentNumber=int(data[0]),Campus=data[1],Department=data[2],Program=data[3],YearofJoin=int(data[4]),Fname=data[5],Lname=data[6],Gender=data[7],MartialStatus=data[8],DOB=data[9],Mob=int(data[10]),EmailId=data[11],CurrentStatus=data[12],Address=data[13]+'\n'+data[14],State=state[int(data[15])-1],Country=data[16],PinCode=int(data[17]))
        try: #Register Use in auth table............
            newuser=auth.models.User.objects.create_user(data[11],data[11],data[18])
            newuser.first_name=data[5]
            newuser.last_name='student'
            newuser.save()
        except:
            return LAuth(request,'red','This Email_Id Alrady Exist','Please Try Register As Another Email_Id')
        SI.save()
        StudentLogin(info=SI,Username1=data[11],Username2=int(data[0])).save()
        return LAuth(request,'green','Welcome '+data[5]+' '+data[6],'You Are Registerd Successfuly')
    return render(request,"RegisterStudent.html",{'iitbhu':'IIT(BHU) Varanasi Registration'})
'''
def Login(request):
    if request.user.id:
        auth.logout(request)
        return HttpResponseRedirect('../Home/')
    data=[]
    if request.method == 'POST':
        usertype={"alumni":models.AlumniInfo,"staff":models.StaffInfo,"student":models.StudentInfo}
        user=request.POST.get('user')

        try:
            user=usertype[request.POST.get('usertype')].objects.filter(Enrollment_Number=int(user))[0].Email_Id
        except Exception as error:
            print(error)
            pass
        usr=auth.authenticate(username=user,password=request.POST.get('pswd'))
        if usr is not None:
            if usr.last_name == request.POST.get('usertype'):
                auth.login(request,usr)
        else:
            return HttpResponse('Please Enter Correct Username and Password...')
        try:
            return LAuth(request,'green','Welcome, '+request.user.first_name,'Login As : '+request.POST.get('usertype'))
        except:
            return  HttpResponse('Please Enter Correct User Type...')       
    return render(request,"Login.html",{})
def RegisteredAlumni(request):
    if request.method=='POST':
        return AlumniProfile(request)
    return render(request,"RegisteredAlumni.html",{})
def Notifications(request):
    if request.user.id:
        return render(request,"News.html",{'creg':'blue','hreg':'','reg':'Welcome, '+request.user.first_name,'log':'LOGOUT','iitbhu':'IIT (BHU) Varanasi- News And Notifications'})
    else:
        return LAuth(request,'red','Unauthourised Access','Please Try Login To Access This Page...','IIT (BHU) Varanasi News And Notifications')
def Association(request):
    return HttpResponse("Page Under Construction.......!")
def UpcomingEvents(request):
    return render(request,"header.html",{})
def MakeAGift(request):
    if request.method == 'POST':
        models.Gift.objects.create(Name = str(request.POST.get('firstname')) + str(request.POST.get('middlename')) + str(request.POST.get('lastname')),
                            Relation=request.POST.get('relation'),
                            Designation=request.POST.get('designation'),
                            Address=str(request.POST.get('address'))+'state: '+str(request.POST.get('state')),
                            Email=request.POST.get('email'),
                            Money=request.POST.get('money'),
                            Contact=request.POST.get('contact'))
        return HttpResponse('Gift make Successful !<br><a href="/">Home</a>')
    if request.method=='GET' and request.GET.get('data')=='true':
        data = '<table width="100%">'
        for d in models.Gift.objects.all():
            data += '<tr><td style="background:red;"></td><td style="background:red;"></td></tr>'
            data += '<tr><td>Name</td><td>'+d.Name+'</td></tr>'
            data += '<tr><td>Relation</td><td>'+d.Relation+'</td></tr>'
            data += '<tr><td>Email</td><td>'+d.Email+'</td></tr>'
            data += '<tr><td>Contact</td><td>'+d.Contact+'</td></tr>'
            # data += '<tr><td>Money</td><td>'+d.Money+'</td></tr>'

        data += '</table>'
        return HttpResponse(data)  
    if request.user.id:
        return render(request,"makeagift.html",{'creg':'blue','hreg':'','reg':'Welcome, '+request.user.first_name,'log':'LOGOUT'})
    else:
        return LAuth(request,'red','Unauthourised Access','Please Try Login To Access This Page...')  
def OtherLinks(request):
    return Handle_Pages(request,"OtherLinks.html","IIT (BHU) Varanasi-OtherLinks",'')

def chat(request):
    Info={"alumni":models.AlumniInfo,"staff":models.StaffInfo,"student":models.StudentInfo}
    # db=sqlite3.connect('Home/chat.db')
    # cursor=db.cursor()
    # cursor.execute("""select * from chat""")
    # chatdata=cursor.fetchall()
    # db.close()
    if request.user.id:
        user = models.user.objects.filter(user=request.user).first()
        if not user:
            user = models.user.objects.create(user=request.user)
        chatdata = models.chat.objects.exclude(deleted_chats = user)
        try:
            Info=Info[request.user.last_name].objects.filter(Email_Id=request.user.username)[0]
            return render(request,"chat.html",{'loginuser':Info.First_Name+' '+Info.Last_Name,'chatdata':chatdata})
        except:
            return LAuth(request,'red','Only Student, Staff and alumni can access this chat')
    else:
        return LAuth(request,'red','Unauthourised Access')
        

def delete_chat(request):
    if request.method == 'POST' and request.user.is_authenticated():
        user = models.user.objects.filter(user=request.user).first()
        if not user:
            user = models.user.objects.create(user=request.user)
        chat = models.chat.objects.filter(id=request.POST.get('chatid')).first() 
        if chat:    
            user.deleted_chat.add(chat)
        return HttpResponse('Access')
    return HttpResponse('Not Allowed !')
