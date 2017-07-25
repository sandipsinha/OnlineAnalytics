function CreateDataGrid(apidata){

    $('#fbgrid').w2grid({
        name: 'fbgrid',
        header: 'FaceBook AdSet Data',
        columns: [
            { field: 'campaign_id', caption: 'Campaign ID', size: '20%' , sortable: true},
            { field: 'adset_id', caption: 'Adset ID', size: '20%' , sortable: true},
            { field: 'date', caption: 'Date', size: '10%' , sortable: true},
            { field: 'bid_amount', caption: 'Bid Amount', size: '25%' , sortable: true},
            { field: 'daily_budget', caption: 'Daily Budget', size: '25%',sortable: true }
        ],
        records: apidata,
            show : {
            header         : false,
            toolbar        : true,
            footer         : true,
            columnHeaders  : true,
            lineNumbers    : true,
            expandColumn   : false,
            selectColumn   : false,
            emptyRecords   : true,
            toolbarReload  : false,
            toolbarColumns : true,
            toolbarSearch  : true,
            toolbarAdd     : false,
            toolbarEdit    : false,
            toolbarDelete  : false,
            toolbarSave    : false,
            selectionBorder: true,
            recordTitles   : true,
            skipRecords    : false
        },    
    });
}

function CreateBarChart(barData, BarChart){
    var Labels = _.map(barData, function(o){return 'Campaign ID :' + o.campaign_id + ' \n ' + 'AdSet ID :' + o.adset_id});
    BarChart.options.labels = Labels
    BarChart.setData(barData);
    BarChart.redraw();
  }

function toObject(arr) {
  var rv = {};
  for (var i = 0; i < arr.length; ++i)
    if (arr[i] !== undefined) rv[arr[i]] = arr[i];
  return rv;
}


function update_date_prompts(datearr, maxDate){
    var newOptions = toObject(datearr);
    var selectedOption = maxDate;
    var select = $('#datel');
    if(select.prop) {
     var options = select.prop('options');
    }
    else {
      var options = select.attr('options');
    }
    $('option', select).remove();

    $.each(newOptions, function(val, text) {
        options[options.length] = new Option(text, val);
    });
    select.val(selectedOption);
}




function getFBData(BarChart){
   
             $.ajax({
                    url : '/apiv1/fbad/bid_n_cap',
                    contentType: "application/json",
                    dataType: "json",
                    type: "GET",
                    success: function( data ) {
                  var tempData = JSON.stringify(data);
				          processedData = JSON.parse(tempData);
                  console.log('Just got the data ' + JSON.stringify(processedData));
                  CreateDataGrid(processedData);
                  var datesArray = _.pluck(processedData, 'date')
                  
                  var uniqDates = _.uniq(datesArray);
        
                  var maxDate = uniqDates.reduce(function(prev, current) {
                                return (prev.y > current.y) ? prev : current
                                });
                  var displayarray = _.filter(processedData, function(o){return o.date == maxDate})
                  
                  update_date_prompts(uniqDates, maxDate);
                  
                  CreateBarChart(displayarray, BarChart);
           
                  //Create the d3 line chart figure
                  Initd3Chart(processedData);
          
}});

                  
}