#!/usr/bin/node

class vehicle {
    constructor (make, model, year) {
        this.make = make
        this.model = model
        this.year = year
    }

    description () {
        console.log(`This vehicle is ${model} from the ${year}`)
    }

    start () {
        console.log(`The vehicle has been started!`)
    }

    stop () {
        console.log(`The vehicle has been stopped`)
    }

}