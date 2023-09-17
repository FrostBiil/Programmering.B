class UFO {
    // Constructor
    constructor(x, y, speed) {
        this.x = x;
        this.y = y;
        this.size = createVector(16, 8);
        this.speed = speed;
        this.image = UFOImages[0];
    }

    // Draw the UFO
    draw() {
        this.move();
        image(this.image, this.x, this.y, this.size.x, this.size.y);
    }

    // Move the UFO
    move() {
        this.x += this.speed;

        // If the UFO is out of the screen
        if (this.x < 0 || this.x > width) {
            ufoArray.splice(ufoArray.indexOf(this), 1); // Remove the UFO from the array
        }
    }

    Hit() {
        ufoArray.splice(ufoArray.indexOf(this), 1); // Remove the UFO from the array
        randomValue = Math.floor(Math.random() * 6) * 50 + 50; // Random value:50, 100, 150, 200, 250, 300
        addPoints(randomValue); // add points
    }
}