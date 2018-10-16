function confirmation() {
	var answer = confirm("Thanks for contacting me! Return to home page?")
	if (answer){
		window.location = "https://www.frederickchute.com/";
	}
	else{
		alert("Thanks for contacting me!")
	}
}
