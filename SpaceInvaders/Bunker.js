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