#!/usr/bin/node
const Banco = require('./Banco.js');

// Creamos un nuevo banco
const miBanco = new Banco('Mi Banco');

const cuenta1 = miBanco.crearCuentaBancaria('Juan Pérez');
const cuenta2 = miBanco.crearCuentaBancaria('María González');
const cuenta3 = miBanco.crearCuentaBancaria('Pedro Rodríguez');

// Depositamos fondos en las cuentas
cuenta1.depositar(1000);
cuenta2.depositar(5000);
cuenta3.depositar(200);

// Consultamos el saldo de las cuentas
console.log(`Saldo de la cuenta de ${cuenta1.getOwner()}: ${cuenta1.consultarSaldo()}`);
console.log(`Saldo de la cuenta de ${cuenta2.getOwner()}: ${cuenta2.consultarSaldo()}`);
console.log(`Saldo de la cuenta de ${cuenta3.getOwner()}: ${cuenta3.consultarSaldo()}`);

// Transferimos fondos entre cuentas
cuenta1.transferir(cuenta2, 500);

// Consultamos el saldo de las cuentas después de la transferencia
console.log(`Saldo de la cuenta de ${cuenta1.getOwner()}: ${cuenta1.consultarSaldo()}`);
console.log(`Saldo de la cuenta de ${cuenta2.getOwner()}: ${cuenta2.consultarSaldo()}`);

// Cerramos la cuenta de Pedro Rodríguez
miBanco.cerrarCuenta(cuenta3);
