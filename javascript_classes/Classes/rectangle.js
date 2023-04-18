#!/usr/bin/node
class Rectangle {
    constructor (width, height) {
        this.width = width
        this.height = height
    }

    area () {
        this.height * this.width
    }

    perimeter () {
        2 * (this.height + this.width)
    }
}