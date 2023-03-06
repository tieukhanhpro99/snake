// Khởi tạo các biến
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var snake = [{ x: 10, y: 10 }]; // Mảng lưu trữ các đốt của con rắn
var food = { x: 0, y: 0 }; // Vị trí của mồi
var direction = "right"; // Hướng di chuyển ban đầu của con rắn
var score = 0; // Điểm số

// Vẽ một đốt của con rắn
function drawSegment(x, y) {
  ctx.fillStyle = "green";
  ctx.fillRect(x * 10, y * 10, 10, 10);
}

// Vẽ con rắn
function drawSnake() {
  for (var i = 0; i < snake.length; i++) {
    drawSegment(snake[i].x, snake[i].y);
  }
}

// Tạo mồi ngẫu nhiên trên màn hình
function createFood() {
  food.x = Math.floor(Math.random() * canvas.width / 10);
  food.y = Math.floor(Math.random() * canvas.height / 10);
}

// Vẽ mồi
function drawFood() {
  ctx.fillStyle = "red";
  ctx.fillRect(food.x * 10, food.y * 10, 10, 10);
}

// Kiểm tra va chạm với tường hoặc đuôi của con rắn
function checkCollision(x, y) {
  if (x < 0 || x >= canvas.width / 10 || y < 0 || y >= canvas.height / 10) {
    return true;
  }
  for (var i = 1; i < snake.length; i++) {
    if (snake[i].x === x && snake[i].y === y) {
      return true;
    }
  }
  return false;
}

// Di chuyển con rắn
function moveSnake() {
  var head = { x: snake[0].x, y: snake[0].y };
  switch (direction) {
    case "up":
      head.y--;
      break;
    case "down":
      head.y++;
      break;
    case "left":
      head.x--;
      break;
    case "right":
      head.x++;
      break;
  }
  if (checkCollision(head.x, head.y)) {
    clearInterval(interval);
    alert("Game over!");
    return;
  }
  snake.unshift(head);
  if (head.x === food.x && head.y === food.y) {
    score++;
    createFood();
  } else {
    snake.pop();
  }
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawSnake();
  drawFood();
  document.getElementById("score").innerHTML = score;
}

// Xử lý sự kiện khi nhấn phím
document.addEventListener("keydown", function(event) {
  switch (event.keyCode) {
    case 37: // left arrow
      if (direction !== "right") {
        direction = "left";
      }
      break;
    case 38: // up arrow
      if (direction !== "down") {
        direction = "up";
      }
      break;
    case 39: // right arrow
      if (direction !== "left") {
        direction = ""right";
}
break;
case 40: // down arrow
if (direction !== "up") {
direction = "down";
}
break;
}
});

// Bắt đầu trò chơi
createFood();
var interval = setInterval(moveSnake, 100);
