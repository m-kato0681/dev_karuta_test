'usestrict';

const execProcess = require('../util').execProcess;

const DEVICE = 'atmega88p';
const F_CPU = '12000000';
const ARDU_VER = '10803';
const MAIN_PROGRAM = 'userProgram';  /* The name of program file created by user. */

const CFLAGS = `-Iarduino/avr/cores/arduino -Iarduino/avr/variants/standard -Iusbdrv -I. -DDEBUG_LEVEL=0`;
const OBJ_SYSTEM = ['usbdrv/usbdrv.o', 'usbdrv/usbdrvasm.o', 'usbdrv/oddebug.o', 'usbImpl.o', `${MAIN_PROGRAM}.o`, 'list.o', 'waiting.o', 'main.o'];
const OBJ_OPTION = ['motorControl.o'];

const COMPILE = `${__dirname}/tools/avr/bin/avr-gcc -Wl,--gc-sections -Wall -Os -DARDUINO=${ARDU_VER} -DF_CPU=${F_CPU} ${CFLAGS} -mmcu=${DEVICE}`;
const CPPCOMPILE = `${__dirname}/tools/avr/bin/avr-g++ -Wall -Os -DARDUINO=${ARDU_VER} -DF_CPU=${F_CPU} ${CFLAGS} -mmcu=${DEVICE}`;
const OBJCOPY = `${__dirname}/tools/avr/bin/avr-objcopy -j .text -j .data -O ihex main.elf main.hex`;
const SIZE = `${__dirname}/tools/avr/bin/avr-size main.hex`;
const BHID = `${__dirname}/bootloadHID.exe`;

const build = async () => {
    /* Delete existing files. */
    let result = await execProcess(`del ${MAIN_PROGRAM}.o; del main.elf; del main.hex`, { cwd: __dirname });
    console.log(result);

    /* Build user-defined functions. */
    await execProcess(`${CPPCOMPILE} -c ${MAIN_PROGRAM}.cpp -o ${MAIN_PROGRAM}.o`, { cwd: __dirname }).catch(err => console.log(err));

    /* Link all files. */
    await execProcess(`${COMPILE} -o main.elf ${OBJ_SYSTEM.join(' ')}  ${OBJ_OPTION.join(' ')} core.a`, { cwd: __dirname }).catch(err => console.log(err));

    /* Object copy */
    await execProcess(OBJCOPY, { cwd: __dirname }).catch(err => console.log(err));

    /* Check Program size */
    result = await execProcess(SIZE, { cwd: __dirname });
    /* Parse result as following.
     0:   text    data     bss     dec     hex filename
     1:      0    3794       0    3794     ed2 main.hex */
    console.log(Number(result.split('\r\n')[1].split('\t')[3]));
}

const transfer = async (hexFile) => {
    await execProcess(`${BHID} -r ${hexFile}`, { cwd: __dirname });
}

module.exports = {
    exec: build,
    transfer: transfer
}
