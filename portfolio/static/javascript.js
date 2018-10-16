function confirmation() {
	var answer = confirm("Thanks for contacting me! Want to see my blog? (Just showing off javascript here)")
	if (answer == true){
		window.location.href = "http://localhost:8000/blog/";
	}
	else{
		alert("Thanks again!");
	}
}
