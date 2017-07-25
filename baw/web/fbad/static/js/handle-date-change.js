$(document).ready(function(){
$('#datel').change(function(){
    
  var displayarray = _.filter(processedData, function(o){return o.date == $('#datel :selected').val()})
  
  CreateBarChart(displayarray)
    
});
}
);
    