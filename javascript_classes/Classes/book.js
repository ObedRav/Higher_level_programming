#!/usr/bin/node
module.exports = class Book {
  constructor (title, author) {
    this.title = title;
    this.author = author;
    this.pages = null;
  }

  get bookPages () {
    return function(pageNum) {
        if (this.pages[pageNum - 1]) {
            return this.pages[pageNum - 1];
        } else {
            return `Error: Page ${pageNum} does not exist in this book.`
        }
    };
  }

  set bookPages (content) {
    if (this.pages === null) {
      this.pages = [];
    }
    this.pages.push(content);
  }

  get numPages() {
    return this.pages.length
  }

  get info () {
    return `Author: ${this.author}, Title: ${this.title}`;
  }
};
