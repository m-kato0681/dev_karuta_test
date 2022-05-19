'usestrict';

const childProcess = require('child_process');

const execProcess = (str_command, options) => {
    return new Promise((resolve, reject) => {
        childProcess.exec(str_command, options, (error, stdout, stderr) => {
            if (error) {
                reject(stderr);
            }
            else {
                resolve(stdout);
            }
        });
    });
};

module.exports = {
    execProcess
};
