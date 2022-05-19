// Modules to control application life and create native browser window
const { app, ipcMain, BrowserWindow, globalShortcut } = require('electron')

let firstTime = true;
let _sender
ipcMain.on('message', (event, arg) => {
    _sender = event.sender;
})

ipcMain.on('check_assoc', (event, arg) => {
    if (firstTime) {
        firstTime = false;
        let path = process.argv[1];
        // let path = 'D:\\tmp2\\tmp.sbd'; /* For debug */
        if (!(path === '.')) {
            if (path) {
                fs.readFile(path, (err, data) => {
                    _sender.send('openedByAssoc', data);
                });
            }
        }
    }
})

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow

function createWindow() {
    // Create the browser window.
    mainWindow = new BrowserWindow({
        width: 1200, height: 800, webPreferences: {
            nodeIntegration: true
        }
    })

    // and load the index.html of the app.
    mainWindow.loadFile('src/index.html')

    // Open the DevTools.
    mainWindow.webContents.openDevTools()
    // Remove Electron menu-bar
    mainWindow.removeMenu();

    // Emitted when the window is closed.
    mainWindow.on('closed', function () {
        // Dereference the window object, usually you would store windows
        // in an array if your app supports multi windows, this is the time
        // when you should delete the corresponding element.
        mainWindow = null
    })
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', () => {
    globalShortcut.register('CommandOrControl+Q', () => {
        app.quit();
    });
    createWindow();
})

// Quit when all windows are closed.
app.on('window-all-closed', function () {
    // On OS X it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

app.on('activate', function () {
    // On OS X it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (mainWindow === null) {
        createWindow()
    }
})

app.on('before-quit', function (e) {
    // TODO: Tentative action. App can't be closed by the close button or the exit menu. Another countermeasure is necessary.
    app.exit();
});
// TODO: Tentative action. App can't be closed by the close button or the exit menu. Another countermeasure is necessary.
ipcMain.on('exit', (event, arg) => {
    app.exit();
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
var command = require('./common/command-BTspeaker');  // Robot cleaner
var fs = require('fs');

// var debug = require('./debug').log(true);
// const serial = require('./serial');
// const util = require('./common/util');
// const messageMPY = require('./common/mpy-msg');
// const messageTestmode = require('./common/testmode-msg');
// const nameParser = require('./name-parser');

// let BAUDRATE = { MPY: 115200, TESTMODE: 921600 };
const hid = require('./app/hid');
const build = require('./common/build/userbuild');

ipcMain.on('connected', async (event, arg) => {
//     var msg = arg + " is choosed.";
//     debug(msg);

//     if (arg == 'Studuino:bit') {
//         try {
//             await connectToDevice('Studuino:bit', event.sender);
//         } catch (err) {
//             let status = err.reason == 'NOT_FOUND' ? 'device_not_found' : 'port_opened';
//             event.sender.send('statusChanged', status);
//             return;
//         }
//         event.sender.send('statusChanged', 'uploading_finished');
//         debug('Successfully connected to the device.');
//     }
    if (arg == 'bt-speaker') {
        ipcMain.on('disconnect', (event, arg) => {
            hid.stopSensorRead();
        });

        try {
            await hid.find('bt-speaker');
            let buf = Array(28).fill(0x00); //Array(ReportCount+1)
            buf[1] = 0xaa;
            buf[2] = 0x55;
            await hid.sendData(buf);
            await wait(2000);
            await build.transfer('testmode.hex');
            console.log('transfer finished');

            await wait(3000);
            await hid.find('bt-speaker');
            hid.registerCallback((data) => {
                event.sender.send('sensorChanged', { value: data });
            });
            hid.startSensorRead();
            event.sender.send('statusChanged', 'uploading_finished');
        } catch (err) {
            console.log(err);
            event.sender.send('statusChanged', 'device_not_found');
        }
    }
});

ipcMain.on('send',async (event, arg) => {
    // console.log(arg);
    console.log(Date.now()); //millisで表示
    // sendcommand(command.parsejson(arg)); // studuino
    // write(command.parse(arg), event);   // studuino:bit
    // console.log(command.parse(arg));   // studuino:bit
    // build.exec();
    await sendCommand(command.parse(arg));
    event.returnValue = 0;  //
});

ipcMain.on('saveCodeFile', async (event, arg) => {
    let script = arg.script;
    const outputFile = () => {
        return new Promise((resolve, reject) => {
            fs.writeFile(`${__dirname}/common/build/userProgram.cpp`, script, err => {
                if (err) {
                    reject(err);
                } else {
                    resolve();
                }
            });
        });
    };
    try{
        await outputFile();
        await build.exec();
        await hid.find('bt-speaker');
        let buf = Array(28).fill(0x00); //Array(ReportCount+1)
        buf[1] = 0xaa;
        buf[2] = 0x55;
        await hid.sendData(buf);
        hid.disconnect();
        await wait(3000);
        await build.transfer('main.hex');
        console.log('transfer finished');
        event.returnValue = 0;
    } catch (err) {
        console.log(err);
        event.returnValue = 0;
    }
});

// ipcMain.on('send-multi', (event, args) => {
//     let data = [];
//     for (let arg of args) {
//         // write(command.parse(arg), event);   // Studuino:bit
//         data.push(...command.parse(arg));
//     }
//     write(data, event);
// });

// ipcMain.on('saveCodeFile', async (event, arg) => {
//     // method1 UART経由（testmode）でファイル転送
//     let script = arg.script;
//     console.log('script: ', script);
//     let slot = arg.index;
//     let fileSize = Uint8Array.from(Buffer.from(script)).length + 1;  // 最後に追加する改行(LF)1つ分
//     console.log('File size: ', fileSize);
//     console.log('slot: ', slot);

//     // Connect to the device if not connected.
//     let onConnected = true;
//     if (!serial.isConnected()) {
//         onConnected = false;
//         try {
//             await connectToDevice('Studuino:bit', event.sender);
//         } catch (err) {
//             console.log(err);
//             event.sender.send('statusChanged', 'transfer_finished');
//             return;
//         }
//     }

//     // await util.wait(1500);
//     let data = [...messageTestmode.startUpload];
//     data.push(fileSize & 0xff);
//     data.push((fileSize >> 8) & 0xff);
//     data.push(((fileSize >> 16) & 0x0f) | (slot << 4));
//     data.push(util.calcSum(data));
//     await serial.send(data);  // Prepare to send script
//     await util.wait(100);

//     let newData = [];
//     for (let line of script.split(/\r\n|\r|\n/)) {
//         console.log(line);
//         newData.push(...Uint8Array.from(Buffer.from(line + '\n')));
//     }
//     let remaining = newData.length;
//     let next = newData;
//     while (remaining > 0) {
//         if (remaining < 256) {
//             await serial.send(next);
//             remaining = 0;
//         } else {
//             await serial.send(next.slice(0, 256));
//             next = next.slice(256);
//             remaining -= 256;
//         }
//         await util.wait(100);
//     }
//     if (!onConnected) {
//         await serial.disconnect();
//         ipcMain.removeAllListeners('disconnect');
//     }
//     event.sender.send('statusChanged', 'transfer_finished');
// });

// ipcMain.on('getScriptNames', async (event, arg) => {
//     // method1 UART経由（testmode）でファイル転送
//     // Connect to the device if not connected.
//     let onConnected = true;
//     if (!serial.isConnected()) {
//         onConnected = false;
//         try {
//             await connectToDevice('Studuino:bit', event.sender);
//         } catch (err) {
//             console.log(err);
//             event.returnValue = 0;
//             return;
//         }
//     }

//     let slot = 0;
//     let data = [...messageTestmode.get_script_name];
//     data.push(slot);
//     data.push(util.calcSum(data));
//     await util.wait(20);
//     await serial.send(data);  // Prepare to send script
//     await util.wait(500);
//     console.log(nameParser.getResult());
//     if (!onConnected) {
//         await serial.disconnect();
//         ipcMain.removeAllListeners('disconnect');
//     }
//     event.returnValue = 0;
// });

// ipcMain.on('updateFirmware', async (event, arg) => {
//     try {
//         if (serial.isConnected()) {
//             await serial.disconnect();
//             ipcMain.removeAllListeners('disconnect');
//         }
//         let comName = await serial.searchDevice('Studuino:bit');
//         for (let i = 0; i < arg.length; i++) {
//             await updateFirmware(arg[i], comName);
//         }
//     } catch (err) {
//         // event.sender.send('debug', 'Error: ' + err);
//         event.sender.send('statusChanged', 'finish_firmware_update');
//     }
//     event.sender.send('statusChanged', 'finish_firmware_update');
//     // event.returnValue = 0;
// });


// const write = async (data, event) => {
//     debug('Write: ' + data);  // Debug
//     if(serial.isConnected())
//         await serial.send(data);
//     await util.wait(10);
//     event.returnValue = 0;
// }

// const connectToDevice = (device, event_sender) => {
//     return new Promise(async (resolve, reject) => {
//         let comName;
//         try {
//             comName = await serial.searchDevice(device);
//             await serial.connect({ port: comName, baud: BAUDRATE.MPY });
//         } catch (err) {
//             reject(err);
//             return;
//         };
//         debug('COM port: ' + comName);

//         await serial.send([0x03]);
//         await util.wait(2000);  // To avoid starting communication just after a device being reset.
//         await serial.send([0x03]);
//         await serial.send(messageMPY.goTestMode);
//         await serial.disconnect();
//         await util.wait(100);

//         ipcMain.on('disconnect', (event, arg) => {
//             debug('Device disconnected');
//             serial.disconnect();
//             ipcMain.removeAllListeners('disconnect');
//         });
//         serial.registerCallback((data) => {
//             event_sender.send('sensorChanged', { value: data });
//         });
//         await util.wait(2000);  // Need to wait until the board restarting as testmode.
//         await serial.connect({ port: comName, baud: BAUDRATE.TESTMODE });
//         await serial.send(messageTestmode.ledMatrixOffAll);
//         resolve();
//     });
// }

let buf = Array(9).fill(0x00);
buf.unshift(0); /* Need for windows */

const sendCommand = async (command) => {
    if (!hid.isConnected()) return;

    buf.splice(1, command.length, ...command);
    console.log(buf);
    let retry = 5;
    let result = await hid.sendData(buf).catch(err => 'NG');
    while (result != 'OK' && retry > 0) {
        console.log(`NG-${retry}`);
        result = await hid.sendData(buf).catch(err => 'NG');
        await wait(50);
        retry--;
    }
    // console.log('send finish');
}

const wait = (duration) => {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve();
        }, duration);
    });
};
