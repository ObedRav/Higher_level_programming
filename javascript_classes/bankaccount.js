#!/usr/bin/node

class BankAccount {
    constructor (balance, owner) {
        this.#balance = balance
        this.owner = owner
    }

    deposit (money) {
        this.#balance += money
    }

    withdraw (money) {
        if (this.#balance >= money) {
            this.#balance -= money
        } else {
            console.log("Not enoght monet")
        }
    }

    get balance () {
        return this.#balance
    }
}