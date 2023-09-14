//#region
// Constants
const anim_change_rate = 20;
const aliens_per_row = 8;
const aliens_space = 30;

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
const SquidImages = [];
const CrabImages = [];
const OctopusImages = [];
const bunkerImages = [];
const crabLaserImages = [];
const octopusLaserImages = [];
const squidLaserImages = [];
const laserImages = [];

const alienArray = [];
const bullets = [];
const bunkerArray = [];



//#endregion

// Load images
function preload() {
    loadImages(spaceshipImages, "Spaceship", 1);
    loadImages(SquidImages, "Squid", 2);
    loadImages(CrabImages, "Crab", 2);
    loadImages(OctopusImages, "Octopus", 2);
    loadImages(bunkerImages, "Bunker", 1)
    loadImages(crabLaserImages, "CrabLaser", 4)
    loadImages(octopusLaserImages, "OctopusLaser", 4)
    loadImages(squidLaserImages, "SquidLaser", 4)
    loadImages(laserImages, "Laser", 1)

}

// function to load images in a loop
function loadImages(array, name, count) {
    for (let i = 0; i < count; i++) {
        const img = loadImage(`Images/${name}/Img${i}.png`);
        if (img) {
            array.push(img);
        } else {
            console.error(`Failed to load image Img${i}.png`);
        }
    }
}

// setup the game
function setup() {
    createCanvas(400, 400); // Create a canvas

    imageMode(CENTER); // Centering images

    spaceship = new Spaceship(200, 350); // Create a spaceship

    // Create 5 rows of the 3 different aliens
    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < aliens_per_row; j++) {
            if (i == 0) { alienArray.push(new Octopus(aliens_space + j * aliens_space, aliens_space + i * aliens_space)); } // Create the first row of aliens as Octopus
            if (i == 1 || i == 2) { alienArray.push(new Crab(aliens_space + j * aliens_space, aliens_space + i * aliens_space)); } // Create the second and third row of aliens as Crab
            if (i == 3 || i == 4) { alienArray.push(new Squid(aliens_space + j * aliens_space, aliens_space + i * aliens_space)); } // Create the fourth and fifth row of aliens as Squid
        }
    }

    for (let i = 0; i < 3; i++) { bunkerArray.push(new Bunker(50 + i * 150, 300)); } // creates 3 bunkers
}

// running the game
function draw() {
    background(0); // Set the background to black

    if (frameCount % 30 === 0) { // Every 30 frames
        if (moveDownAllAliens()) {
            for (let i = 0; i < alienArray.length; i++) { alienArray[i].moveDown(); }
        } else {
            for (let i = 0; i < alienArray.length; i++) { alienArray[i].move(); }
        }
    }

    for (let i = 0; i < alienArray.length; i++) { alienArray[i].draw(); }

    spaceship.draw();

    animHandler();

    if (keyIsDown(32) && readyToShoot) { spaceship.shoot(); }

    if (bullets) {
        for (let i = 0; i < bullets.length; i++) {
            bullets[i].draw();
        }
    }

    for (let i = 0; i < bunkerArray.length; i++) {
        bunkerArray[i].draw();
    }

    // alienShoot();
    if (frameCount % 60 === 0) {
        alienShoot();
    }
}

// cycling animations for the aliens
function animHandler() {
    anim_frame++;
    if (anim_frame % anim_change_rate === 0) {
        for (let i = 0; i < alienArray.length; i++) {
            alienArray[i].animate();
        }
    }
}

// function to make the aliens shoot
function alienShoot() {
    let randomAlien = alienArray[Math.floor(Math.random() * alienArray.length)];

    if (randomAlien instanceof Squid) {
        bullets.push(new Bullet(squidLaserImages, "alien", randomAlien.x, randomAlien.y + randomAlien.size.y / 2, -2));
    } else if (randomAlien instanceof Crab) {
        bullets.push(new Bullet(crabLaserImages, "alien", randomAlien.x, randomAlien.y + randomAlien.size.y / 2, -2));
    } else if (randomAlien instanceof Octopus) {
        bullets.push(new Bullet(octopusLaserImages, "alien", randomAlien.x, randomAlien.y + randomAlien.size.y / 2, -2));
    }
}

// function to make the squid shoot
function squidShoot() {
    
}

// function to make the crab shoot
function crabShoot() {
    
}

// function to make the octopus shoot
function octopusShoot() {
    
}


// function to handle when the aliens move down
function moveDownAllAliens() {
    for (let i = 0; i < alienArray.length; i++) {
        if ((alienArray[i].x - alienArray[i].speed <= 0 && aliens_dir == "left") || (alienArray[i].x + alienArray[i].size.x + alienArray[i].speed >= width && aliens_dir == "right")) {
            if (aliens_dir == "left") {
                aliens_dir = "right";
                return true;
            } else {
                aliens_dir = "left";
                return true;
            }
        }
    }
    return false;
}

// create a class for the aliens
class Alien {
    constructor(x = 200, y = 200) {
        this.x = x;
        this.y = y;
        this.size = createVector(16, 8);
        this.speed = 10;
        this.verticalSpeed = 20;
    }

    // Draw the alien
    draw() {
        image(this.image, this.x, this.y, this.size.x, this.size.y);
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
        this.y += this.verticalSpeed;
    }

    destroy() {
        // Remove the alien from the array
        alienArray.splice(alienArray.indexOf(this), 1);
    }
}

// create a class for the squid that extends the alien class
class Squid extends Alien {
    constructor(x = 200, y = 200) {
        super(x, y);
        this.image = SquidImages[0];
    }

    // Animation of the alien
    animate() {
        const currentIndex = SquidImages.indexOf(this.image);
        const nextIndex = (currentIndex + 1) % SquidImages.length;
        this.image = SquidImages[nextIndex];
    }
}

// create a class for the crab that extends the alien class
class Crab extends Alien {
    constructor(x = 200, y = 200) {
        super(x, y);
        this.image = CrabImages[0];
    }

    // Animation of the alien
    animate() {
        const currentIndex = CrabImages.indexOf(this.image);
        const nextIndex = (currentIndex + 1) % CrabImages.length;
        this.image = CrabImages[nextIndex];
    }
}

// create a class for the octopus that extends the alien class
class Octopus extends Alien {
    constructor(x = 200, y = 200) {
        super(x, y);
        this.image = OctopusImages[0];
    }

    // Animation of the alien
    animate() {
        const currentIndex = OctopusImages.indexOf(this.image);
        const nextIndex = (currentIndex + 1) % OctopusImages.length;
        this.image = OctopusImages[nextIndex];
    }
}

// Create a spaceship class
class Spaceship {
    constructor(x = 200, y = 300) {
        this.x = x;
        this.y = y;
        this.size = createVector(16, 8);
        this.speed = 1;
        this.direction = 0;
        this.image = spaceshipImages[0];
    }

    // Draw the spaceship
    draw() {
        this.move();
        image(this.image, this.x, this.y, this.size.x, this.size.y);
    }

    // Move the spaceship
    move() {
        if (keyIsDown(LEFT_ARROW) && this.x > 0) { this.x -= this.speed; }
        if (keyIsDown(RIGHT_ARROW) && this.x < width - this.size.x) { this.x += this.speed; }
    }

    // Animation of the spaceship
    animate() {
        const currentIndex = spaceshipImages.indexOf(this.image);

        const nextIndex = (currentIndex + 1) % spaceshipImages.length;

        this.image = spaceshipImages[nextIndex];
    }

    // Shoot a bullet
    shoot() {
        readyToShoot = false
        bullets.push(new Bullet( laserImages, "spaceship", this.x, this.y - this.size.y / 2,));
    }
}

class Bullet {
    constructor(image, shooter, x = 200, y = 300, speed = 2) {
        this.x = x;
        this.y = y;
        this.image = image[0];
        this.shooter = shooter;
        this.size = createVector(2, 8);
        this.speed = speed;
    }

    // Draw the bullet
    draw() {
        this.move();

        if (this.shooter == "spaceship") {
            this.hitAlien();
        }
            
        if (this.shooter == "alien")
        {
            this.hitSpaceship();
        }

        this.hitBunker();

        noStroke();
        fill(255);
        rect(this.x, this.y, this.size.x, this.size.y);
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
            if (dist(this.x, this.y, alienArray[i].x, alienArray[i].y) < alienArray[i].size.y / 2) {
                alienArray[i].destroy()
                bullets.splice(bullets.indexOf(this), 1);
                readyToShoot = true;
            }
        }
    }

    // Check if the bullet hit the spaceship
    hitSpaceship() {
        if (dist(this.x, this.y, spaceship.x, spaceship.y) < spaceship.size.y / 2) {
            bullets.splice(bullets.indexOf(this), 1);
        }
    }

    // Check if the bullet hit a bunker
    hitBunker() {
        for (let i = 0; i < bunkerArray.length; i++) {
            if (dist(this.x, this.y, bunkerArray[i].x, bunkerArray[i].y) < bunkerArray[i].size.y) {
                bullets.splice(bullets.indexOf(this), 1);
                bunkerArray[i].hit();

                readyToShoot = true;
            }
        }
    }
}

// Create a bunker class
class Bunker {
    constructor(x = 200, y = 250) {
        this.x = x;
        this.y = y;
        this.size = createVector(22, 16);
        this.life = 3;
        this.image = bunkerImages[0];
    }

    // Draw 
    draw() {
        image(this.image, this.x, this.y, this.size.x, this.size.y);
    }

    // On hit
    hit() {
        this.life--;
        console.log(this.life);
        if (this.life === 0) this.destroy();
    }

    destroy() { bunkerArray.splice(bunkerArray.indexOf(this), 1); } // Remove the bunker from the array
}