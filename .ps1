@echo off
setlocal

:: Create a temporary PowerShell script
set "psScript=%temp%\ball.ps1"
echo Add-Type -AssemblyName System.Windows.Forms > "%psScript%"
echo Add-Type -AssemblyName System.Drawing >> "%psScript%"
echo $form = New-Object Windows.Forms.Form >> "%psScript%"
echo $form.Text = "Bouncing Ball" >> "%psScript%"
echo $form.Width = 400 >> "%psScript%"
echo $form.Height = 400 >> "%psScript%"
echo $ball = New-Object Drawing.SolidBrush([Drawing.Color]::Red) >> "%psScript%"
echo $x = 10 >> "%psScript%"
echo $y = 10 >> "%psScript%"
echo $dx = 5 >> "%psScript%"
echo $dy = 5 >> "%psScript%"
echo $form.Add_Paint({ >> "%psScript%"
echo     param($sender, $e) >> "%psScript%"
echo     $e.Graphics.FillEllipse($ball, $x, $y, 20, 20) >> "%psScript%"
echo }) >> "%psScript%"
echo $timer = New-Object Windows.Forms.Timer >> "%psScript%"
echo $timer.Interval = 50 >> "%psScript%"
echo $timer.Add_Tick({ >> "%psScript%"
echo     $x += $dx >> "%psScript%"
echo     $y += $dy >> "%psScript%"
echo     if ($x -lt 0 -or $x -gt $form.ClientSize.Width - 20) { $dx = -$dx } >> "%psScript%"
echo     if ($y -lt 0 -or $y -gt $form.ClientSize.Height - 20) { $dy = -$dy } >> "%psScript%"
echo     $form.Invalidate() >> "%psScript%"
echo }) >> "%psScript%"
echo $timer.Start() >> "%psScript%"
echo [void]$form.ShowDialog() >> "%psScript%"

:: Run the PowerShell script
powershell -ExecutionPolicy Bypass -File "%psScript%"

:: Clean up
del "%psScript%"

endlocal
