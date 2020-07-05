$(document).ready(function() {
	write_status("initializing simulator...");

	$('a').bind('click', function(e) {           
		var url = $(this).attr('href');
		if(url != "#")
		{
			$.ajax({
			type: "get",
			url: url, 
			success: function(data, status, xhr){
				write_status(data);
				if(xhr.hasOwnProperty('responseJSON') && 'run' in data){
					if(data['run'] == 'started'){
						$("#run")[0].innerHTML = "pause";
					}
					else{
						$("#run")[0].innerHTML = "play";
					}
				}
				update_png();
				update_settings();                   
			}
			});
		}
		else
		{
			if(this.id == "enable_settings"){
				console.log("enable_settings")
				$('#simulation_settings').toggle();
				$('#simulation_node').hide();
			}
			if(this.id == "modify_nodes"){
				console.log("modify_nodes");
				$('#simulation_node').toggle();
				$('#simulation_settings').hide();
			}
		}
		update_settings();
	    e.preventDefault(); // stop the browser from following the link
	});
	$('select').bind('change', function(e) {
		this.previousElementSibling.value=this.value; 
		this.previousElementSibling.focus();
		$.ajax({
			type: "get",
			url: "/simulation_node", 
			data: { node: this.value },
			success: function(data){
				if(data['node'] == 'none'){
					$('input#value')[0].value = 'undefined';   
				}else{
					$('input#value')[0].value = data[Object.keys(data)[0]];   
				}
				        
			}
		});
	});
	$('form#simulation_node').submit(function(e) {   
		e.preventDefault();
		var form = $(this);
		var url = form.attr('action');
	
		$.ajax({
			   type: "POST",
			   url: url,
			   data: form.serialize(), // serializes the form's elements.
			   success: function(data)
			   {	
					var c = $('div#container')[0];
				   	if(data['node'] == "post ok"){
						//$('#simulation_node').hide();
				   	}
				   	write_status(data);
			   }
			 });
	});
	$('form#simulation_settings').submit(function(e) {   
		e.preventDefault();
		var form = $(this);
		var url = form.attr('action');
	
		$.ajax({
			   type: "POST",
			   url: url,
			   data: form.serialize(), // serializes the form's elements.
			   success: function(data)
			   {
					var c = $('div#container')[0];
					if('title' in data){
						data = "post ok"
					}

					//perform reinit on modified settings
					$.ajax({
						type: "get",
						url: "/reinit",
						success: function(data){
							write_status(data);
							update_png(); 
							update_settings();                   
						}
					});

					write_status(data);
				   //alert(data); // show response
			   }
			 });
	});

	//perform init on page load
	$.ajax({
		type: "get",
		url: "/init?scd=../open_substation.scd",
		success: function(data){
			write_status(data);
			update_png();
			update_settings();                   
		}
	});
})

function update_settings()
{
	$.ajax({
		type: "get",
		url: "/simulation_settings", 
		success: function(data){
			$('input#options')[0].value = data["options"]; 
			$('input#title')[0].value = data["title"];
			$('input#tran')[0].value = data["tran"];            
		}
	});

	$.ajax({
		type: "get",
		url: "/simulation_nodes", 
		success: function(data){
			var sel = $('#nodes');
			sel.find('option').remove().end();
			sel.append('<option>--- select a node---</option>');
			for(var opt_data in data){
				for(var elem in data[opt_data]['elements']){
					var opt = document.createElement('option');
					opt.innerHTML = data[opt_data]['elements'][elem];
					sel.append(opt);
				}
				
			}
			     
		}
	});
}

function write_status(data){
	var c = $('div#container')[0];
	var d = JSON.stringify(data).replace(/{|}|\"/g,"").replace(/\\n/g,"<br>");
	c.innerHTML= "<pre style='white-space: pre-line'>" + d + "</pre>";  
}

function update_png(){
	var timestamp = new Date().getTime();  
	var el = document.getElementById("plot");  
	var queryString = "?t=" + timestamp;    
	el.src = "static/plot.png" + queryString;  
}
