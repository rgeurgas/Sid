document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
});


$(document).ready(function(){
    $('.modal').modal();
    $('.chips').chips();
    $('.chips-placeholder').chips({
    	placeholder: 'Digite as tags',
    	secondaryPlaceholder: '+Tag',
  	});
  	
  	maxD = new Date();
  	
    $('.datepicker').datepicker({
    	format: 'yyyy-mm-dd',
    	maxDate: maxD,
    	yearRange: [1950, maxD.getFullYear()],
    });
   
	$('#excluir-links').click(function(){
		console.log("clickou");
		$('.open-link').addClass("vanish");
		$('.exclude-link').removeClass("vanish");
		$(this).addClass("vanish");
		$("#voltar-links").removeClass("vanish");
	});
	$('#voltar-links').click(function(){
		console.log("clickou 2");
		$('.open-link').removeClass("vanish");
		$('.exclude-link').addClass("vanish");
		$(this).addClass("vanish");
		$("#excluir-links").removeClass("vanish");
	});

	$('#excluir-lists').click(function(){
		console.log("clickou");
		$('.open-list').addClass("vanish");
		$('.exclude-list').removeClass("vanish");
		$(this).addClass("vanish");
		$("#voltar-lists").removeClass("vanish");
	});
	$('#voltar-lists').click(function(){
		console.log("clickou 2");
		$('.open-list').removeClass("vanish");
		$('.exclude-list').addClass("vanish");
		$(this).addClass("vanish");
		$("#excluir-lists").removeClass("vanish");
	});

	$('#excluir-summarys').click(function(){
		console.log("clickou");
		$('.open-summary').addClass("vanish");
		$('.exclude-summary').removeClass("vanish");
		$(this).addClass("vanish");
		$("#voltar-summarys").removeClass("vanish");
	});
	$('#voltar-summaries').click(function(){
		console.log("clickou 2");
		$('.open-summary').removeClass("vanish");
		$('.exclude-summary').addClass("vanish");
		$(this).addClass("vanish");
		$("#excluir-summaries").removeClass("vanish");
	});
});