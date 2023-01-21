function send(){

	name=document.getELementById('name').value;
	email=document.getELementById('email').value;
	message=document.getELementById('message').value;
	
	if(name=="" or email == "" or message ==""){
		alert('Please ensure all fields are filled correctly')
	}
	else{
		alert('Please wait...')
	}
}
