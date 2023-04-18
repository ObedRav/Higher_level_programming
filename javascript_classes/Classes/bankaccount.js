#!/usr/bin/node

module.exports = class CuentaBancaria {
    #owner;
    #saldo;

    constructor (owner) {
        this.#owner = owner
        this.#saldo = 0 
    }

    consultarSaldo() {
        return this.#saldo
    }

    depositar(monto) {
        this.#saldo += monto
    }

    retirar(monto) {
        if (this.#saldo < monto) {
            console.log(`No hay fondos suficientes`)
        } else {
            this.#saldo -= monto
        }
    }

    getNombreCliente() {
        return this.#owner
    }

    setNombreCliente(nuevoNombre) {
        this.#owner = nuevoNombre
    }
}