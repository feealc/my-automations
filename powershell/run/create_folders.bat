@echo off

title run create_folders

::powershell.exe ../create_folders.ps1 -showPressEnter $true -askForPath $true -askForConfirm $true
powershell.exe ../create_folders.ps1 -askForPath $true -askForConfirm $true

PAUSE