(function () {
	"use strict";

	var treeviewMenu = $('.app-menu');

	// Toggle Sidebar
	$('[data-toggle="sidebar"]').click(function(event) {
		event.preventDefault();
		$('.app').toggleClass('sidenav-toggled');
	});

	// Activate sidebar treeview toggle
	$("[data-toggle='treeview']").click(function(event) {
		event.preventDefault();
		if(!$(this).parent().hasClass('is-expanded')) {
			treeviewMenu.find("[data-toggle='treeview']").parent().removeClass('is-expanded');
		}
		$(this).parent().toggleClass('is-expanded');
	});

	// Set initial active toggle
	$("[data-toggle='treeview.'].is-expanded").parent().toggleClass('is-expanded');

	//Activate bootstrip tooltips
	$("[data-toggle='tooltip']").tooltip();

})();

let jamb_total = ()=>{
	            	var eng=parseFloat(document.getElementById('eng').value);
                  	var jsub2=parseFloat(document.getElementById('jsub2').value);
                  	var jsub3=parseFloat(document.getElementById('jsub3').value);
                  	var jsub4=parseFloat(document.getElementById('jsub4').value);
                  	
                  	var all = [eng , jsub2 , jsub3 , jsub4];
                  	;
                  	total=0
                  	for(x=0;x<=3;x++)
                  		{
				total= total + all[x]	                  		
                  		}
                  	document.getElementById('total').innerHTML=total ;
                  	}
                  	
                	
  
                  	
                  	
                  	
                  	
                  	
                  	
                  	
              
              
              
              
