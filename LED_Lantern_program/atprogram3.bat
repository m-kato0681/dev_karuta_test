cd /d %~dp0

atprogram -t stk500 -c com8 -i ISP -d atmega168pa program -c --verify -fl -f Document3.hex write -fs --values FFDEF8 -v write -lb --values CF -v

pause

