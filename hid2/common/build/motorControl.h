#ifndef __MOTORCONTROL_H__
#define __MOTORCONTROL_H__

//#defineよりconstとして定義したほうが、後で参照しやすかったり、重複宣言を回避したりできるので便利

//DCモーターの回転を数字で定義
const byte FORWARD          = 0;
const byte BACKWARD         = 1;
const byte STOP             = 2;
#define PIN_RIGHT_A  5
#define PIN_RIGHT_B  6
#define PIN_LEFT_A   9
#define PIN_LEFT_B  10

//|IN_A1|IN_B1|OUT_A1|OUT_B1|FUNCTION|ROATATION|
//|    0|    0|     0|     0|STOP    |STOP     |
//|    1|    0|     1|     0|FORWARD |NORMAL   |
//|    0|    1|     0|     1|BACKWARD|REVERSE  |
//|    1|    1|     0|     0|BREAK   |BREAK    |

void initMotor();
void leftMotorControl(byte rotation);
void leftMotorPower(byte power);
void rightMotorControl(byte rotation);
void rightMotorPower(byte power);
void motorControl(byte controlL, byte controlR);

#endif

