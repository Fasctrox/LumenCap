$(document).ready(function() {

	$("#id_docfile").on("change", function(){

		this.form.submit()

	});
	$("#search").on('keyup',function(){
		if($("#search").val() == ""){

			$(".searchresults").empty()

		}else{
		$.ajax({
			method:"GET",
			url:"/feed",
			data: {q:$("#search").val()},
			success:function(result){
				$(".searchresults").empty()
				for (var i in result){
					console.log(result[i].name);
					$(".searchresults").append("<a class = 'waves-effect waves-light fullwidth result blue ' href = '/list/"+result[i].name+"' ><p class = 'white-text'>"+ result[i].name +"</p></a>")
				}
			},
			error:function(e){
				console.log(e.responseText)
			}

		})}

	});
	$(".dropdown-button").dropdown();

});

