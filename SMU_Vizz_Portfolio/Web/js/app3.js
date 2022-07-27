var data2 = [
    {"genre2":"Action","gross3":"$243,435,855,754.00 "},
    {"genre2":"Adventure","gross3":"$45,916,596,693.00 "},
    {"genre2":"Animation","gross3":"$80,142,045,796.00 "},
    {"genre2":"Biography","gross3":"$20,729,581,801.00 "},
    {"genre2":"Comedy","gross3":"$97,175,468,462.00 "},
    {"genre2":"Crime","gross3":"$21,355,448,322.00 "},
    {"genre2":"Drama","gross3":"$57,150,648,537.00 "},
    {"genre2":"Family","gross3":"$2,157,897,417.00 "},
    {"genre2":"Horror","gross3":"$14,543,329,602.00 "},
    {"genre2":"Mystery","gross3":"$2,023,670,554.00 "},
    {"genre2":"Romance","gross3":"$188,394,999.00 "},
    {"genre2":"Sci-Fi","gross3":"$260,489,866.00 "},
    {"genre2":"Thriller","gross3":"$323,223,113.00 "},
    {"genre2":"Western","gross3":"$32,025,886.00 "}
  ];

var svg2 = d3.select("#pie"),
width2 = svg2.attr("width"),
height2 = svg2.attr("height"),
radius = 200;

var g = svg2.append("g")
       .attr("transform", "translate(" + width2 / 2 + "," + height2 / 2 + ")");

var ordScale = d3.scaleOrdinal()
                .domain(data2)
                .range(['#ffd384','#94ebcd','#fbaccc','#d3e0ea','#fa7f72']);

var pie = d3.pie().value(function(d) { 
    return d.gross3; 
});

var arc = g.selectAll("arc")
       .data(pie(data2))
       .enter();

var path = d3.arc()
         .outerRadius(radius)
         .innerRadius(0);


arc.append("path")
.attr("d", path)
.attr("fill", function(d) { return ordScale(d.data.genre2); });


var label = d3.arc()
          .outerRadius(radius)
          .innerRadius(0);

arc.append("text")
.attr("transform", function(d) { 
        return "translate(" + label.centroid(d) + ")"; 
})
.text(function(d) { return d.data.genre2; })
.style("font-family", "arial")
.style("font-size", 15);