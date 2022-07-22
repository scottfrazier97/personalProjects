let a;
let inva;
let a2;
let inva2;
let vermin;
let vermax;
let hormin;
let hormax;

function setup() {
  cnv = createCanvas(1520, 600);
  frameRate(30);
  stroke(255);
  a = height / 2;
  inva = height / 2;
  a2 = width/2;
  inva2 = width/2;
  vermin = 0;
  vermax = 600;
  hormin = 0;
  hormax = 1520;
}

function draw() {
    background(51);
    r = random(255); // r is a random number between 0 - 255
    g = random(100,200); // g is a random number betwen 100 - 200
    b = random(100); // b is a random number between 0 - 100
    ab = random(200,255); // a is a random number between 200 - 255
  
    stroke(r,g,b,ab);
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

