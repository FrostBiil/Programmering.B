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
const alienArray = [];
const bullets = [];
const bunkerArray = [];

//#endregion

// Load images
function preload() {
    // Load spaceship images
    for (let i = 1; i < 4; i++) {
        const img = loadImage(`Images/SpaceShips/img${i}.png`);
        if (img) {
            spaceshipImages.push(img);
        } else {
            console.error(`Failed to load image ship_${i}.png`);
        }
    }

    // Load Squid images
    for (let i = 1; i < 3; i++) {
        const img = loadImage(`Images/Squid/Img${i}.png`);
        if (img) {
            SquidImages.push(img);
        } else {
            console.error(`Failed to load image Img${i}.png`);
        }
    }

    // Load Crab images
    for (let i = 1; i < 3; i++) {
        const img = loadImage(`Images/Crab/Img${i}.png`);
        if (img) {
            CrabImages.push(img);
        } else {
            console.error(`Failed to load image Img${i}.png`);
        }
    }

    // Load Octopus images
    for (let i = 1; i < 3; i++) {
        const img = loadImage(`Images/Octopus/Img${i}.png`);
        if (img) {
            OctopusImages.push(img);
        } else {
            console.error(`Failed to load image Img${i}.png`);
        }
    }

    // Load bunker images
    for (let i = 1; i < 4; i++) {
        const img = loadImage(`Images/Bunker/Img${i}.png`);
        if (img) {
            bunkerImages.push(img);
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
        if ((alienArray[i].x - alienArray[i].speed <= 0 && aliens_dir == "left") || (alienArray[i].x + alienArray[i].size + alienArray[i].speed >= width && aliens_dir == "right")) {
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

class Alien {
    constructor(x = 200, y = 200) {
        this.x = x;
        this.y = y;
        this.size = 20;
        this.speed = 10;
        this.verticalSpeed = 20;
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
        this.y += this.verticalSpeed;
    }

    destroy() {
        // Remove the alien from the array
        alienArray.splice(alienArray.indexOf(this), 1);
    }
}

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
        this.size = 20;
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
        if (keyIsDown(LEFT_ARROW) && this.x > 0) { this.x -= this.speed; }
        if (keyIsDown(RIGHT_ARROW) && this.x < width - this.size) { this.x += this.speed; }
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
        bullets.push(new Bullet(this.x, this.y-this.size/2,));
    }
}

class Bullet {
    constructor(x = 200, y = 300, speed = 2) {
        this.x = x;
        this.y = y;
        this.sizex = 2;
        this.sizey = 4;
        this.speed = speed;
    }

    // Draw the bullet
    draw() {
        this.move();
        this.hitAlien();
        this.hitBunker();

        noStroke();
        fill(255);
        rect(this.x, this.y, this.sizex, this.sizey);
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
            if (dist(this.x, this.y, alienArray[i].x, alienArray[i].y) < alienArray[i].size/2) {
                alienArray[i].destroy()
                bullets.splice(bullets.indexOf(this), 1);
                readyToShoot = true;
            }
        }
    }

    // Check if the bullet hit a bunker
    hitBunker() {
        for (let i = 0; i < bunkerArray.length; i++) {
            if (dist(this.x, this.y, bunkerArray[i].x, bunkerArray[i].y) < bunkerArray[i].size) {
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
        this.size = 50;
        this.life = 3;
        this.image = bunkerImages[0];
    }

    // Draw 
    draw() {
        image(this.image, this.x, this.y, this.size, this.size);
    }

    // On hit
    hit() {
        this.life--;
        this.image = bunkerImages[3 - this.life];
        if (this.life === 0) this.destroy();
    }

    destroy() { bunkerArray.splice(bunkerArray.indexOf(this), 1); } // Remove the bunker from the array
}