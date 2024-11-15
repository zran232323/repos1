@echo off
setlocal enabledelayedexpansion

REM Game Settings
set "score=0"
set "lives=3"
set "level=1"
set "boss_level=5"
set "max_level=10"
set "triangle_pos_x=5"
set "triangle_pos_y=5"
set "triangle_dir=0"
set "upgrade_level=1"
set "triangle=^"
set "circle=O"
set "bullet=-"
set "boss_hp=5"
set "enemy_alive=1"
set "minion1_alive=0"
set "minion2_alive=0"
set "minion1_pos_x=1"
set "minion1_pos_y=1"
set "minion2_pos_x=10"
set "minion2_pos_y=10"
set "boss_pos_x=5"
set "boss_pos_y=8"

:main
cls
echo Score: %score% Lives: %lives% Level: %level% Upgrades: %upgrade_level%
call :draw
choice /c wasdqe /n /m "Move (WASD), Rotate (Q/E), Shoot (Space): " >nul
if %errorlevel%==1 set /a "triangle_pos_y-=1" & if !triangle_pos_y! LSS 1 set "triangle_pos_y=1"
if %errorlevel%==2 set /a "triangle_pos_y+=1" & if !triangle_pos_y! GTR 10 set "triangle_pos_y=10"
if %errorlevel%==3 set /a "triangle_pos_x-=1" & if !triangle_pos_x! LSS 1 set "triangle_pos_x=1"
if %errorlevel%==4 set /a "triangle_pos_x+=1" & if !triangle_pos_x! GTR 10 set "triangle_pos_x=10"
if %errorlevel%==5 call :rotate_left
if %errorlevel%==6 call :rotate_right

if %errorlevel%==7 call :shoot
if !enemy_alive! EQU 0 (
    call :enemy_defeated
    goto main
)

if %level% EQU %boss_level% (
    call :boss_ai
    goto main
)

set /a "enemy_pos-=1"
if !enemy_pos! LEQ !triangle_pos_x! (
    call :hit
) else (
    goto main
)

:draw
cls
set "line1=          "
set "line2=          "
set "line3=          "
set "line4=          "
set "line5=          "
set "line6=          "
set "line7=          "
set "line8=          "
set "line9=          "
set "line10=         "

REM Draw player
set "line!triangle_pos_y!=!line!triangle_pos_y:~0,!triangle_pos_x!!triangle!!line!triangle_pos_y:~!triangle_pos_x!+1!"

REM Draw boss
if !enemy_alive! EQU 1 set "line!boss_pos_y!=!line!boss_pos_y:~0,!boss_pos_x!!circle!!line!boss_pos_y:~!boss_pos_x!+1!"

REM Draw minions if alive
if !minion1_alive! EQU 1 set "line!minion1_pos_y!=!line!minion1_pos_y:~0,!minion1_pos_x!!circle!!line!minion1_pos_y:~!minion1_pos_x!+1!"
if !minion2_alive! EQU 1 set "line!minion2_pos_y!=!line!minion2_pos_y:~0,!minion2_pos_x!!circle!!line!minion2_pos_y:~!minion2_pos_x!+1!"

echo !line1!
echo !line2!
echo !line3!
echo !line4!
echo !line5!
echo !line6!
echo !line7!
echo !line8!
echo !line9!
echo !line10!
exit /b

:rotate_left
set /a "triangle_dir-=1"
if !triangle_dir! LSS 0 set "triangle_dir=3"
call :update_triangle
exit /b

:rotate_right
set /a "triangle_dir+=1"
if !triangle_dir! GTR 3 set "triangle_dir=0"
call :update_triangle
exit /b

:update_triangle
if !triangle_dir! EQU 0 set "triangle=^"
if !triangle_dir! EQU 1 set "triangle=>"
if !triangle_dir! EQU 2 set "triangle=v"
if !triangle_dir! EQU 3 set "triangle=<"
exit /b

:shoot
if !triangle_dir! EQU 0 call :bullet_up
if !triangle_dir! EQU 1 call :bullet_right
if !triangle_dir! EQU 2 call :bullet_down
if !triangle_dir! EQU 3 call :bullet_left
exit /b

:bullet_up
for /L %%y in (!triangle_pos_y!,-1,1) do (
    if %%y==!boss_pos_y! if !triangle_pos_x! EQU !boss_pos_x! set "enemy_alive=0"
)
exit /b

:bullet_right
for /L %%x in (!triangle_pos_x!,1,10) do (
    if %%x==!boss_pos_x! if !triangle_pos_y! EQU !boss_pos_y! set "enemy_alive=0"
)
exit /b

:bullet_down
for /L %%y in (!triangle_pos_y!,1,10) do (
    if %%y==!boss_pos_y! if !triangle_pos_x! EQU !boss_pos_x! set "enemy_alive=0"
)
exit /b

:bullet_left
for /L %%x in (!triangle_pos_x!,-1,1) do (
    if %%x==!boss_pos_x! if !triangle_pos_y! EQU !boss_pos_y! set "enemy_alive=0"
)
exit /b

:enemy_defeated
cls
echo You defeated the enemy!
set /a "score+=10"
set "enemy_alive=1"
set /a "level+=1"
if %level% EQU %boss_level% (
    call :boss_fight
) else (
    if %level% GTR %max_level% (
        echo You win the game! Final score: %score%
        pause
        exit
    ) else (
        goto main
    )
)
exit /b

:hit
cls
echo The enemy hit you!
set /a "lives-=1"
if %lives% LEQ 0 (
    echo Game Over! Your final score: %score%
    pause
    exit
)
goto main

:boss_fight
echo Boss fight! The boss can move in all directions, summon minions, and throw corrupted windows!
set /a "enemy_alive=1"
set "minion1_alive=0"
set "minion2_alive=0"
set "boss_hp=5"

:boss_loop
call :boss_ai
call :draw
call :shoot

if !enemy_alive! EQU 0 (
    set /a "boss_hp-=1"
    if !boss_hp! LEQ 0 (
        echo You defeated the boss! But the final phase begins...
        timeout /t 2 >nul
        call :final_phase
    ) else (
        set "enemy_alive=1"
        set "boss_pos_x=5"
        set "boss_pos_y=8"
        goto boss_loop
    )
)
goto boss_loop

:boss_ai
REM Simple AI for the boss to move randomly in any direction
set /a "move_direction=!random! %% 4"
if !move_direction! EQU 0 (
    set /a "boss_pos_y-=1"
    if !boss_pos_y! LSS 1 set "boss_pos_y=1"
)
if !move_direction! EQU 1 (
    set /a "boss_pos_y+=1"
    if !boss_pos_y! GTR 10 set "boss_pos_y=10"
)
if !move_direction! EQU 2 (
    set /a "boss_pos_x-=1"
    if !boss_pos_x! LSS 1 set "boss_pos_x=1"
)
if !move_direction! EQU 3 (
    set /a "boss_pos_x+=1"
    if !boss_pos_x! GTR 10 set "boss_pos_x=10"
)

REM Boss can summon minions or throw corrupted windows
set /a "action=!random! %% 3"
if !action! EQU 0 (
    call :summon_minions
)
if !action! EQU 1 (
    call :throw_corrupted_window
)
exit /b

:summon_minions
if !minion1_alive! EQU 0 (
    set "minion1_alive=1"
    set "minion1_pos_x=1"
    set "minion1_pos_y=1"
) else if !minion2_alive
else if !minion2_alive! EQU 0 (
    set "minion2_alive=1"
    set "minion2_pos_x=10"
    set "minion2_pos_y=10"
)
exit /b

:throw_corrupted_window
cls
echo *** ALERT! *** The boss throws a corrupted terminal window at you!
timeout /t 2 >nul
for /L %%i in (1,1,3) do (
    cls
    echo Corrupted Terminal Window!
    timeout /t 1 >nul
    cls
    echo ####################
    echo # ################ #
    echo ####################
    timeout /t 1 >nul
)
set /a "lives-=1"
if %lives% LEQ 0 (
    echo Game Over! The corrupted windows got you!
    pause
    exit
)
goto boss_loop
exit /b

:final_phase
cls
echo *** ALERT! *** The screen is breaking apart!
timeout /t 2 >nul

REM Simulate screen breaking
for /L %%i in (1,1,5) do (
    cls
    echo    O O O O O
    echo  O O O O O O O
    echo O O O O O O O O O
    echo  O O O O O O O O
    echo   O O O O O O O
    echo     O O O O O
    echo       O O O
    timeout /t 1 >nul
    cls
    echo    O O O O O
    echo  O O O O O O O
    echo O O O O O O O O O
    echo  O O O O O O O O
    echo   O O O O O O O
    echo     O O O O O
    echo       O O O
    timeout /t 1 >nul
)

echo The evil face of the virus appears! Move your window and destroy it!
echo Press any key to continue...
pause >nul

:virus_face
echo        #####
echo      #     #
echo     #       #
echo      # O O #
echo       #  ^ #
echo        #####
echo      The virus is defeated!
pause
exit
