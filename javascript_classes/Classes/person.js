#!/usr/bin/node

class person {
    constructor (firstName, lastName, age, gender) {
        this.firstName = firstName;
        this.lastName = lastName
        this.#age = age;
        this.gender = gender;
    }

    get fullName() {
        return `${this.firstName} ${this.lastName}`
    }

    set fullName(name) {
        [first, last] = name.split(' ')
        this.firstName = first
        this.lastName = last
    }

    getAge() {
        return this.#age;
      }
    
      setAge(age) {
        if (age >= 0 && age <= 120) {
          this.#age = age;
        } else {
          console.log("Invalid age.");
        }
      }

    introduce () {
        console.log(`Hi, my name is ${this.name}, i'm ${this.age} years old and my gender is ${this.gender}`)
    }
}