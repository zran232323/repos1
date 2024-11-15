@echo off
setlocal enabledelayedexpansion

:: Initialize game variables
set "enemies_killed=0"
set "max_enemies=50"

:game_loop
cls
echo Evil Windows Hunt
echo Remaining enemies: %max_enemies%

:: Display moving evil windows
for /l %%i in (1,1,%max_enemies%) do (
    set /a "rand_x=!random! %% 80"
    set /a "rand_y=!random! %% 20"
    call :draw_window !rand_x! !rand_y!
)

:: Check if player closes an evil window
choice /c 123456 /n /t 1 /d 1 /m "Press a number key to close an evil window: "
if %errorlevel% lss 6 (
    set /a "enemies_killed+=1"
    echo Evil window closed!
    if %enemies_killed% geq %max_enemies% (
        echo Congratulations! You've defeated all evil windows.
        pause
    )
    goto :game_loop
) else (
    echo Out of attempts! Game over.
    pause
    exit
)

:draw_window
setlocal
set "x=%1"
set "y=%2"
for /l %%a in (1,1,3) do (
    for /l %%b in (1,1,5) do (
        if %%a==2 if %%b==3 (
            echo *|set /p=
        ) else (
            echo.|set /p=
        )
    )
    echo.
)
endlocal
goto :eof
