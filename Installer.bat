@echo off
title Compiler
color 0A

setlocal enabledelayedexpansion

:menu
cls
echo ========================================
echo          Compiler for GD_)GdD)A(9fhiu
echo ========================================
echo.
echo 1. Start Compilation
echo 2. Exit
echo Each file is named randomly
set /p choice=Choose an option (1-2): 

if %choice%==1 goto start
if %choice%==2 goto exit
goto menu

:start
cls
echo Compiling...
echo [System]dosdjghdshfpafikfjuhzsogj312
echo [System]htrfhfhmjnkrdfkeorkjsedoghsighdjk
echo [System]fsuifhsiufhdsiufghsiugfdsghsfsjfdc2
echo [System]fesdesufye89w34tyw97efhdsojtg9r043jta
echo [System]se98ecyct98cfit
echo [System]jsdiufjweiuafgj8ajgfrja9gjfd0gjafk
echo [System]mkguidhgidjgsfgispuih
echo [System]idsfiegdogsdisjgidgisg
echo [System]gdougjdofgjshfpsigdfdpsfpg
echo [System]ddjsfjsoifjfjdpgs
echo [System]NormalFile
echo [System]vjfudighfdighfdoigfdgduiog
echo [System]jhfsiufhgsdiogfhsd
echo [System]iogjdogjdogdogfhdig
echo [System]oijfsfsiogfjoigd
echo [System]vjfudighfdighfdoigfdgduiog
echo [System]jhfsiufhgsdiogfhsd
echo [System]iogjdogjdogdogfhdig
echo [System]oijfsfsiogfjoigd
echo [System]vjfudighfdighfdoigfdgduiog
echo [System]jhfsiufhgsdiogfhsd
echo [System]iogjdogjdogdogfhdig
echo [System]oijfsfsiogfjoigd
echo [System]vjfudighfdighfdoigfdgduiog
echo [System]jhfsiufhgsdiogfhsd
echo [System]iogjdogjdogdogfhdig
echo [System]oijfsfsiogfjoigd
echo [System]vjfudighfdighfdoigfdgduiog
echo [System]jhfsiufhgsdiogfhsd
echo [System]iogjdogjdogdogfhdig
echo [System]oijfsfsiogfjoigd
echo [System]vjfudighfdighfdoigfdgduiog
echo [System]jhfsiufhgsdiogfhsd
echo [System]iogjdogjdogdogfhdig
echo [System]oijfsfsiogfjoigd
echo [System]vjfudighfdighfdoigfdgduiog
echo [System]jhfsiufhgsdiogfhsd
echo [System]iogjdogjdogdogfhdig
echo [System]oijfsfsiogfjoigd
timeout /t 5 >nul
echo [System]sefgsdgksjhsighsfsdfd
timeout /t 1 >nul
echo [System]fsdgdfgiusjbvkdfjglkfjbldkbkdlfb
timeout /t 5 >nul
echo [System]gjddsgkldgl;dgkdgkfd;lcgkdf;l
timeout /t 5 >nul
echo [System]file1ds
timeout /t 5 >nul
echo [System]fkdsiofjslfjdslfdsjfjks
timeout /t 5 >nul
echo [System]INSTALLER CORRUPTED! PLEASE CLOSE WINDOW TO PREVENT COURUPTION
timeout /t 1 >nul
echo [System]sgfdsgdg
timeout /t 1 >nul
echo [System]fsdfsfsdf

timeout /t 3 >nul
echo Compilation corrupted...
timeout /t 2 >nul
goto glitchfix


:glitch
set /a glitchCount=0
set /a maxGlitches=20

:glitchLoop
set /a glitchCount+=1
set "chars=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:',.<>/?"
set "randomString="
for /l %%i in (1,1,50) do (
    set /a index=!random! %% 77
    set "randomString=!randomString!!chars:~!index!,1!"
)
start cmd /c "echo !randomString! && timeout /t 5 >nul && exit"
if !glitchCount! geq !maxGlitches! goto lose
echo.
set /p fix=Type "fix" to de-corrupt the window: 
if /i "%fix%"=="fix" goto glitchLoop
goto glitchLoop

:lose
cls
echo Too many glitchy windows! You lose.
pause
goto menu

:exit
exit
