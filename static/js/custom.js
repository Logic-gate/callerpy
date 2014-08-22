//sliders autoplay
	//intro slider
	$('#carousel_fade_intro').carousel({
		interval: 2500,
		pause: "false"
	})
	//works sliders
	$('#carousel_horizontal_slide, #carousel_vertical_slide, #carousel_fade_1, #carousel_fade_2').carousel({
		interval: false
	})

//make section height of window
	$(function(){
		$('#intro').css({'height':($(window).height())+'px'});
		$(window).resize(function(){
		$('#intro').css({'height':($(window).height())+'px'});
		});
	});

//custom scrollbar
	$(document).ready(
	function() {  
		$("html").niceScroll();
		}
	);

//contact form
	$(document).ready(function() {
	var options = {
	target: '.alert',
	beforeSubmit: showRequest,
	success: showResponse
	};
	$('#contactForm').ajaxForm(options);
	});
	function showRequest(formData, jqForm, options) {
	var queryString = $.param(formData);
	return true;
	}
	function showResponse(responseText, statusText)  {
	}
	$.fn.clearForm = function() {
		return this.each(function() {
		var type = this.type, tag = this.tagName.toLowerCase();
		if (tag == 'form')
			return $(':input',this).clearForm();
		if (type == 'text' || type == 'password' || tag == 'textarea')
			this.value = '';
		else if (type == 'checkbox' || type == 'radio')
			this.checked = false;
		else if (tag == 'select')
			this.selectedIndex = -1;
		});
	};

//smooth scroll on page
	$(function() {
		$('#more a, .nav a, .nav li a, .brand, #footer li a').bind('click',function(event){
		var $anchor = $(this);

		$('[data-spy="scroll"]').each(function () {
		var $spy = $(this).scrollspy('refresh')
		});

		$('html, body').stop().animate({
		scrollTop: $($anchor.attr('href')).offset().top -61
		}, 1500,'easeInOutExpo');

		event.preventDefault();
		});
	});

//gallery image hover tooltip trigger
	$("[data-thumb=tooltip]").tooltip();

//collapse menu on click on mobile and tablet devices
	$('.nav a').click(function () { $(".nav-collapse").collapse("hide") });