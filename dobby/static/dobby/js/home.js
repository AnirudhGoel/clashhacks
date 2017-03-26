$(document).ready(function() {
	var userId = $("#userId").val();

	// Pending Tran
	$.getJSON("/dobby/pendingTeacher/", {userId: userId}, function(data) {
		if (data.response != "None") {
			resp = data.response;
			for (var i = 0; i < Object.keys(resp).length; i++) {
				// console.log(resp[i]);
				$("#pendTran").append("<div class='circle col-md-4'>" + resp[i]['learnerName'] + "<br>" + resp[i]['skillName'] + "<br>" + resp[i]['location'] + "<br>" + resp[i]['mobile'] + "<br><button onclick='acceptClicked(event);' id='" + resp[i]['transId'] + "' class='accept'>Accept</button><button onclick='rejectClicked(event);' id='" + resp[i]['transId'] + "' class='reject'>Reject</button>" + "</div>");
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
				$("#onTran").append("<div class='circle col-md-4'>" + resp[i]['learnerName'] + "<br>" + resp[i]['skillName'] + "<br>" + resp[i]['location'] + "<br>" + resp[i]['mobile'] + "<br><input id='text-" + resp[i]['ongId'] + "' type='text' class='text'></input><select id='sel-" + resp[i]['ongId'] + "'><option>Hours</option><option>Rupees</option></select><br><button onclick='completeClicked(event);' id='" + resp[i]['ongId'] + "' class='complete'>Complete</button></div>");
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
				$("#compTran").append("<div class='circle col-md-4'>" + resp[i]['learnerName'] + "<br>" + resp[i]['skillName'] + "<br>" + "<br>" + resp[i]['mobile'] + "<br>" + resp[i]['spent'] + "</div>");
			}
		} else {

		}
	});
});

// Buttons
function acceptClicked(event) {
	console.log(event.target.id);
	$.getJSON("/dobby/pendingToOngoing", {transId: event.target.id}, function(data) {
		console.log(data);
		location.reload(); 
	});
}

function rejectClicked(event) {
	console.log(event.target.id);
	$.getJSON("/dobby/pendingToReject", {transId: event.target.id}, function(data) {
		console.log(data);
		location.reload(); 
	});
}

function completeClicked(event) {
	console.log(event.target.id);
	var selectValue = $('select[id=sel-' + event.target.id + ']').val();
	if (selectValue == "Hours") {
		byTime = 1;
	} else {
		byTime = 0;
	}
	var value = $("#text-" + event.target.id).val();

	if (value != "") {
		$.getJSON("/dobby/ongoingToComplete", {ongId: event.target.id, byTime: byTime, value: value}, function(data) {
			console.log(data);
			location.reload(); 
		});
	}
}