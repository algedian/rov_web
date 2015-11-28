function camoff(){
	window.stop();
	setTimeout(function(){
		var frame = document.getElementById("nemo");
		frame.src = "/static/img/fiesta_spider.jpg";	
	}, 1000);
}

function camon(){
	//alert("camon");
	var img = $('#nemo')[0];
	img.src='/video_feed'
}

function ledon(){
	//$('button#ledon').click(function(){
		//alert("led");
	$.ajax({
		url:'ledon',
		success: function(){
			
		}
	});
		
	//});
}

function ledoff(){
	//$('button#ledoff').bind('click',function(){
	//alert("led");
	$.ajax({
		url:'ledoff',
		success: function(){
			//alert("off");
		}
	});
	
	//});
}
function gostraight(){
	$.ajax({
		url:'gostraight',
		success: function(){
			/*setTimeout(function(){
				motorstop();
			}, 1000);*/
		}
	});
}

function goback(){
	$.ajax({
		url:'goback',
		success: function(){
			/*setTimeout(function(){
				motorstop()
			}, 1000);*/
		}
	});
}

function goleft(){
	$.ajax({
		url:'goleft',
		success: function(){
			/*setTimeout(function(){
				motorstop()
			}, 1000);*/
		}
	});
}

function goright(){
	$.ajax({
		url:'goright',
		success: function(){
			/*setTimeout(function(){
				motorstop()
			}, 1000);*/
		}
	});
}

function goup(){
	$.ajax({
		url:'goup',
		success: function(){
			/*setTimeout(function(){
				motorstop()
			}, 1000);*/
		}
		});
	return false
}

function godown(){
	$.ajax({
		url:'godown',
		success: function(){
			/*setTimeout(function(){
				motorstop()
			}, 1000);*/
		}
	});
}

function updownstop(){
	$.ajax({
		url:'updownstop',
		success: function(){
			
		}
	});
}

function forbackstop(){
	$.ajax({
		url:'forbackstop',
		success: function(){
			
		}
	});
}
