@echo off
setlocal enabledelayedexpansion

rem Define colors
set colors=0 1 2 3 4 5 6 7 8 9 A B C D E F

rem Loop to change colors
for /L %%i in (1,1,50) do (
    for %%c in (%colors%) do (
        color %%c
        timeout /t 0.1 >nul
    )
)

rem Reset color and run wininit
color 07
start cmd /c wininit
