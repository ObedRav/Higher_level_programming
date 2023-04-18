#!/usr/bin/node
exports.esrever = function (list) {
    rev_list = []

    for (item of list) {
        rev_list.unshift(item)
    }

    return rev_list
}