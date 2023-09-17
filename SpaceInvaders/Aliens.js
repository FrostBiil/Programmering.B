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