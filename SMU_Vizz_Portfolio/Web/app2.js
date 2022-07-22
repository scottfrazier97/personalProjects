const data = [
    {"year2":1980,"gross2":2483666964},
    {"year2":1981,"gross2":2520064889},
    {"year2":1982,"gross2":3187580517},
    {"year2":1983,"gross2":2750004626},
    {"year2":1984,"gross2":3533092196},
    {"year2":1985,"gross2":3691509283},
    {"year2":1986,"gross2":3647511836},
    {"year2":1987,"gross2":4033434255},
    {"year2":1988,"gross2":4840385631},
    {"year2":1989,"gross2":6087250779},
    {"year2":1990,"gross2":6804235860},
    {"year2":1991,"gross2":6254770668},
    {"year2":1992,"gross2":7334167717},
    {"year2":1993,"gross2":8053959337},
    {"year2":1994,"gross2":9062925753},
    {"year2":1995,"gross2":9448305484},
    {"year2":1996,"gross2":9819527991},
    {"year2":1997,"gross2":13112275767},
    {"year2":1998,"gross2":11176023159},
    {"year2":1999,"gross2":13509638121},
    {"year2":2000,"gross2":13454129869},
    {"year2":2001,"gross2":15617625148},
    {"year2":2002,"gross2":17003436520},
    {"year2":2003,"gross2":17661932024},
    {"year2":2004,"gross2":18721747812},
    {"year2":2005,"gross2":17866609897},
    {"year2":2006,"gross2":18654070363},
    {"year2":2007,"gross2":20383671799},
    {"year2":2008,"gross2":21702162009},
    {"year2":2009,"gross2":23338680609},
    {"year2":2010,"gross2":23106595534},
    {"year2":2011,"gross2":24837686836},
    {"year2":2012,"gross2":25476190195},
    {"year2":2013,"gross2":25995848674},
    {"year2":2014,"gross2":26491482563},
    {"year2":2015,"gross2":26746011088},
    {"year2":2016,"gross2":28938844792},
    {"year2":2017,"gross2":28485248415},
    {"year2":2018,"gross2":28085289459},
    {"year2":2019,"gross2":30339653041},
    {"year2":2020,"gross2":2848298792}
  ]

const width = 1500;
const height = 500;
const margin = { top: 25, bottom: 25, left: 85, right: 0};

const svg = d3.select('#d3-container')
    .append('svg')
    .attr('height', height)
    .attr('width', width - margin.left)
    .attr('viewBox', [0,0,width,height])
    .style('background', 'rgb(64,72,91,255)');

const x = d3.scaleBand()
    .domain(d3.range(data.length))
    .range([margin.left, width - margin.right])
    .padding(0.1);

const y = d3.scaleLinear()
    .domain([0,30000000000])
    .range([height-margin.bottom, margin.top]);

svg
    .append('g')
    .attr('fill', 'white')
    .selectAll('rect')
    .data(data)
    .join('rect')
        .attr('x', (d,i) =>x(i))
        .attr('y', (d) => y(d.gross2))
        .attr('height', d => y(0) - y(d.gross2))
        .attr('width', x.bandwidth())
        .attr('class', 'rectangle')
        
function xAxis(g){
    g.attr('transform', `translate(0, ${height-margin.bottom})`)
    .call(d3.axisBottom(x).tickFormat(i => data[i].year2))
    .attr("font-size", "14px")
}

function yAxis(g){
    g.attr('transform', `translate(${margin.right}, 0)`)
        .call(d3.axisRight(y).ticks(null, data.format))
}

svg.append('g').call(xAxis)
svg.append('g').call(yAxis)
svg.node();


