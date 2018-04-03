$(document).foundation()
var current_state = 0
var current_pending = null
var Id = 0;

/**
 * sends data to the bot and handles the response.
 * acts as a controller
 */
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
			data: JSON.stringify({ query:$("#cullo-ui-text").val(),state:current_state, pending:current_pending })
		}).done(function( msg ) {
			msg = JSON.parse(msg)
			console.log(msg)
		console.log(msg.state);
		console.log(msg['pending']);
		console.log(msg['return_message']);
		current_state = msg.state
		current_pending = msg['pending']
		$('#cullo-ui-text').val("");
		appendInitialResponse(response($("#cullo-ui-text").val(),msg['return_message'],Id));

		});
	}
});

/***
 * clears the textarea, after getting response from bot.
 * @param element
 */
function clearContents(element) {
  element.value = '';
}

/***
 * Validates the textarea for some content, before submitting data to bot.
 * @param response
 */
function validateText(){
	if($('#cullo-ui-text').val() == ""){
		console.log("Enter something!");
		return false;
	}else{
		return true;
	}
}

/***
 * Sets the response to the UI
 * @param response
 */
function response(userQuery, response, Id){
	if(response == ""){
		response = '<div class="media-object"> <div class="media-object-section"> <i class="fa fa-user fa-4x" aria-hidden="true"></i></div> <div class="media-object-section"> <h4>User.</h4> <p>' +userQuery+'</p>   </div> </div>';
	}else{
		response = '<div class="media-object cullo-response"> <div class="media-object-section"><i class="fa fa-female fa-4x" aria-hidden="true"></i></div> <div class="media-object-section"> <h4>Cullo.</h4> <p>'+response+'</p>   </div> </div>'	
		/*response = '<div class="media-object cullo-response"> <div class="media-object-section"> <div class="thumbnail"> <img src="assets/img/media-object/avatar-1.jpg"> </div> </div> <div class="media-object-section"> <h4>Cullo.</h4> <p>'+response+'</p>   </div> </div>'*/
	}
	
	return response;
}

/***
 * Sets the response to the UI
 * @param response
 */
function appendInitialResponse(response){
	console.log(response)
	$("#cullo-ui-response").append(response);
	$("#cullo-ui-response").scrollTop($("#cullo-ui-response")[0].scrollHeight);
}