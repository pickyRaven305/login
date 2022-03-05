from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Permission,Group
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from home.models import Feedback,Students,Staff,Courses,Subjects
from datetime import datetime
from django.contrib.auth.decorators import permission_required


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')
    
def loginUser(request):
    #print(request.method == "POST")
    if (request.method == "POST"):
        #to check credentials
        username = request.POST.get("username")
        password = request.POST.get("password")
        remeber_me = request.POST.get("rememberMe",'')
        #print(remeber_me)
        
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            if not remeber_me:
                request.session.set_expiry(0)
                
            login(request,user)
            return redirect("/")
        else:
            
            if ((User.objects.filter(username=username).exists() == False) ):
                messages.error(request, "please provide correct credentials!!")
                return render(request, 'login.html')
                
            if not (username or password):
                messages.error(request, "please provide all credentials!!")
                return render(request, 'login.html')
             
           
    
    return render(request, 'login.html')
 
def logoutUser(request):
    logout(request)
    return redirect("/login")

def feedback(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            desc = request.POST.get('desc') 

            feedback = Feedback(name = name, email=email, phone=phone, desc= desc, date = datetime.today())
            messages.success(request,"Thank you for providing your valuable feedback")
            feedback.save()
        return render(request, 'feedback.html')
    else:
        return render(request, 'login.html')
    
  
def studentRegisteration(request):
    #pass for 123.abc.com is 123456@abcd
    try:
        if request.user.is_authenticated:
                #print(request.method =="POST")
            if request.method =='POST':
               firstName = request.POST.get('firstname')
               lastName = request.POST.get('lastname')
               email = request.POST.get('email')
               password = request.POST.get('password')
               C_password = request.POST.get('C_password')
               address1  = str(request.POST.get('address1'))
               address2  = str(request.POST.get('address2'))
               city  = str(request.POST.get('city'))
               state  = str(request.POST.get('state'))
               zipcode  = str(request.POST.get('zipcode'))
               address = (address1 +', '+address2 + ', ' +city + ', ' + state + ', ' + zipcode)

               student = Students(firstName=firstName,lastName=lastName,email=email,password=password,address= address,)
               if(firstName and lastName and email and password and C_password and address):
                    if(password == C_password):    
                        user = User.objects.create_user(username = email,password = password,date_joined = datetime.today(),first_name = firstName,last_name = lastName,email = email)

                        if(User.objects.get(email=email) == True):
                            messages.error(
            request, 'User with this email id already exists. Please proceed to login!!')    

                        else:
                            student.save()
                            user.save()
                            messages.success(request,"Student regsistered sucessfully")
                            user = User.objects.get(username=email)
                            permission = Permission.objects.get(codename='Student')
                            user.user_permissions.add(permission)    
                                                   


                            #User

                        return render(request, 'studentReg.html')
                    else:
                        messages.error(request,"diffrent passwords entered")

               else:
                    messages.error(request,"Please providing all the information")

            else:
                return render(request, 'studentReg.html')

        return render(request, 'studentReg.html')
    except:
        messages.error(request,"Soem error occured!!")
        return render(request, 'studentReg.html')
        

def staffRegisteration(request):
    try:
         #pass for 123.abc.com is 123456@abcd
        if request.user.is_authenticated:
            #print(request.method =="POST")
            if request.method =='POST':
               firstName = request.POST.get('firstname')
               lastName = request.POST.get('lastname')
               email = request.POST.get('email')
               password = request.POST.get('password')
               C_password = request.POST.get('C_password')
               address1  = str(request.POST.get('address1'))
               address2  = str(request.POST.get('address2'))
               city  = str(request.POST.get('city'))
               state  = str(request.POST.get('state'))
               zipcode  = str(request.POST.get('zipcode'))
               address = (address1 +', '+address2 + ', ' +city + ', ' + state + ', ' + zipcode)

               staff = Staff(firstName=firstName,lastName=lastName,email=email,password=password,address= address)

               if(firstName and lastName and email and password and C_password and address):
                   
                    if(password == C_password):
                        user = User.objects.create_user(username = email,password = password,date_joined = datetime.today(),first_name = firstName,last_name = lastName,email = email)
                        
                        if(User.objects.get(email=email) == True):
                            
                            messages.error(
            request, 'User with this email id already exists. Please proceed to login!!')    

                        else:
                            staff.save()
                            user.save()
                            user = User.objects.get(username=email)
                            permission = Permission.objects.get(codename='Staff')
                            user.user_permissions.add(permission)
                            messages.success(request,"staff regsistered sucessfully")
                            
                        return render(request, 'staffReg.html')

                    else:
                        messages.info(request,"diffrent passwords entered")

               else:
                    messages.info(request,"Please providing all the information")

        else:
            return render(request, 'staffReg.html')

        return render(request, 'staffReg.html')
    except:
        messages.info(request,"Please try again some error occcured")
        
        return render(request, 'staffReg.html')
    
def courseRegisteration(request):
    try:
        if request.user.is_authenticated:
            #print(request.method =="POST")
            if request.method =='POST':
                course_name = request.POST.get('course_name')
                if(course_name):
                    Course = Courses(course_name=course_name,created_at=datetime.today())
                    Course.save()
                    messages.info(request,"Course added sucessfully")
                    
                    return render(request,'courseReg.html')
                else:
                    messages.info(request,"Please provide a course name")
                    
        return render(request,'courseReg.html')                    
    except:
        messages.info(request,"Please try again some error occcured")
        return render(request,'courseReg.html')                    
        
    

def subjectRegisteration(request):
    try:
            course_name = Courses.objects.all
            staff_name = Staff.objects.values("firstName","lastName",'id')
    
    
            if request.user.is_authenticated:
            #print(request.method =="POST")
                if request.method =='POST':
                    subjects = request.POST.get('subject')
                    coursename = request.POST.get("coursename")
                    ID = request.POST.get("staffID")


                    if(subjects and coursename):
                        course = Courses.objects.get(course_name = coursename)
                        staffID = Staff.objects.get(pk=int(ID))
                        subReg = Subjects(subject_name=subjects,staff_id=staffID,created_at=datetime.today())
                        subReg.save()
                        messages.info(request,"Subject added sucessfully")

                        return render(request,'subReg.html',{"courseName":course_name,"staffName":staff_name})

                    else:
                        messages.info(request,"please select course , staff and enter Subject")

            return render(request,'subReg.html',{"courseName":course_name,"staffName":staff_name})
    except:
        messages.info(request,"Please try again some error occcured")
        return render(request,'subReg.html',{"courseName":course_name,"staffName":staff_name})
        
    

#admin@#1214
    
    
#def attendence(request):
    
    
    # student = Students.object.get(admin = request.user.id)
    
    # course = student.course_id
    
    # subject = Subject.objects.filter(course_id = course)
    
    # context = {
    #     "subjects": subject
    # }
    # return render(request, 'attendence.html',context