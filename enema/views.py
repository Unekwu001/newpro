from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Schools,Agents,Lodges,Locations,Lodgepics,Roomates

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
                message="User already exists"
                return render(request,'agent-reg.html',{'message':message})
            else:
                record = Agents(name=name,email=email,pwd=pwd)
                record.save()
                #flash(message)
                # message="Congratulations! You can login."
                # send email
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
                fss = FileSystemStorage()
                image_name = fss.save(uploaded_file.name,uploaded_file)
                
                if image_name.endswith('.jpg') or image_name.endswith('.png') or image_name.endswith('.jpeg') or image_name.endswith('.JPEG') or image_name.endswith('.JPG') or image_name.endswith('.PNG'):

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
                    record.pic=image_name           
                    record.save()
                    messages.success(request,'Your profile has been updated successfully.')
                    return redirect(agent_dash)
                else:
                    
                    return redirect(edit_profile)
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
            upload8 = request.FILES.get('pic8')
            upload9 = request.FILES.get('pic9')

            """name conversion of retrieved files.After conversion,file is saved to media folder while filename is saved in database"""
            fss = FileSystemStorage()
            image_name1 = fss.save(upload1.name,upload1)
            image_name2 = fss.save(upload2.name,upload2)
            image_name3 = fss.save(upload3.name,upload3)
            image_name4 = fss.save(upload4.name,upload4)
            image_name5 = fss.save(upload5.name,upload5)
            image_name6 = fss.save(upload6.name,upload6)
            image_name7 = fss.save(upload7.name,upload7)
            image_name8 = fss.save(upload8.name,upload8)
            image_name9 = fss.save(upload9.name,upload9)

            """record formation for each image"""
            record1=Lodgepics(picname=image_name1,lodgeid=lodgeid,agentid=session_collected,sn=1)
            record2=Lodgepics(picname=image_name2,lodgeid=lodgeid,agentid=session_collected,sn=2)
            record3=Lodgepics(picname=image_name3,lodgeid=lodgeid,agentid=session_collected,sn=3)
            record4=Lodgepics(picname=image_name4,lodgeid=lodgeid,agentid=session_collected,sn=4)
            record5=Lodgepics(picname=image_name5,lodgeid=lodgeid,agentid=session_collected,sn=5)
            record6=Lodgepics(picname=image_name6,lodgeid=lodgeid,agentid=session_collected,sn=6)
            record7=Lodgepics(picname=image_name7,lodgeid=lodgeid,agentid=session_collected,sn=7)
            record8=Lodgepics(picname=image_name8,lodgeid=lodgeid,agentid=session_collected,sn=8)
            record9=Lodgepics(picname=image_name9,lodgeid=lodgeid,agentid=session_collected,sn=9)
            
            """saving all 9 records to database"""
            finallist=[record1,record2,record3,record4,record5,record6,record7,record8,record9]
            for y in finallist:
                y.save()
            messages.info(request,f'{name} has been successfully created and added to your list of lodges. Great!') 
            return redirect(agent_dash)

    else:
        messages.info(request,'Kindly login to continue.') 
        return redirect(agent_login)






        


def forgot_pwd(request):
    return render(request,'4got-pwd.html')


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

            """fetch record for to be updated"""
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
        if pix is not None:
                fss = FileSystemStorage()
                image_name = fss.save(pix.name,pix)
        
        record = Roomates(
        pic = image_name,
        schoolname = schul,
        lodgerent = lodgerent,
        location = location,
        tiled = tiled,
        water = water,
        light = light,
        pricesharing = pricesharing,
        lodgetype = lodgetype,
        religion = religion,
        phone = phone
        )
        record.save()
        messages.info(request,f'You have been added as a roomy. Congratulations!. You will be matched within the next 48 hours.')
        return redirect(roomates_grid,name)

