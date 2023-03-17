#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
	  
	  // alternative method
    const newHeight = this.width;
    this.width = this.height;
    this.height = newHeight;

   //  [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
