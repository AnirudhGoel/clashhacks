function login(event) {
	event.preventDefault();

	var username = $("#username").val();
	var password = $("#password").val();
	$.getJSON("login/", {username: username, password: password}, function(data) {
		if (data.response == "valid") {
			window.location = "http://localhost:8000/dobby/home";
		} else {
			console.log(data.response, data.message);
		}
	});
}