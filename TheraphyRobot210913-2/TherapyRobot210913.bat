cd /d %~dp0

%~dp0tools\atprogram -t stk500 -c com8 -i ISP -d atmega328p program -c --verify -fl -f %~dp0hex\TherapyRobot210913.hex write -fs --values FFDEFE -v write -lb --values FF -v

pause

