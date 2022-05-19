'use strict';

function calcSum(data) {
    let sum = 0;
    for (let i in data) {
        sum += data[i];
    }
    sum = 256 - sum % 256;
    return sum;
}

const parser = require('./BTspeaker.json');

module.exports = {
    parse: (obj) => {
        let command = parser.COMMAND[obj.id];
        let data = obj.data.map(elm => {
            if (elm.type == 'key') {
                return parser.DATA[elm.data];
            } else /*if (elm.type == 'value')*/ {
                return Number(elm.data);
            }
        });
        data.unshift(Number(command));
        // let msg = [part.id, part.function[func]]
        // if (obj.data) {
        //     msg.push(obj.data.length);
        //     msg.push(...obj.data);
        // } else {
        //     msg.push(0);
        // }
        // msg.push(calcSum(msg));
        return data;
    }
}
