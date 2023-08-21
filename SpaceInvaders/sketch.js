// Constants
const Animation_frame_rate_change = 10;

// Variables
let anim_frame = 0;
let spaceship;
let alien;

// Arrays
const spaceshipImages = [];
const alienImages = [];

function preload() {
  // Load spaceship images
  for (let i = 0; i < 3; i++) {
    spaceshipImages.push(loadImage(`Images/SpaceShips/ship_${i}.png`));
  }

  // Load aliens images
  for (let i = 0; i < 5; i++) {
    alienImages.push(loadImage(`Images/Aliens/SpaceInvadersAliens_${i}.jpg`));
  }
}

function setup() {
  createCanvas(400, 400);
  Spaceship = new Spaceship(200, 350);
  Alien = new Alien(100, 100);
}

function draw() {
  background(220);
  Alien.display();
  Spaceship.display();
  animationHandler();
}

function animationHandler() {
  anim_frame++;
  if (anim_frame % Animation_frame_rate_change === 0) {
    Spaceship.animate();
    Alien.animate();
  }
}

// Create an alien class
class Alien {
  constructor(x = 200, y = 200) {
    this.x = x;
    this.y = y;
    this.size = 40;
    this.speed = 1;
    this.direction = 0;
    this.image = alienImages[0];
  }

  // Display the alien
  display() {
    this.move();
    image(this.image, this.x, this.y, this.size, this.size);
  }

  // Move the alien from side to side
  move() {
    if (this.direction === 0) {
      this.x += this.speed;
    } else if (this.direction === 1) {
      this.x -= this.speed;
    }

    if (this.x >= width - this.size) {
      this.direction = 1;
    } else if (this.x <= 0) {
      this.direction = 0;
    }
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
}
