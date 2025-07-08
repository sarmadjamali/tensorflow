# Ensure TLS 1.2 is used
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# Define paths and URLs
$pythonInstallerUrl = "https://www.python.org/ftp/python/3.10.13/python-3.10.13-amd64.exe"
$installerPath = "$env:TEMP\python-3.10.13-amd64.exe"
$pythonInstallDir = "C:\Python310"
$venvPath = "$env:USERPROFILE\tf-env"

# Step 1: Download Python 3.10.13
Write-Host "📥 Downloading Python 3.10.13 installer..."
Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $installerPath -UseBasicParsing

# Step 2: Install Python silently
Write-Host "⚙️ Installing Python 3.10.13 to $pythonInstallDir..."
St
