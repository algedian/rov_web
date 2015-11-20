function camoff(){
	var img = $('#nemo')[0]
	img.src='/static/img/fiesta_spider.jpg'
}

function camon(){
	var img = $('#nemo')[0]
	img.src='/video_feed'
}

function ledon(){
	//$('button#ledon').click(function(){
		alert("led");
		$.ajax({
			url:'ledon',
			success: function(){
				alert("on");
			}
		})
		return false
	//});
}

function ledoff(){
	//$('button#ledoff').bind('click',function(){
		alert("led");
		$.ajax({
			url:'ledoff',
			success: function(){
				alert("off");
			}
		})
		return false
	//});
}
/*
$(document).ready(function(){
	namespace = '/btnclick';
	
	var socket = io.connect('http://' + document.domain + 
	':' + location.port + namespace);
	
	socket.on('connect', function(){
		socket.emit('my event', {data: 'I\'m connected!'});
	});
	
	$('form#btnoff').submit(fucntion(event){
		alert('off');
		//socket.emit('btn off event', );
		return false;
	});
});	
*/	    

