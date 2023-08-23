//#region variables
// Constants
const anim_change_rate = 10;
const aliens_per_row = 8;

// Variables
let aliens_dir = "left";

// Objects
let spaceship;

// Integers
let anim_frame = 0;

// Booleans
let readyToShoot = true;

// Arrays
const spaceshipImages = [];
const alienImages = [];
const alienArray = [];
const bullets = [];

//#endregion

function preload() {
  // Load spaceship images
  for (let i = 0; i < 3; i++) {
    spaceshipImages.push(loadImage(`Images/SpaceShips/ship_${i}.png`));
  }

  // Load aliens images
  for (let i = 0; i < 2; i++) {
    alienImages.push(loadImage(`Images/Aliens/SpaceInvadersAliens_${i}.png`));
  }
}

function setup() {
  createCanvas(400, 400);
  spaceship = new Spaceship(200, 350);

  // Create two rows of the same aliens
  for (let i = 0; i < 2; i++) {
    for (let j = 0; j < aliens_per_row; j++) {
      alienArray.push(new Alien(40 + j * 40, 50 + i * 40));
    }
  }
}

function draw() {
  background(0);
  if (frameCount % 30 === 0) {
    if (moveDownAllAliens()) {
      for (let i = 0; i < alienArray.length; i++) {
        alienArray[i].moveDown();
      }
    } else {
      for (let i = 0; i < alienArray.length; i++) {
        alienArray[i].move();
      }
    }
  }
  for (let i = 0; i < alienArray.length; i++) {
    alienArray[i].draw();
  }
  spaceship.draw();
  animHandler();

  if (keyIsDown(32) && readyToShoot) {
    spaceship.shoot();
    readyToShoot = false;
  }

  if (bullets !== undefined) {
    for (let i = 0; i < bullets.length; i++) {
      bullets[i].draw();
    }
  }
}

function animHandler() {
  anim_frame++;
  if (anim_frame % anim_change_rate === 0) {
    spaceship.animate();

    for (let i = 0; i < alienArray.length; i++) {
      alienArray[i].animate();
    }
  }
}

function moveDownAllAliens() {
  for (let i = 0; i < alienArray.length; i++) {
    if (alienArray[i].x - alienArray[i].speed <= 0 && aliens_dir == "left" || alienArray[i].x + alienArray[i].size + alienArray[i].speed >= width && aliens_dir == "right") {
      if (aliens_dir == "left") {
        aliens_dir = "right";
      } else {
        aliens_dir = "left";
      }
      return true;
    }
  }
  return false;
}

class Alien {
  constructor(x = 200, y = 200) {
    this.x = x;
    this.y = y;
    this.size = 40;
    this.speed = 10;
    this.verticalSpeed = 20;
    this.image = alienImages[0];
  }

  // Draw the alien
  draw() {
    image(this.image, this.x, this.y, this.size, this.size);
  }

  // Move the alien from side to side and down
  move(speed = this.speed) {
    this.speed = speed;

    // Move from left to right
    if (aliens_dir == "right") {
      this.x += speed;
    }
    // Move from right to left
    else if (aliens_dir == "left") {
      this.x -= speed;
    }
  }

  // Move the alien down
  moveDown() {
    this.y += this.speed;
  }

  // Animation of the alien
  animate() {
    const currentIndex = alienImages.indexOf(this.image);
    const nextIndex = (currentIndex + 1) % alienImages.length;
    this.image = alienImages[nextIndex];
  }
}

class Squid extends Alien {
}

class Crap extends Alien {
}

class Octupus extends Alien {
}



// Create a spaceship class
class Spaceship {
  constructor(x = 200, y = 300) {
    this.x = x;
    this.y = y;
    this.size = 40;
    this.speed = 1;
    this.direction = 0;
    this.image = spaceshipImages[0];
  }

  // Draw the spaceship
  draw() {
    this.move();
    image(this.image, this.x, this.y, this.size, this.size);
  }

  // Move the spaceship
  move() {
    if (keyIsDown(LEFT_ARROW)) {
      this.x -= this.speed;
    }
    if (keyIsDown(RIGHT_ARROW)) {
      this.x += this.speed;
    }
  }

  // Animation of the spaceship
  animate() {
    const currentIndex = spaceshipImages.indexOf(this.image);
    const nextIndex = (currentIndex + 1) % spaceshipImages.length;
    this.image = spaceshipImages[nextIndex];
  }

  // Shoot a bullet
  shoot() {
    bullets.push(new Bullet(this.x + this.size / 2, this.y));
  }
}

class Bullet {
  constructor(x = 200, y = 300, size = 10, speed = 2) {
    this.x = x;
    this.y = y;
    this.size = size;
    this.speed = speed;
  }

  // Draw the bullet
  draw() {
    this.move();
    this.hitAlien();

    noStroke();
    fill(255);
    beginShape();
    vertex(this.x, this.y - this.size); // Top point
    quadraticVertex(this.x + this.size, this.y, this.x, this.y + this.size); // Curve to the right
    quadraticVertex(this.x - this.size, this.y, this.x, this.y - this.size); // Curve to the left
    endShape(CLOSE);
  }

  // Move the bullet
  move() {
    this.y -= this.speed;

    if (this.y < 0) {
      bullets.splice(bullets.indexOf(this), 1);
      readyToShoot = true;
    }
  }

  // Check if the bullet hit an alien
  hitAlien() {
    for (let i = 0; i < alienArray.length; i++) {
      if (dist(this.x, this.y, alienArray[i].x, alienArray[i].y) < this.size + alienArray[i].size) {
        alienArray.splice(i, 1);
        bullets.splice(bullets.indexOf(this), 1);
        readyToShoot = true;
      }
    }
  }
}
