# Load necessary assembly for message boxes
Add-Type -AssemblyName System.Windows.Forms

# Simulate script compilation
Write-Host "Compiling script..." -ForegroundColor Green
Start-Sleep -Seconds 2
Write-Host "Compilation failed!" -ForegroundColor Red
Start-Sleep -Seconds 1

# Initialize window counter
$windowCount = 0

# Function to create glitched message windows
function Show-GlitchedWindow {
    param (
        [string]$message,
        [string]$title
    )
    [System.Windows.Forms.MessageBox]::Show($message, $title, [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Error)
    $global:windowCount++
}

# Create glitched windows until the limit is reached
while ($windowCount -lt 100) {
    Show-GlitchedWindow -message "Error: Glitch $windowCount detected." -title "Compilation Error"
    Start-Sleep -Milliseconds 500
}

# End of game
Write-Host "You lost! Too many glitched windows!" -ForegroundColor Yellow

