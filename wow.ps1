function Start-FakeGlitch {
    $colors = @("Red", "Green", "Blue", "Yellow", "Cyan", "Magenta")
    $duration = 1  # Duration of glitch effect in seconds

    while ($true) {
        $randomColor = Get-Random -InputObject $colors
        Write-Host -ForegroundColor $randomColor "Glitching..."
        Start-Sleep -Seconds $duration
    }
}

Start-FakeGlitch