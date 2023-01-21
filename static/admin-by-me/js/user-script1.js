let container = document.getElementById('container')

toggle = () => {
	container.classList.toggle('sign-in')
	container.classList.toggle('sign-up')
}

setTimeout(() => {
	container.classList.add('sign-in')
},0)

 
 
let validator = () => {
		var pwdPattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
		var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
		
		var mail = document.getElementById('reg-email').value;
		var pass1 = document.getElementById('reg-pwd').value;
		var pass2 = document.getElementById('reg-chkpwd').value;
		
		if(!mail.match(mailformat))
				{
				Swal.fire("You have entered an invalid email address!");
				return false;
				}					
		else if(!pass1.match(pwdPattern)) 
				{
				Swal.fire('Password should have a combination of at least 6 characters made up of lowercase,uppercased letters, and number(s)')
				return false;
				}
		else if(pass1 != pass2)
				{
				Swal.fire('Oops! Please make sure both passwords match.')
				return false;
				}
	 	else
	 			{
	 			Swal.fire('Congratulations!')
	 			}
		}
		
  
  
 // let welcome =()=>{
//	Swal.fire({
  //		title: 'Login to complete your form submission.',
  //		showClass: {popup: 'animate__animated animate__fadeInDown'},
  //		hideClass: {popup: 'animate__animated animate__fadeOutUp'}
	//	})
	//	}
//const welcoming = setTimeout(welcome,1000)			
 	
  
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
