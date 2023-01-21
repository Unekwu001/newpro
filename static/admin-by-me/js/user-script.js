let container = document.getElementById('container')

toggle = () => {
	container.classList.toggle('sign-in')
	container.classList.toggle('sign-up')
}

setTimeout(() => {
	container.classList.add('sign-up')
},0)



let validator = (e) => {
		var pwdPattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
		var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
		
		var mail = document.getElementById('reg-email').value;
		var pass1 = document.getElementById('reg-pwd').value;
		var pass2 = document.getElementById('reg-chkpwd').value;
		
		if(!mail.match(mailformat))
				{
				Swal.fire("You have entered an invalid email address!");
				e.preventDefault();;
				}					
		else if(!pass1.match(pwdPattern)) 
				{
				Swal.fire('Password should have a combination of at least 6 characters made up of lowercase,uppercased letters, and number(s)')
				e.preventDefault();;
				}
		else if(pass1 != pass2)
				{
				Swal.fire('Oops! Please make sure both passwords match.')
				e.preventDefault();;
				}
	 	else
	 			{
	 			Swal.fire('Loading.....')
	 			}
		}
		
 	
 	
 	
let welcome =()=>{
	Swal.fire({
  		title: 'Welcome to Psameeetech Academy',
  		showClass: {popup: 'animate__animated animate__fadeInDown'},
  		hideClass: {popup: 'animate__animated animate__fadeOutUp'}
		})
		}
const welcoming = setTimeout(welcome,1000)			
 	
 		
 //let warning =()=>{
 //	Swal.fire('This is <span style="color:red">NOT</span> the Federal Polytechnic Nasarawa Website. This site belongs to Psameeetech Academy. Psameeetech Academy will help you fill all the necessary information on the school site and forward all details to your email or whatsapp (based on your preference). Thankyou ')
 //}
 //const mytimeout = setTimeout(warning,8000)	
		
		
				
		
		
		
		
		
		
		
		
		
		
		

