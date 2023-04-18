#!/usr/bin/node

class book {
    constructor (title, author, numPages) {
        this.title = title
        this.author = author
        this.numPages = numPages
    }

    get Info () {
        return `Author: ${this.author}, Title: ${this.title}`
    }
}