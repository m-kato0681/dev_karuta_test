'usestrict';

const execProcess = require('../util').execProcess;

const DEVICE = 'atmega88p';
const F_CPU = '12000000';
const ARDU_VER = '10803';
const MAIN_PROGRAM = 'userProgram';  /* The name of program file created by user. */

const CFLAGS = `-Iarduino/avr/cores/arduino -Iarduino/avr/variants/standard -Iusbdrv -I. -DDEBUG_LEVEL=0`;
const SRC_SYSTEM = ['usbdrv/usbdrv.c', 'usbdrv/usbdrvasm.S', 'usbdrv/oddebug.c', 'usbImpl.c', 'list.cpp', 'waiting.cpp', 'main.cpp'];
const SRC_OPTION = ['motorControl.cpp'];

const COMPILE = `${__dirname}/tools/avr/bin/avr-gcc -Wl,--gc-sections -Wall -Os -DARDUINO=${ARDU_VER} -DF_CPU=${F_CPU} ${CFLAGS} -mmcu=${DEVICE}`;
const CPPCOMPILE = `${__dirname}/tools/avr/bin/avr-g++ -Wall -Os -DARDUINO=${ARDU_VER} -DF_CPU=${F_CPU} ${CFLAGS} -mmcu=${DEVICE}`;
const OBJCOPY = `${__dirname}/tools/avr/bin/avr-objcopy -j .text -j .data -O ihex main.elf main.hex`;
const SIZE = `${__dirname}/tools/avr/bin/avr-size main.hex`;
const BHID = `${__dirname}/bootloadHID.exe`;

const build = async () => {
    /* Delete existing files. */
    // for (let i in SRC_SYSTEM) {
    //     let result = await execProcess(`del ${OBJ_SYSTEM[i]}`, { cwd: __dirname });
    //     console.log(result);
    // }
    /* Build user-defined functions. */
    for (let i in SRC_SYSTEM) {
        const [target, postfix] = SRC_SYSTEM[i].split('.');
        if (postfix == "c") {
            await execProcess(`${COMPILE} -c ${target}.c -o ${target}.o`, { cwd: __dirname }).catch(err => console.log(err));
        } else if (postfix == "cpp") {
            await execProcess(`${CPPCOMPILE} -c ${target}.cpp -o ${target}.o`, { cwd: __dirname }).catch(err => console.log(err));
        } else {
            await execProcess(`${COMPILE} -x assembler-with-cpp -c ${target}.S -o ${target}.o`, { cwd: __dirname }).catch(err => console.log(err));
        }
    }
    for (let i in SRC_OPTION) {
        const [target, postfix] = SRC_OPTION[i].split('.');
        if (postfix == "c") {
            await execProcess(`${COMPILE} -c ${target}.c -o ${target}.o`, { cwd: __dirname }).catch(err => console.log(err));
        } else if (postfix == "cpp") {
            await execProcess(`${CPPCOMPILE} -c ${target}.cpp -o ${target}.o`, { cwd: __dirname }).catch(err => console.log(err));
        } else {
            await execProcess(`${COMPILE} -x assembler-with-cpp -c ${target}.S -o ${target}.o`, { cwd: __dirname }).catch(err => console.log(err));
        }
    }
}

const transfer = async (hexFile) => {
    await execProcess(`${BHID} -r ${hexFile}`, { cwd: __dirname });
}

build();
