function Initd3Chart(lineData) {
    var adsetArray = _.pluck(lineData, 'adset_id');

    var uniqadset = _.uniq(adsetArray);

    var options = {
        'daily_budget': 'daily_budget',
        'bid_amount': 'bid_amount'
    };

    var color = d3.scaleOrdinal(d3.schemeCategory10);
    // set the dimensions and margins of the graph
    //Width and height
    var w = 500;
    var h = 350;
    var padding = 50;



    
    // parse the date / time
    var parseTime = d3.timeParse("%Y-%m-%d");

    // set the ranges
    var xScale = d3.scaleTime().range([padding, w - padding * 2]);
    var yScale = d3.scaleLinear().range([h - padding, padding]);
    var dataGroupkeys = [];


    var svg = d3.select("#lchart").append("svg")
        .attr("width", w)
        .attr("height", h)

    ;



    // format the data
    var lineGen = d3.line()
        .x(function(d) {
            return xScale(parseTime(d.date));
        })
        .y(function(d) {
            return yScale(d.daily_budget);
        })
        .curve(d3.curveMonotoneX);

    // Scale the range of the data
    xScale.domain(d3.extent(lineData, function(d) {
        return parseTime(d.date);
    }));
    yScale.domain([0, d3.max(lineData, function(d) {
        return d.daily_budget;
    })]);


    // Add the X Axis
    svg.append("g")
        .attr("transform", "translate(0," + (h - padding) + ")")
        //.attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale).ticks(7))
        .selectAll("text")
        .style("text-anchor", "end")
        .attr("dx", "-.8em")
        .attr("dy", ".15em")
        .attr("transform", "rotate(-65)");

    // Add the Y Axis
    svg.append("g")
        .attr("transform", "translate(" + padding + ",0)")
        .call(d3.axisLeft(yScale));

    var dataGroup = d3.nest()
        .key(function(d) {
            return d.adset_id
        }).entries(lineData);

    //Remove Old data and map the new data
    var index = 1;
    _.map(dataGroup, function(d) {
        dataGroupkeys.push(d.key)
    });
    svg.selectAll(".line").remove();
    //Apply Transition
    var t = d3.transition()
        .duration(3000)
        .ease(d3.easeLinear);


    //Create lines 

    dataGroup.forEach(function(d, i) {

        svg.append('svg:path')
            .attr('d', lineGen(d.values))
            .attr('stroke', function() {
                return d.color = color(d.key);
            })
            .attr('stroke-width', 2)
            .attr('id', 'adset_id_' + d.key)
            .attr("class", "line")
            .transition(t)
            .attr('fill', function() {
                return color(d.key);
            });
        index += 1;
    });
    svg.append("text")
        .attr("x", (w / 2) - padding + 20)
        .attr("y", (h))
        .style("fill", "black")
        .attr("class", "legend")
        .style("text-anchor", "middle")
        .style("font-weight", 'bold')
        .text("Date");

    svg.append("text")
        .attr("text-anchor", "middle") // this makes it easy to centre the text as the transform is applied to the anchor
        .attr("transform", "translate(" + (padding / 2 - 10) + "," + (h / 2) + ")rotate(-90)") // text is drawn off the screen top left, move down and out and rotate
        .text("Daily Budget");

    var div = d3.select("body").append("div")   
    .attr("class", "tooltip")               
    .style("opacity", 0);

    svg.selectAll(".linePoint").remove();
    svg.selectAll("circle")
        .data(lineData)
        .enter().append("circle")
        .attr("class", "linePoint")
        .attr("cx", function(d, i) {
            return xScale(parseTime(d.date));
        })
        .attr("cy", function(d, i) {
            return yScale(d.daily_budget);
        })
        .attr("r", "3")
        .style("fill", function(d, i) {
            return color(d.adset_id);
        })
        .style("stroke", "grey")
        .style("stroke-width", "1px")
        .on("mouseover", function(d) {      
            div.transition()        
                .duration(200)      
                .style("opacity", .9);      
            div.html("Campaign ID: "  + d.campaign_id + "<br/>"  + "Adset ID: " +  d.adset_id + "<br/>"  + "Bid Amount: " +  d.bid_amount )  
                .style("left", (d3.event.pageX) + "px")     
                .style("top", (d3.event.pageY - 28) + "px");    
            })                  
        .on("mouseout", function(d) {       
            div.transition()        
                .duration(500)      
                .style("opacity", 0);   
        });



    



};