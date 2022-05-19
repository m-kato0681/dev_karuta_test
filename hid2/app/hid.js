'usestrict';

const HID = require('node-hid');
const deviceInfo = require('./deviceInfo.json');
let devices = HID.devices();

let device = null;
let reportCount = 27
let fSensorRead = false;
let readCallback = null;

// let buf = Array(reportCount).fill(0x00);
// buf.unshift(0); /* Need for windows */

const getSensor = () => {
    return new Promise((resolve, reject) => {
        try {
            let recv = device.getFeatureReport(0x00, reportCount + 1);
            setTimeout(() => {
                resolve(recv);
            }, 100);
        } catch (err) {
            console.log('sensor read error');
            // console.log(err);
            reject(err);
        }
    });
}

const sendData = (data) => {
    return new Promise((resolve, reject) => {
        // data.unshift(0);  /* Necessary for windows */
        try {
            // device.write(data);  // Mac
            device.sendFeatureReport(data);  // Win
            setTimeout(() => {
                resolve('OK');
            }, 20);
        } catch (err) {
            reject(err);
        }
    });
}

module.exports = {
    // find: (vid, pid) => {
    isConnected: () => {
        return !!device;
    },
    find: (deviceName) => {
        const vid = deviceInfo[deviceName].vid;
        const pid = deviceInfo[deviceName].pid;
        reportCount = deviceInfo[deviceName].reportCount;

        return new Promise((resolve, reject) => {
            const devices = HID.devices();
            const deviceInfo = devices.find(elm => (elm.vendorId === vid && elm.productId === pid));
            if (deviceInfo) {
                device = new HID.HID(deviceInfo.path);
                resolve();
            } else {
                reject(`Device not found: ${vid} - ${pid}`);
            }
        });
    },
    disconnect: () => {
        device = null;
    },
    sendData: (buf) => {
        return new Promise((resolve, reject) => {
            if (device) {
                try {
                    console.log(buf);
                    device.sendFeatureReport(buf);
                    setTimeout(() => {
                        resolve('OK');
                    }, 20);
                } catch (err) {
                    reject(err);
                }
            } else {
                reject(`Device not found: ${vid} - ${pid}`);
            }
        });
    },
    startSensorRead: () => {
        fSensorRead = true;
        const asyncRead = async () => {
            while (fSensorRead) {
                let resp = await getSensor().catch(() => 'ERR');
                if (readCallback && resp != 'ERR') {
                    readCallback(resp);
                }
            }
            device = null;
        }
        asyncRead();
    },
    stopSensorRead: () => {
        fSensorRead = false;
        readCallback = null;
    },
    registerCallback: (callback) => {
        readCallback = callback;
    }
}
