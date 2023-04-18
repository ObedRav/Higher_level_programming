#!/usr/bin/node

class CuentaBancaria {
    #owner;
    #saldo;

    constructor(owner) {
        this.#owner = owner;
        this.#saldo = 0;
    }

    consultarSaldo() {
        return this.#saldo;
    }

    depositar(monto) {
        this.#saldo += monto;
    }

    retirar(monto) {
        if (this.#saldo < monto) {
            console.log(`Dinero insuficiente`);
        } else {
            this.#saldo -= monto;
        }
    }

    transferir (cuenta, monto) {
        if (this.#saldo < monto) {
            console.log(`Dinero insuficiente`);
        } else {
            this.retirar(monto)
            cuenta.depositar(monto)
        }
    }

    getOwner() {
        return this.#owner
    }

    setOwner(nuevoOwner) {
        this.#owner = nuevoOwner
    }
}

module.exports = class Banco {
    #nombre;
    #cuentas;

    constructor(nombre) {
        this.#nombre = nombre
        this.#cuentas = []
    }

    crearCuentaBancaria(owner) {
        const account = new CuentaBancaria(owner)
        this.#cuentas.push(account)
        return account
    }

    obtenerCuentaBancaria(owner) {
        const account = this.#cuentas.find((account) => account.getOwner() === owner)
        return account
    }

    cerrarCuenta(cuenta) {
        if (this.#cuentas.includes(cuenta)) {
            const index = this.#cuentas.indexOf(cuenta)
            this.#cuentas.splice(index, 1)
        } else {
            return `La cuenta no existe`
        }
    }

    depositar(owner, monto) {
        const account = this.obtenerCuentaBancaria(owner)
        account.depositar(monto)
    }

    retirar(owner, monto) {
        const account = this.obtenerCuentaBancaria(owner)
        account.retirar(monto)
    }
}