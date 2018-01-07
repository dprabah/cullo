$(document).foundation()

var Id = 0;
$( "#cullo-ui-ask" ).click(function() {
	
	if(validateText()){
		var currResp = ++Id;
		console.log(currResp);
		console.log(Id);
		appendInitialResponse(response($('#cullo-ui-text').val(),"",Id));
		
		$.ajax({
			method: "POST",
			contentType: "application/json",
			url: "/ask",
			data: JSON.stringify({ query:$("#cullo-ui-text").val() })
		}).done(function( msg ) {
		console.log(msg);
		appendInitialResponse(response($("#cullo-ui-text").val(),msg,Id));
			
		});
	}

});

function validateText(){
	if($('#cullo-ui-text').val() == ""){
		console.log("Enter something!");
		return false;
	}else{
		return true;
	}
}

function response(userQuery, response, Id){
	if(response == ""){
		response = '<div class="media-object"> <div class="media-object-section"> <i class="fa fa-user fa-4x" aria-hidden="true"></i></div> <div class="media-object-section"> <h4>User.</h4> <p>' +userQuery+'</p>   </div> </div>';
	}else{
		response = '<div class="media-object cullo-response"> <div class="media-object-section"><i class="fa fa-female fa-4x" aria-hidden="true"></i></div> <div class="media-object-section"> <h4>Cullo.</h4> <p>'+response+'</p>   </div> </div>'	
		/*response = '<div class="media-object cullo-response"> <div class="media-object-section"> <div class="thumbnail"> <img src="assets/img/media-object/avatar-1.jpg"> </div> </div> <div class="media-object-section"> <h4>Cullo.</h4> <p>'+response+'</p>   </div> </div>'*/
	}
	
	return response;
}

function appendInitialResponse(response){
	$("#cullo-ui-response").append(response);
	$("#cullo-ui-response").scrollTop($("#cullo-ui-response")[0].scrollHeight);
}