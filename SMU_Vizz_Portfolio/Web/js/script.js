
var canvas = document.getElementById('myCanvas');
var context = canvas.getContext('2d');

const mouse = { x: 0, y: 0 };
function mouseEvents(e) {
  const bounds = canvas.getBoundingClientRect();
  mouse.x = e.pageX - bounds.left - scrollX;
  mouse.y = e.pageY - bounds.top - scrollY;
};

window.addEventListener("mousemove", mouseEvents);

xcenter = canvas.width/2;
ycenter = canvas.height/2;

// draw design at x,y and rotated by angle
function drawRotated(x, y, angle) {

  context.setTransform(1, 0, 0, 1, x, y);
  context.rotate(angle);
  
  //face
  context.fillStyle = '#ffc964 ';
  context.strokeStyle = 'black';
  context.lineWidth = 5;
  context.beginPath();
  context.arc(320, 240, 200, 0, 2 * Math.PI);
  context.fill();
  context.stroke();
  context.closePath();

  //eyes
  context.fillStyle = 'black';
  context.beginPath();
  context.arc(270, 175, 30, 0, 2 * Math.PI);
  context.fill();
  context.stroke();
  context.closePath();

  context.beginPath();
  context.arc(370, 175, 30, 0, 2 * Math.PI);
  context.fill();
  context.stroke();
  context.closePath();

  //mouth
  context.strokeStyle = 'black';
  context.lineWidth = 5;
  context.beginPath();
  context.arc(320, 240, 125, 0, -1 * Math.PI);
  context.stroke();
  context.closePath();

  //nose
  context.strokeStyle = 'black';
  context.lineWidth = 3;
  context.beginPath();
  context.arc(325, 255, 6.6, 0, -1 * Math.PI);
  context.stroke();
  context.closePath();
  context.stroke();

  
};

// render loop called 60 times a second
function update(timer) {
  context.setTransform(1, 0, 0, 1, 0, 0); // reset transform
  context.clearRect(0, 0, 1220, 1220);

  // get angle from center to mouse
  var angle = Math.atan2(mouse.y - 610, mouse.x - 610);

  // draw rotated design
  
  drawRotated(xcenter, ycenter, angle);
  requestAnimationFrame(update);
};
requestAnimationFrame(update);



