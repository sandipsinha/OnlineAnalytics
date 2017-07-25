function DrawChart(){

const fromDt = null
const toDt = null
$.ajax({
  			url : '/apiv1/solar/solardb',
  			contentType: "application/json",
  			dataType: "json",
  			type: "POST",
  			data: JSON.stringify({fdate:fromDt, tdate: toDt}),
			success: function( data ) {
				  var processedData = JSON.parse(JSON.stringify(data));
				  createAverageChart(processedData);

			}
  		});
          
}