param(
    [string]$SourceDir = "\\wsl.localhost\Ubuntu-24.04\home\ysaadaoui\nettimer\windows_widget\rainmeter\NetTime",
    [string]$TargetRoot = "$env:USERPROFILE\Documents\Rainmeter\Skins"
)

$targetDir = Join-Path $TargetRoot "NetTime"

if (-not (Test-Path $SourceDir)) {
    throw "Source skin folder not found: $SourceDir"
}

New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
Copy-Item -Path (Join-Path $SourceDir "*") -Destination $targetDir -Recurse -Force

Write-Host "NetTime skin installed to: $targetDir"
Write-Host "Open Rainmeter > Manage > NetTime > Load NetTime.ini"
