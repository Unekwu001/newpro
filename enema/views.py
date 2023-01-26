import datetime
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from config.settings import client
from django.contrib import messages
from .models import Schools,Agents,Lodges,Locations,Lodgepics,Roomates,CustomerInfo,Myadmin,Schedule_Inspection,Roomymatching_table

# Create your views here.
def index(request):
    schools=Schools.objects.all()
    return render(request,'index.html',{'schools':schools})
    
    

def property_grid(request,id):
    allpics=Lodgepics.objects.all()
    uniq_schul=Schools.objects.get(id=id)
    lodges=Lodges.objects.filter(region=uniq_schul.name).order_by('-date_uploaded')
    if lodges:
        return render(request,'property-grid.html',{'uniq_schul':uniq_schul,'allpics':allpics,'lodges':lodges})
    else:
        messages.info(request,f' {uniq_schul.name} is not available in your Geo-location.')
        return redirect(index)


def single_property(request,id):
    record = Lodges.objects.get(id=id)
    agent= Agents.objects.get(id=record.agentid)
    allpics=Lodgepics.objects.all()
    return render(request,'property-single.html',{'record':record,'allpics':allpics,'agent':agent})



def agent_reg(request):
    session_collected=request.session.get('loggedin')
    if session_collected:
        messages.info(request,'Please kindly logout before you make a registration ')
        return redirect(agent_dash)
    else:
        if request.method=="GET":
            return render(request,'agent-reg.html')
        if request.method=="POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            pwd = request.POST.get('pwd')
            record_exists = Agents.objects.all().filter(email=email)
            if record_exists:
                messages.success(request,'User already exists.')
                return render(request,'agent-reg.html')
            else:
                record = Agents(name=name,email=email,pwd=pwd)
                record.save()
                mail = EmailMessage(
                    subject = 'Welcome to Enema Corporation',
                    body = f'Your login credentials are as follows: \n Email: {email} \n Password: {pwd} \n\n Students in need of lodges are waiting for you!',
                    from_email = 'info@enema.ng',
                    to = [email],
                    reply_to = [email],
                    headers={'Content-Type': 'text/plain'},)
                mail.send()
                return redirect(agent_login)



def agent_login(request):
    session_collected=request.session.get('loggedin')
    if session_collected:
        messages.info(request,'You are currently logged in.')
        return redirect(agent_dash)
    else:
        if request.method == 'GET':
            return render(request,'agent-login.html')
        if request.method == 'POST':   
            email = request.POST.get('email')
            pwd = request.POST.get('pwd')
            arecord_exists = Agents.objects.filter(email=email,pwd=pwd)
            if arecord_exists:
                for record_exists in arecord_exists:
                    userid = record_exists.id
                    request.session['loggedin'] = userid
                    return redirect(agent_dash)
            else:
                messages.info(request,'Invalid credentials. ')
                return redirect(agent_login)


def agent_dash(request):
    session_collected=request.session.get('loggedin')
    if session_collected:
        agentlodges=Lodges.objects.filter(agentid=session_collected).order_by('-date_uploaded')
        allpics=Lodgepics.objects.all().filter(agentid=session_collected)          
        record = Agents.objects.get(id=session_collected)
        return render(request,'agent-dash.html',{'record':record,'agentlodges':agentlodges,'allpics':allpics})
    else:
        messages.info(request,'Kindly login to continue.') 
        return redirect(agent_login)


def edit_profile(request):
    session_collected=request.session.get('loggedin')
    if session_collected:
        if request.method == "GET":
            agentlodges=Lodges.objects.filter(agentid=session_collected).order_by('-date_uploaded')
            allpics=Lodgepics.objects.all().filter(agentid=session_collected)       
            
            record = Agents.objects.get(id=session_collected)
            return render(request,'edit-profile.html',{'record':record,'agentlodges':agentlodges,'allpics':allpics})
        else:
            
            uploaded_file = request.FILES.get('pix')
            
            if uploaded_file is not None:   
                image = uploaded_file
                name = request.POST.get('name')
                phone = request.POST.get('phone')
                email =  request.POST.get('email')
                address =  request.POST.get('address')
                identity = request.POST.get('identity')
                identitynum = request.POST.get('identitynum')
                record = Agents.objects.get(id=session_collected)
                record.name=name
                record.phone=phone
                record.email=email
                record.address=address
                record.id_type=identity
                record.id_numb=identitynum 
                record.pic=image          
                record.save()
                messages.success(request,'Your profile has been updated successfully.')
                return redirect(agent_dash)
            else:
                name = request.POST.get('name')
                phone = request.POST.get('phone')
                email =  request.POST.get('email')
                address =  request.POST.get('address')
                identity = request.POST.get('identity')
                identitynum = request.POST.get('identitynum')
                record = Agents.objects.get(id=session_collected)
                record.name=name
                record.phone=phone
                record.email=email
                record.address=address
                record.id_type=identity
                record.id_numb=identitynum           
                record.save()
                messages.success(request,'Your profile has been updated successfully.')
                return redirect(agent_dash)
    else:
        messages.info(request,'Kindly login to continue.')   
        return redirect(agent_login)


def agent_logout(request):
    session_collected=request.session.get('loggedin')
    if session_collected:
        request.session.pop('loggedin')
        messages.info(request,'login to continue.') 
        return redirect(agent_login)
    else:
        messages.info(request,'Kindly login to continue.') 
        return redirect(agent_login)



def add_property(request):
    session_collected=request.session.get('loggedin')
    if session_collected:
        if request.method == "GET":
            agentlodges=Lodges.objects.filter(agentid=session_collected).order_by('-date_uploaded')
            allpics=Lodgepics.objects.all().filter(agentid=session_collected)  
            schools=Schools.objects.all()
            locations=Locations.objects.all()
            return render(request,'add-property.html',{'schools':schools,'locations':locations,'session_collected':session_collected,'agentlodges':agentlodges,'allpics':allpics})
        else:
            name=request.POST.get('name')
            price=request.POST.get('price')
            region=request.POST.get('region')
            location=request.POST.get('location')
            lodgetype=request.POST.get('lodgetype')
            tiled=request.POST.get('tiled')
            light=request.POST.get('light')
            water=request.POST.get('water')
            status=request.POST.get('status')
            agentid=session_collected
            
            entry1 = Lodges(
            name=name, 
            location=location, 
            lodgetype=lodgetype,  
            price=price,  
            Tiled =tiled,  
            light =light, 
            water = water, 
            status =status,  
            region=region,  
            agentid =agentid  
            )
            entry1.save()
            """we will retrieve the id of the lodge we saved and use it to save images on the Lodgepics table"""
            lodgeid=Lodges.objects.get(id=entry1.id)

            """next, we retrieve uploaded files"""
            upload1 = request.FILES.get('pic1')
            upload2 = request.FILES.get('pic2')
            upload3 = request.FILES.get('pic3')
            upload4 = request.FILES.get('pic4')
            upload5 = request.FILES.get('pic5')
            upload6 = request.FILES.get('pic6')
            upload7 = request.FILES.get('pic7')

            """record formation for each image"""
            record1=Lodgepics(picname=upload1,lodgeid=lodgeid,agentid=session_collected,sn=1)
            record2=Lodgepics(picname=upload2,lodgeid=lodgeid,agentid=session_collected,sn=2)
            record3=Lodgepics(picname=upload3,lodgeid=lodgeid,agentid=session_collected,sn=3)
            record4=Lodgepics(picname=upload4,lodgeid=lodgeid,agentid=session_collected,sn=4)
            record5=Lodgepics(picname=upload5,lodgeid=lodgeid,agentid=session_collected,sn=5)
            record6=Lodgepics(picname=upload6,lodgeid=lodgeid,agentid=session_collected,sn=6)
            record7=Lodgepics(picname=upload7,lodgeid=lodgeid,agentid=session_collected,sn=7)
            
            
            """saving all 7 records to database"""
            finallist=[record1,record2,record3,record4,record5,record6,record7]
            for y in finallist:
                y.save()
            messages.info(request,f'{name} has been successfully created and added to your list of lodges. Great!') 
            return redirect(agent_dash)

    else:
        messages.info(request,'Kindly login to continue.') 
        return redirect(agent_login)




def resetmail_sent(request):
    return render(request,'resetmail_sent.html')


def forgot_pwd(request):
    if request.method == "GET":
        return render(request,'4got-pwd.html')
    else:
        email = request.POST.get('email')
        records = Agents.objects.filter(email=email)
        if records:
            # html_message = f'Click the link below to reset your password. \n \n <a href="https://web-production-ee0e.up.railway.app/passwordreset/{email}/">Password reset Link</a>'
            # send_mail('enema Inc - Reset Password','','unekwutheophilus@gmail.com',[f'{email}'],fail_silently=False,html_message=html_message)
            return redirect(resetmail_sent)
        else:
            messages.info(request,f'{email} is not a registered user.')
            return redirect(forgot_pwd)


def pwd_reset(request,email):
    if request.method == "GET":
        messages.info(request,'Reset your password in a few seconds.')
        return render(request,'reset_pwd.html',{'email':email})
    if request.method == "POST":
        pwd = request.POST.get('pwd')
        record = Agents.objects.get(email=email)
        if record:
            record.pwd = pwd
            record.save()
            # send_mail('enema Inc - New credentials',f'Congratulations!. Below are your new login details. \n Email: {email} \n Password: {pwd}','unekwutheophilus@gmail.com',[f'{email}'],fail_silently=False)
            messages.success(request,f'Congratulations!. You can login here with your new details.')
            return redirect(agent_login)
        else:
            messages.info(request,f'something went wrong')
            return redirect(forgot_pwd)



def editlodge(request,id):
    session_collected=request.session.get('loggedin')
    if session_collected:
        if request.method=="POST":
            name= request.POST.get('name')
            price=request.POST.get('price')
            region=request.POST.get('region')
            location=request.POST.get('location')
            lodgetype=request.POST.get('lodgetype')
            tiled=request.POST.get('tiled')
            light=request.POST.get('light')
            water=request.POST.get('water')
            status=request.POST.get('status')
            agentid=session_collected

            """fetch record to be updated"""
            record = Lodges.objects.get(id=id)

            """updating the fetched records"""
            record.name=name
            record.price=price
            record.region=region
            record.location=location
            record.lodgetype=lodgetype
            record.Tiled=tiled
            record.light=light
            record.water=water
            record.status=status
            record.agentid=agentid

            """saving fetched record to database"""
            record.save()
            messages.success(request,f'{name} was updated successfully.')
            return redirect(agent_dash)

        else:
            lodge= Lodges.objects.get(id=id)
            agentlodges=Lodges.objects.filter(agentid=session_collected).order_by('-date_uploaded') 
            schools=Schools.objects.all()
            locations=Locations.objects.all()
            allpics=Lodgepics.objects.all().filter(agentid=session_collected)  
            return render(request,'editlodge.html',{'allpics':allpics,'lodge':lodge,'agentlodges':agentlodges,'schools':schools,'locations':locations})
    else:
        messages.info(request,'Kindly login to continue.') 
        return redirect(agent_login)    


def deletelodge(request,id):
    session_collected=request.session.get('loggedin')
    if session_collected:
        alodge = Lodges.objects.get(id=id)
        alodge.delete()
        messages.success(request,f'You have successfully deleted {alodge.name}') 
        return redirect(agent_dash)
    else:
        return redirect(agent_login)



def selectschool(request):
    """"this view is for roomy button at index.html."""
    schools=Schools.objects.all()
    return render(request,'selectschool.html',{'schools':schools})


def typeofroomy(request,name):
    school = Schools.objects.get(name=name)
    return render(request,'typeofroomy.html',{'school':school})


def roomates_grid(request,name):
    roomates = Roomates.objects.filter(schoolname=name).order_by('-date_uploaded')
    if roomates:
        return render(request,'roomates_grid.html',{'roomates':roomates})
    else:
        messages.info(request,f'Room mates are not yet available in {name}')
        return redirect(selectschool)



def roomy_form(request,name):
    if request.method == "GET":
        roomates = Roomates.objects.filter(schoolname=name)
        school = Schools.objects.get(name=name)
        locations = Locations.objects.filter(school=name)
        return render(request,'roomy-form.html',{'roomates':roomates,'school':school,'locations':locations})
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        schul = request.POST.get('school') 
        lodgerent = request.POST.get('lodgerent')
        pricesharing = request.POST.get('sharingformula')
        location =request.POST.get('location')
        tiled = request.POST.get('tiled')
        water = request.POST.get('water') 
        light = request.POST.get('light')
        lodgetype = request.POST.get('lodgetype')
        religion = request.POST.get('religion')
        pix = request.FILES.get('pix')
        pic1 = request.FILES.get('pic1')
        pic2 = request.FILES.get('pic2')
        pic3 = request.FILES.get('pic3')
         
        """inserting a new record"""
        record = Roomates(
        pic = pix,
        pic1 = pic1,
        pic2 = pic2,
        pic3 = pic3,
        schoolname = schul,
        lodgerent = lodgerent,
        location = location,
        tiled = tiled,
        water = water,
        light = light,
        pricesharing = pricesharing,
        lodgetype = lodgetype,
        religion = religion,
        phone = phone,
        fullname = fullname
        )
        record.save()
        messages.info(request,f'You have been added as a roomy. Congratulations!. You will be matched within the next 48 hours.')
        return redirect(roomates_grid,name)


def pay(request,id):
    if request.method == "POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        amount=request.POST.get('amount')
        phone=request.POST.get('phone')

        customer = CustomerInfo(
            fullname=fullname,
            email=email,
            phonenumber=phone,
            amount=amount,
            payfor="roomate_meeting"
        )
        customer.save()
        roomate = Roomates.objects.get(id=id)
        return render(request, 'payment.html',{"email":email,'phone':phone,'amount':amount,'roomate':roomate,'fullname':fullname})
    else:
        roomate = Roomates.objects.get(id=id)
        return render(request,'pay.html',{'roomate':roomate})



def roomate_single(request,id):
    roomate = Roomates.objects.get(id=id)
    pricetopay = (int(roomate.pricesharing)/100)*(int(roomate.lodgerent))
    return render(request,'roomate-single.html',{'roomate':roomate, 'pricetopay':pricetopay})



def lodge_pay(request,id):
    if request.method == "POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        amount=request.POST.get('amount')
        phone=request.POST.get('phone')

        customer = CustomerInfo(
            fullname=fullname,
            email=email,
            phonenumber=phone,
            amount=amount,
            payfor="lodge_inspection"
        )
        customer.save()
        lodge = Lodges.objects.get(id=id)   
        return render(request, 'lodge-payment.html',{'email':email,'phone':phone,'amount':amount,'lodge':lodge,'fullname':fullname})
    else:
        lodge = Lodges.objects.get(id=id)
        lodgepics = Lodgepics.objects.filter(lodgeid=lodge.id,sn=1)
        lodgepic = lodgepics[0].picname
        return render(request,'lodge-pay.html',{'lodge':lodge,'lodgepic':lodgepic})


def congrats(request):
    return render(request,'congrats.html')



def admin_login(request):
    if request.method == "GET":
        return render(request,'admin/admin-login.html')
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        record = Myadmin.objects.get(username=username,pwd=pwd)
        if record:
            request.session['adminloggedin'] = record.id
            return redirect(admindash) 
        else:
            messages.info(request,'Invalid credentials. ')
            return redirect(admin_login)


def admindash(request):
    session_collected=request.session.get('adminloggedin')
    if session_collected:
        admin = Myadmin.objects.get(id=session_collected)
        lodges=Lodges.objects.all().order_by('-date_uploaded')
        roomates = Roomates.objects.all().order_by('-date_uploaded')         
        agents= Agents.objects.all().order_by('-date_joined')
        return render(request,'admin/admin-dashboard.html',{'roomates':roomates,'admin':admin,'agents':agents,'lodges':lodges})
    else:
        messages.info(request,'Kindly login to continue.') 
        return redirect(admin_login)




def admin_agentpanel(request):
    agents = Agents.objects.all().order_by('-date_joined')
    return render(request,'admin/agents-panel.html',{'agents':agents})



def verify_agent(request,id):
    agent = Agents.objects.get(id=id)
    agent.status = "verified"
    agent.save()
    return redirect(admin_agentpanel)



def admin_lodgepanel(request):
    lodges = Lodges.objects.all().order_by('-date_uploaded')
    return render(request,'admin/lodges-panel.html',{'lodges':lodges})


def toggle_lodgestatus(request,id):
    lodge = Lodges.objects.get(id=id)
    if lodge.status=="available":
        lodge.status = "occupied"
        lodge.save()
        return redirect(admin_lodgepanel)
    if lodge.status=="occupied":
        lodge.status="available"
        lodge.save()
        return redirect(admin_lodgepanel)



def admindelete_lodge(request,id):
    lodge = Lodges.objects.get(id=id)
    lodge.delete()
    return redirect(admin_lodgepanel)


def admin_showlodge(request,id):
    record = Lodges.objects.get(id=id)
    agent= Agents.objects.get(id=record.agentid)
    allpics=Lodgepics.objects.all()
    return render(request,'admin/admin-showlodge.html',{'record':record,'allpics':allpics,'agent':agent})



def schedulodge_inspection(request,id):
    if request.method == 'GET':
        lodge = Lodges.objects.get(id=id)
        return render(request,'schedulingform.html',{'lodge':lodge})
    else:
        lodge = Lodges.objects.get(id=id)
        doi = request.POST.get('doi')
        toi = request.POST.get('toi')
        studentname = request.POST.get('name')
        studentphone = request.POST.get('phone')
        studentemail = request.POST.get('email')
        # doi_clean = datetime.strftime('%M %B %Y')

        """creating record"""
        record = Schedule_Inspection(
            date_of_inspection=doi,
            timeof_inspection=toi,
            studentname=studentname,
            studentphone=studentphone,
            studentemail=studentemail,
            lodgename =lodge.name,
            lodgeid =lodge.id
        )
        record.save()

        """sending email to student"""
        send_mail('Lodge Inspection Day!',
        f'Congratulations {studentname} ! You have been scheduled to inspect {lodge.name} as follows: \n Date of inspection: {doi} \n Time of inspection: {toi} \n Meeting venue: Kitchen 54 Tammah. \n\n Have a wonderful day ahead. \n Jemimah Adiburmi\n Head of people.\n Enema Corporations.',
        'enema.corporations.admin@enema.ng',
        [f'{studentemail}'],
        fail_silently=False)

        """sending text message to the student's phone number using twilio"""
        
        date = record.date_of_inspection
        date = datetime.datetime.strptime(date,'%Y-%m-%d')
        date = date.strftime('%A %B %d , %Y')

        message = client.messages.create(
            body=f'Congratulations {studentname} ! You have been scheduled to inspect {lodge.name} as follows: \n Date of inspection: {date} \n Time of inspection: {toi} \n Meeting venue: Kitchen 54 Tammah. \n\n Jemimah Adiburmi\n Head of people.\n Enema Corporations.',
            from_='+12182281796',
            to=f'+234{studentphone}'
        )
        print(message.sid)
        
        """flash message"""
        messages.info(request,'Well done. A student has been scheduled.')
        return redirect(admin_lodgepanel)



def schedulehistory(request,id):
    histories = Schedule_Inspection.objects.filter(lodgeid=id)
    return render(request,'admin/schedulehistory.html',{'histories':histories})


def reschedule_student(request,id):
    if request.method == "GET":
        record = Schedule_Inspection.objects.get(id=id)
        return render(request,'reschedulingform.html',{'record':record})
    else:
        record = Schedule_Inspection.objects.get(id=id)
        doi=request.POST.get('doi')
        toi=request.POST.get('toi')
        studentname=request.POST.get('name')
        studentphone=request.POST.get('phone')
        studentemail=request.POST.get('email')

        record.date_of_inspection=doi
        record.timeof_inspection=toi
        record.studentname=studentname
        record.studentphone=studentphone
        record.studentemail=studentemail

        record.save()
        messages.info(request,f' {record.studentname} has been successfully rescheduled for {record.lodgename}.')
        return redirect(schedulehistory,record.lodgeid)


def allschedulehistory(request):
    histories = Schedule_Inspection.objects.all()
    return render(request,'admin/allschedulehistory.html',{'histories':histories})


def toggle_schedulehistory(request,id):
    record = Schedule_Inspection.objects.get(id=id)
    if record.inspection_status == 'fulfilled':
        record.inspection_status='inprogress'
        record.save()
        messages.info(request,f'Inspection status has changed to "inprogress" for record with ID {record.id}.')
        return redirect(allschedulehistory)
    elif record.inspection_status == 'inprogress':
        record.inspection_status='fulfilled'
        record.save()
        messages.info(request,f'Inspection status has changed to "fulfilled" for record with ID {record.id}.')
        return redirect(allschedulehistory)
    else:
        return redirect(allschedulehistory)
    


def admin_roomiespanel(request):
    roomies = Roomates.objects.all()
    return render(request,'admin/roomies-panel.html',{'roomies':roomies})


def admin_deleteroomy(request,id):
    roomy = Roomates.objects.get(id=id)
    roomy.delete()
    messages.info(request,f'{roomy.name} has been successfully deleted from the list of roomies.')
    return redirect(admin_roomiespanel)


def admin_matchroomy(request,id):
    if request.method=="GET":
        roomy = Roomates.objects.get(id=id)
        return render(request,'matchroomy.html',{'roomy':roomy})
    else:
        roomy = Roomates.objects.get(id=id)

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')

        """inserting into roomymatching_table"""
        record = Roomymatching_table(
            owner_name = roomy.fullname,
            owner_phone = roomy.phone,
            seeker_name = name,
            seeker_phone = phone,
            date_ofmeeting = date,
            time_ofmeeting =time
        )
        record.save()

        date = record.date_ofmeeting
        date = datetime.datetime.strptime(date,'%Y-%m-%d')
        date = date.strftime('%A %B %d , %Y')

        message1 = client.messages.create(
            body=f'Congratulations {roomy.fullname} ! You have been scheduled to meet {name} as follows: \n Date: {date} \n Time: {time} \n Meeting venue: Kitchen 54 Tammah. \n\n Jemimah Adiburmi\n Head of people.\n Enema Corporations.',
            from_='+12182281796',
            to=f'+234{roomy.phone}'
        )
        print(message1.sid)

        message2 = client.messages.create(
            body=f'Congratulations {name} ! You have been scheduled to meet {roomy.fullname} as follows: \n Date: {date} \n Time: {time} \n Meeting venue: Kitchen 54 Tammah. \n\n Jemimah Adiburmi\n Head of people.\n Enema Corporations.',
            from_='+12182281796',
            to=f'+234{phone}'
        )
        print(message2.sid)

        messages.info(request,f'{name} has been matched to {roomy.fullname}')
        return redirect(admin_roomiespanel)


def matchhistory(request,id):
    histories = Roomymatching_table.objects.filter(id=id)
    return render(request,'admin/matchhistory.html',{'histories':histories})


def terms_of_service(request):
    return render(request,'termsOfService.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')