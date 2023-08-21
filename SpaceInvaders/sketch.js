// Constants
const anim_change_rate = 10;
const aliens_per_row = 8;

// Variables

// Integers
let anim_frame = 0;
let aliens_dir = 1;

// Booleans
let readyToShoot = true;

// Arrays
const spaceshipImages = [];
const alienImages = [];
const alienArray = [];
const bullets = [];

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
  Spaceship = new Spaceship(200, 350);

  // Create two rows of the same aliens
  for (let i = 0; i < 2; i++) {
    for (let j = 0; j < aliens_per_row; j++) {
      alienArray.push(new Alien(40 + j * 40, 50 + i * 40));
    }
  }
}

function draw() {
  background(0);
  for (let i = 0; i < alienArray.length; i++) {
    alienArray[i].display();
  }
  Spaceship.display();
  animationHandler();

  if (keyIsDown(32) && readyToShoot) {
    Spaceship.shoot();
    readyToShoot = false;
  }

  if (bullets !== undefined) {
    for (let i = 0; i < bullets.length; i++) {
      bullets[i].display();
    }
  }
}

function animationHandler() {
  anim_frame++;
  if (anim_frame % anim_change_rate === 0) {
    Spaceship.animate();

    for (let i = 0; i < alienArray.length; i++) {
      alienArray[i].animate();
    }
  }
}

// Create an alien class
class Alien {
  constructor(x = 200, y = 200) {
    this.x = x;
    this.y = y;
    this.size = 40;
    this.speed = 2;
    this.direction = 0;
    this.image = alienImages[0];
  }

  // Display the alien
  display() {
    this.display();
    image(this.image, this.x, this.y, this.size, this.size);
  }

  // Display the alien
  display() {
    image(this.image, this.x, this.y, this.size, this.size);
  }

  // Move the alien from side to side
  move() {

  }

  // Animation of the alien
  animate() {
    const currentIndex = alienImages.indexOf(this.image);
    const nextIndex = (currentIndex + 1) % alienImages.length;
    this.image = alienImages[nextIndex];
  }
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

  // Display the spaceship
  display() {
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
    bullets.push(new Bullet(this.x, this.y));
  }
}

class Bullet {
  constructor(x = 200, y = 300, size = 10, speed = 2) {
    this.x = x;
    this.y = y;
    this.size = size;
    this.speed = speed;
  }

  // Display the bullet
  display() {
    this.move();

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
}
