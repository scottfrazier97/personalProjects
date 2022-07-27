const svg = d3.select('svg');

const width = parseFloat(svg.attr('width')); 
const height = +svg.attr('height'); 

const g = svg.append('g')  
    .attr('transform', `translate(${width / 2}, ${height / 2})`);

const circle = g.append('circle') 
    .attr('r', height / 2)    
    .attr('fill', '#ffc964')
    .attr('stroke', 'black')

const leftEye = g.append('circle')
    .attr('r', 35)    
    .attr('cx', -50)     
    .attr('cy', -40)
    .attr('fill', 'black')

const rightEye = g.append('circle')
    .attr('r', 35)    
    .attr('cx', 50)     
    .attr('cy', -40)
    .attr('fill', 'black')

const mouth = g.append('path')
    .attr('d', d3.arc()({     
        innerRadius: 170,
        outerRadius: 179, 
        startAngle: Math.PI / 1.65, 
        endAngle: Math.PI * 3/3.25
    }))

const leftBrow = g.append('path')
    .attr('d', d3.arc()({     
        innerRadius: 145,
        outerRadius: 157, 
        startAngle: Math.PI / -14.8, 
        endAngle: Math.PI / -4.9
    }))

const rightBrow = g.append('path')
    .attr('d', d3.arc()({     
        innerRadius: 145,
        outerRadius: 157, 
        startAngle: Math.PI / 14.8, 
        endAngle: Math.PI / 4.9
    }))

