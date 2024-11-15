@echo off
:loop
mode con: cols=80 lines=25
cls
echo Bouncing CMD!
ping -n 1 127.0.0.1 > nul
goto loop
