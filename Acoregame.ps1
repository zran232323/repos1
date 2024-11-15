$reactorTemperature = 25  # Initial temperature in degrees Celsius
$coolantSystemConnected = $false
$reactorRunning = $false
$coolantLevel = 100  # Initial coolant level
$logFile = "reactor_log.txt"

function Log-Event {
    param (
        [string]$message
    )
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$timestamp - $message" | Out-File -Append -FilePath $logFile
}

function Show-Menu {
    Clear-Host
    Write-Host "=============================="
    Write-Host "   Nuclear Reactor Control"
    Write-Host "=============================="
    Write-Host "Reactor Status: $([string]::Join(', ', @(
        if ($reactorRunning) { 'Running' } else { 'Stopped' }
        if ($reactorTemperature -ge 100) { 'Critical' }
    )))"
    Write-Host "1. Connect Self-Destruct System"
    Write-Host "2. Prime Self-Destruct System"
    Write-Host "3. Connect Coolant System"
    Write-Host "4. Check Reactor Temperature"
    Write-Host "5. Enter Core Console"
    Write-Host "6. Refill Coolant"
    Write-Host "7. Exit"
    Write-Host "=============================="
}

function Connect-SelfDestruct {
    Write-Host "Self-destruct system connected."
    Log-Event "Self-destruct system connected."
}

function Prime-SelfDestruct {
    Write-Host "Are you sure you want to prime the self-destruct system? (yes/no)"
    $confirmation = Read-Host
    if ($confirmation -eq 'yes') {
        Write-Host "Self-destruct system primed. Reactor will self-destruct in 10 seconds!"
        Log-Event "Self-destruct system primed."
        for ($i = 10; $i -ge 1; $i--) {
            Write-Host "$i seconds remaining..."
            Start-Sleep -Seconds 1
        }
        Write-Host "BOOM! The reactor has self-destructed."
        Log-Event "Reactor self-destructed."
        Stop-Job -Name "ReactorTemperatureJob"
        $global:reactorRunning = $false
    } else {
        Write-Host "Self-destruct system priming aborted."
        Log-Event "Self-destruct system priming aborted."
    }
}

function Connect-CoolantSystem {
    $global:coolantSystemConnected = $true
    Write-Host "Coolant system connected."
    Log-Event "Coolant system connected."
}

function Check-Temperature {
    Write-Host "Current reactor temperature: $reactorTemperature°C"
    Log-Event "Checked reactor temperature: $reactorTemperature°C"
}

function Refill-Coolant {
    $global:coolantLevel = 100
    Write-Host "Coolant refilled to 100%."
    Log-Event "Coolant refilled to 100%."
}

function CompilationEffect {
    param (
        [string]$action
    )
    Write-Host "Compiling $action procedure..."
    Start-Sleep -Seconds 1
    Write-Host "Loading modules..."
    Start-Sleep -Seconds 1
    Write-Host "Initializing systems..."
    Start-Sleep -Seconds 1
    Write-Host "Checking dependencies..."
    Start-Sleep -Seconds 1
    Write-Host "Verifying integrity..."
    Start-Sleep -Seconds 1
    Write-Host "Finalizing $action procedure..."
    Start-Sleep -Seconds 1
    Write-Host "$action procedure complete."
    Log-Event "$action procedure complete."
}

function Enter-CoreConsole {
    Clear-Host
    Write-Host "=============================="
    Write-Host "   Core Console"
    Write-Host "=============================="
    Write-Host "Type 'start' to start the reactor, 'shutdown' to prime the shutdown procedure, or 'exit' to return to the main menu."
    do {
        $command = Read-Host "Core Console"
        switch ($command) {
            'start' {
                if (-not $reactorRunning) {
                    CompilationEffect -action "Startup"
                    $global:reactorRunning = $true
                    Write-Host "Reactor started successfully."
                    Log-Event "Reactor started."
                    Start-Job -ScriptBlock {
                        while ($true) {
                            Start-Sleep -Seconds 5
                            $global:reactorTemperature += 5
                            if ($global:coolantSystemConnected) {
                                $global:reactorTemperature -= 3
                                $global:coolantLevel -= 1
                            }
                            if ($global:reactorTemperature -ge 100) {
                                Write-Host "Warning: Reactor temperature critical! Immediate action required!"
                                Log-Event "Reactor temperature critical!"
                            }
                            if ($global:coolantLevel -le 0) {
                                $global:coolantSystemConnected = $false
                                Write-Host "Warning: Coolant level depleted! Coolant system disconnected."
                                Log-Event "Coolant level depleted. Coolant system disconnected."
                            }
                        }
                    }
                } else {
                    Write-Host "Reactor is already running."
                    Log-Event "Attempted to start reactor, but it is already running."
                }
            }
            'shutdown' {
                CompilationEffect -action "Shutdown"
                Write-Host "Shutdown procedure primed. Reactor will shut down in 10 seconds!"
                Log-Event "Shutdown procedure primed."
                for ($i = 10; $i -ge 1; $i--) {
                    Write-Host "$i seconds remaining..."
                    Start-Sleep -Seconds 1
                }
                Write-Host "Reactor has been safely shut down."
                Log-Event "Reactor shut down."
                Stop-Job -Name "ReactorTemperatureJob"
                $global:reactorRunning = $false
                break
            }
            'exit' {
                Write-Host "Exiting Core Console..."
                Log-Event "Exited Core Console."
                break
            }
            default {
                Write-Host "Invalid command. Please type 'start', 'shutdown', or 'exit'."
                Log-Event "Invalid command entered in Core Console."
            }
        }
    } while ($command -ne 'exit')
}

do {
    Show-Menu
    $choice = Read-Host "Enter your choice (1-7)"
    switch ($choice) {
        1 { Connect-SelfDestruct }
        2 { Prime-SelfDestruct }
        3 { Connect-CoolantSystem }
        4 { Check-Temperature }
        5 { Enter-CoreConsole }
        6 { Refill-Coolant }
        7 { Write-Host "Exiting game..."; Log-Event "Game exited."; break }
        default { Write-Host "Invalid choice. Please select a valid option."; Log-Event "Invalid menu choice." }
    }
    Write-Host "Press Enter to continue..."
    Read-Host
} while ($choice -ne 7)

# Clean up any running jobs
Get-Job | Remove-Job
Log-Event "Cleaned up running jobs."
