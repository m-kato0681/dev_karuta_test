cd /d %~dp0

atprogram -t stk500 -c com8 -i ISP -d atmega88pa program -c --verify -fl -f cleaner-bootloader.hex write -fs --values FFDEF8 -v write -lb --values CF -v

pause

