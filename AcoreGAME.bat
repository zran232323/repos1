@echo off
setlocal enabledelayedexpansion

set reactorTemperature=25
set coolantSystemConnected=false
set reactorRunning=false
set coolantLevel=100
set coreStatus=normal

:menu
cls
echo ==============================
echo    Nuclear Reactor Control
echo ==============================
echo Reactor Status: 
if "%reactorRunning%"=="true" (
    echo Running
) else (
    echo Stopped
)
if %reactorTemperature% geq 100 (
    echo Critical
)
echo ==============================
echo 1. Connect Self-Destruct System
echo 2. Prime Self-Destruct System
echo 3. Connect Coolant System
echo 4. Check Reactor Temperature
echo 5. Enter Core Console
echo 6. Refill Coolant
echo 7. View Core
echo 8. Exit
echo ==============================
set /p choice="Enter your choice (1-8): "

if "%choice%"=="1" goto connectSelfDestruct
if "%choice%"=="2" goto primeSelfDestruct
if "%choice%"=="3" goto connectCoolantSystem
if "%choice%"=="4" goto checkTemperature
if "%choice%"=="5" goto enterCoreConsole
if "%choice%"=="6" goto refillCoolant
if "%choice%"=="7" goto viewCore
if "%choice%"=="8" goto exitGame
goto menu

:connectSelfDestruct
echo Self-destruct system connected.
pause
goto menu

:primeSelfDestruct
set /p confirm="Are you sure you want to prime the self-destruct system? (yes/no): "
if /i "%confirm%"=="yes" (
    echo Self-destruct system primed. Reactor will self-destruct in 10 seconds!
    set coreStatus=self-destruct
    for /l %%i in (10,-1,1) do (
        echo %%i seconds remaining...
        timeout /t 1 >nul
    )
    echo BOOM! The reactor has self-destructed.
    set reactorRunning=false
    pause
    goto exitGame
) else (
    echo Self-destruct system priming aborted.
    pause
    goto menu
)

:connectCoolantSystem
set coolantSystemConnected=true
echo Coolant system connected.
pause
goto menu

:checkTemperature
echo Current reactor temperature: %reactorTemperature%°C
pause
goto menu

:refillCoolant
set coolantLevel=100
echo Coolant refilled to 100%%.
pause
goto menu

:viewCore
cls
if "%coreStatus%"=="normal" (
    color 3F
    echo [Cyan Orb]
    echo    ___
    echo   /   ^
    echo  ^     ^
    echo   ^___^
) else if "%coreStatus%"=="meltdown" (
    color 5F
    echo [Purple Orb]
    echo    ___
    echo   /   ^
    echo  ^     ^
    echo   ^___^
) else if "%coreStatus%"=="critical" (
    color 4F
    echo [Red Orb]
    echo    ___
    echo   /   ^
    echo  ^     ^
    echo   ^___^
) else if "%coreStatus%"=="self-destruct" (
    color 5F
    echo [Purple Orb]
    echo    ___
    echo   /   ^
    echo  ^     ^
    echo   ^___^
)
pause
goto menu

:enterCoreConsole
cls
echo ==============================
echo    Core Console
echo ==============================
echo Type 'start' to start the reactor, 'shutdown' to prime the shutdown procedure, 'cv' to view the core, or 'exit' to return to the main menu.
:coreConsole
set /p command="Core Console: "
if /i "%command%"=="start" (
    if "%reactorRunning%"=="false" (
        call :compilationEffect "Startup"
        set reactorRunning=true
        set coreStatus=normal
        echo Reactor started successfully.
        start "" cmd /c call :monitorReactor
    ) else (
        echo Reactor is already running.
    )
) else if /i "%command%"=="shutdown" (
    call :compilationEffect "Shutdown"
    echo Shutdown procedure primed. Reactor will shut down in 10 seconds!
    for /l %%i in (10,-1,1) do (
        echo %%i seconds remaining...
        timeout /t 1 >nul
    )
    echo Reactor has been safely shut down.
    set reactorRunning=false
    goto menu
) else if /i "%command%"=="cv" (
    goto viewCore
) else if /i "%command%"=="exit" (
    echo Exiting Core Console...
    goto menu
) else (
    echo Invalid command. Please type 'start', 'shutdown', 'cv', or 'exit'.
)
goto coreConsole

:compilationEffect
set action=%1
echo Compiling %action% procedure...
timeout /t 1 >nul
echo Loading modules...
timeout /t 1 >nul
echo Initializing systems...
timeout /t 1 >nul
echo Checking dependencies...
timeout /t 1 >nul
echo Verifying integrity...
timeout /t 1 >nul
echo Finalizing %action% procedure...
timeout /t 1 >nul
echo %action% procedure complete.
goto :eof

:monitorReactor
:monitorLoop
timeout /t 5 >nul
set /a reactorTemperature+=5
if "%coolantSystemConnected%"=="true" (
    set /a reactorTemperature-=3
    set /a coolantLevel-=1
)
if %reactorTemperature% geq 100 (
    echo Warning: Reactor temperature critical! Immediate action required!
    set coreStatus=critical
)
if %coolantLevel% leq 0 (
    set coolantSystemConnected=false
    echo Warning: Coolant level depleted! Coolant system disconnected.
)
if "%reactorRunning%"=="true" goto monitorLoop
goto :eof

:exitGame
echo Exiting game...
pause
exit /b

