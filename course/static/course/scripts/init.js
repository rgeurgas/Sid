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
    	format: 'dd mmm, yyyy',
    	maxDate: maxD,
    	yearRange: [1950, maxD.getFullYear()],
    });
});