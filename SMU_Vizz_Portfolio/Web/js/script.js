
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
  context.setTransform(1, 0, 0, 1, x, y); // move origin to center
  context.rotate(angle);

  // draw everything centered at (0, 0)
  // face
  context.fillStyle = '#ffc964';
  context.strokeStyle = 'black';
  context.lineWidth = 5;
  context.beginPath();
  context.arc(0, 0, 200, 0, 2 * Math.PI); // centered at 0,0
  context.fill();
  context.stroke();
  context.closePath();

  // eyes
  context.fillStyle = 'black';
  context.beginPath();
  context.arc(-50, -65, 30, 0, 2 * Math.PI); // left eye
  context.fill();
  context.stroke();
  context.closePath();

  context.beginPath();
  context.arc(50, -65, 30, 0, 2 * Math.PI); // right eye
  context.fill();
  context.stroke();
  context.closePath();

  // mouth
  context.strokeStyle = 'black';
  context.lineWidth = 5;
  context.beginPath();
  context.arc(0, 0, 125, 0, -1 * Math.PI);
  context.stroke();
  context.closePath();

  // nose
  context.strokeStyle = 'black';
  context.lineWidth = 3;
  context.beginPath();
  context.arc(5, 15, 6.6, 0, -1 * Math.PI); // slight offset
  context.stroke();
  context.closePath();
};

// render loop called 60 times a second
function update(timer) {
  context.setTransform(1, 0, 0, 1, 0, 0); // reset transform
  context.clearRect(0, 0, canvas.width, canvas.height);

  // get angle from center to mouse
  var angle = Math.atan2(mouse.y - ycenter, mouse.x - xcenter);

  // adjust angle to so that face is upright, always facing mouse
  angle -= Math.PI / 2;

  // draw rotated design
  drawRotated(xcenter, ycenter, angle);
  requestAnimationFrame(update);
};
requestAnimationFrame(update);



