let a;
let inva;
let a2;
let inva2;
let vermin;
let vermax;
let hormin;
let hormax;

function setup() {
  var canvasDiv = document.getElementById('myCanvas2');

  var width = canvasDiv.offsetWidth;
  var height = width/2.5;

  cnv = createCanvas(width, height);
  frameRate(30);
  stroke(255);
  a = height / 2;
  inva = height / 2;
  a2 = width/2;
  inva2 = width/2;
  vermin = 0;
  vermax = height;
  hormin = 0;
  hormax = width;
}

function draw() {
    background(51);
    r = 255;
  
    stroke(r);
    strokeWeight(10);

    line(0, a, width, a);
    line(0, inva, width, inva);

    line(a2, 0, a2, height);
    line(inva2, 0, inva2, height);

    a = a - 2;
    inva = inva + 2;

    a2 = a2 - 5;
    inva2 = inva2 + 5;

    if (a < vermin) {
      a = vermax;
    }

    if (inva > vermax) {
        inva = vermin;
    }

    if (a2 < hormin) {
        a2 = hormax;
    }
  
    if (inva2 > hormax) {
        inva2 = hormin;
    }
}

