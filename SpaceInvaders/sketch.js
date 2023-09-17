//#region
// Constant(s)
const anim_change_rate = 20;
const aliens_per_row = 8;
const aliens_space = 30;

// Variable(s)
let aliens_dir = "left";

// Integer(s)
let anim_frame = 0;
let points = 0;


// Boolean(s)
let readyToShoot = true;

// Image(s)
const spaceshipImages = [];
const SquidImages = [];
const CrabImages = [];
const OctopusImages = [];
const bunkerImages = [];
const crabLaserImages = [];
const octopusLaserImages = [];
const squidLaserImages = [];
const laserImages = [];
const UFOImages = [];

const alienLaserImages = {
    Squid: squidLaserImages,
    Crab: crabLaserImages,
    Octopus: octopusLaserImages,
};

// Object(s)
const alienArray = [];
const bulletsArray = [];
const bunkerArray = [];
const spaceshipArray = [];
const ufoArray = [];

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
    loadImages(UFOImages, "UFO", 1)

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

    spaceshipArray.push(new Spaceship(200, 350)); // Create a spaceship

    const alienTypes = [Octopus, Crab, Crab, Squid, Squid];
    const rows = 5;

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < aliens_per_row; j++) {
            const AlienType = alienTypes[i];
            alienArray.push(new AlienType(aliens_space + j * aliens_space, aliens_space + i * aliens_space));
        }
    }

    // creates 3 bunkers
    for (let i = 0; i < 3; i++) {
        bunkerArray.push(new Bunker(50 + i * 150, 300));
    }
}

// running the game
function draw() {
    background(0); // Set the background to black

    displayPoints(); // Display points

    if (frameCount % 30 === 0) { // Every 30 frames
        if (moveDownAllAliens()) {
            for (let i = 0; i < alienArray.length; i++) { alienArray[i].moveDown(); }
        } else {
            for (let i = 0; i < alienArray.length; i++) { alienArray[i].move(); }
        }
    }

    for (let i = 0; i < alienArray.length; i++) { alienArray[i].draw(); }

    for (let i = 0; i < spaceshipArray.length; i++) {
        spaceshipArray[i].draw();
    }

    animHandler();

    if (keyIsDown(32) && readyToShoot) {
        for (let i = 0; i < spaceshipArray.length; i++) {
            spaceshipArray[i].shoot();
        }
    }

    if (bulletsArray) {
        for (let i = 0; i < bulletsArray.length; i++) {
            bulletsArray[i].draw();
        }
    }

    for (let i = 0; i < bunkerArray.length; i++) {
        bunkerArray[i].draw();
    }

    for (let i = 0; i < ufoArray.length; i++) {
        ufoArray[i].draw();
    }

    // alienShoot();
    if (frameCount % 60 === 0) {
        alienShoot();
    }

    if (frameCount % 600 === 0) {
        console.log("ufo created");
        ufoArray.push(new UFO(0, 50, 1));
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
    const alienType = randomAlien.constructor.name;
    const laserImages = alienLaserImages[alienType];
    bulletsArray.push(new Bullet(laserImages, "alien", randomAlien.x, randomAlien.y + randomAlien.size.y / 2, -2));
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

// function for game over
function gameOver() {
    // Remove all the aliens
    for (let i = 0; i < alienArray.length; i++) {
        alienArray.splice(i, 1);
    }

    // Remove all the bullets
    for (let i = 0; i < bulletsArray.length; i++) {
        bulletsArray.splice(i, 1);
    }

    // Remove all the bunkers
    for (let i = 0; i < bunkerArray.length; i++) {
        bunkerArray.splice(i, 1);
    }

    // Remove the spaceship
    for (let i = 0; i < spaceshipArray.length; i++) {
        spaceshipArray.splice(i, 1);
    }

    // Display game over and the amount of points
    textSize(32);
    text("Game Over", 100, 100);
    text("Points: " + points, 100, 130);


    // Display restart
    textSize(16);
    text("Press R to restart", 100, 150);

    // Restart the game
    if (keyIsDown(82)) {
        setup();
    }
}

// function to display points
function displayPoints() {
    // Display points
    textSize(16);
    text("Points: " + points, 10, 20);
}

// function to add points
function addPoints(amount) {
    points += amount;
}
