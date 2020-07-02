$(document).ready(function() {
	$('a').bind('click', function(e) {           
		var url = $(this).attr('href');
		if(url != "#")
		{
			$.ajax({
			type: "get",
			url: url, 
			success: function(data){
				var c = $('div#container')[0];
				var d = JSON.stringify(data).replace(/{|}|\"/g,"");
				c.innerHTML= d;  
				//update png
				var timestamp = new Date().getTime();  
				var el = document.getElementById("plot");  
				var queryString = "?t=" + timestamp;    
				el.src = "static/plot.png" + queryString;                     
			}
			});
		}
		else
		{
			if(this.id == "enable_settings"){
				console.log("enable_settings")
				$('#simulation_settings').toggle();
			}
			if(this.id == "modify_nodes"){
				console.log("modify_nodes");
				$('#simulation_node').toggle();
			}
		}
	    e.preventDefault(); // stop the browser from following the link
	});

	$.ajax({
		type: "get",
		url: "/simulation_settings", 
		success: function(data){
			$('input#options')[0].value = data["options"]; 
			$('input#title')[0].value = data["title"];
			$('input#tran')[0].value = data["tran"];            
		}
	});
})

