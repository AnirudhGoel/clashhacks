$(document).ready(function() {
	var userId = $("#userId").val();

	// Pending Tran
	$.getJSON("/dobby/pendingTeacher/", {userId: userId}, function(data) {
		if (data.response != "None") {
			resp = data.response;
			for (var i = 0; i < Object.keys(resp).length; i++) {
				// console.log(resp[i]);
				$("#pendTran").append("<div class='circle col-md-4'>" + resp[i]['learnerName'] + "<br>" + resp[i]['skillName'] + "<br>" + resp[i]['location'] + "<br>" + resp[i]['mobile'] + "<br><button id='" + resp[i]['transId'] + "' class='accept'>Accept</button><button id='" + resp[i]['transId'] + "' class='reject'>Reject</button>" + "</div>");
			}
		} else {

		}
	});

	// Ongoing Tran
	$.getJSON("/dobby/ongTrans/", {userId: userId}, function(data) {
		if (data.response != "None") {
			resp = data.response;
			for (var i = 0; i < Object.keys(resp).length; i++) {
				// console.log(resp[i]);
				$("#onTran").append("<div class='circle'>" + resp[i]['learnerName'] + "<br>" + resp[i]['skillName'] + "<br>" + resp[i]['location'] + "<br>" + resp[i]['mobile'] + "<br><button id='" + resp[i]['ongId'] + "' class='complete'>Complete</button></div>");
			}
		} else {

		}
	});

	// Completed Tran
	$.getJSON("/dobby/compTrans/", {userId: userId}, function(data) {
		if (data.response != "None") {
			resp = data.response;
			for (var i = 0; i < Object.keys(resp).length; i++) {
				// console.log(resp[i]);
				$("#compTran").append("<div class='circle'>" + resp[i]['learnerName'] + "<br>" + resp[i]['skillName'] + "<br>" + "<br>" + resp[i]['mobile'] + "<br>" + resp[i]['spent'] + "</div>");
			}
		} else {

		}
	});
});