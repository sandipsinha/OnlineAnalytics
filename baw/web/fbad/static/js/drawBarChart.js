function createAverageChart(processedData) {
	var vis = d3.select("#visualisation"),
    WIDTH = 4000,
    HEIGHT = 5000,
    MARGINS = {
        top: 20,
        right: 20,
        bottom: 20,
        left: 50
    };
    var timelist = processedData.map(function(a) {return a.dates;});
    timelist.sort(function(a, b){
    return Date.parse(a) - Date.parse(b);
	});

	var max_time = timelist[timelist.length-1];
	var min_time = timelist[0];


    var players_array = processedData.map(function(a) {return a.no_of_players;});

    var max_players = _.max(players_array)
    var min_players = _.min(players_array)

    xScale = d3.scaleTime().range([MARGINS.left, WIDTH - MARGINS.right]).domain([new Date(min_time),new Date(max_time)])

    yScale = d3.scaleLinear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([min_players,max_players])
    

    xAxis = d3.axisBottom(xScale)
   

    yAxis = d3.axisLeft(yScale)
   

    vis.append("g")
    .attr("class","axis")
    .attr("transform", "translate(0," + HEIGHT + ")")
    .call(xAxis);



	vis.append("svg:g")
    .attr("class","axis")
    .call(yAxis);

    var lineGen = d3.line()
  	.x(function(d) {
    return xScale(new Date(d.dates));
  	})
	.y(function(d) {
    return yScale(d.no_of_players);
  	}).curve(d3.curveBasis);

  	vis.append('path')
  	.attr('d', lineGen(processedData))
  	.attr('stroke', 'green')
  	.attr('stroke-width', 2)
  	.attr('fill', 'none');

}