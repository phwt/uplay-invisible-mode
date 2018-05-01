@echo off
echo Default uplay directory is "%ProgramFiles% (x86)\Ubisoft\Ubisoft Game Launcher\upc.exe".
CHOICE /M "Use default uplay directory?"
IF "%ERRORLEVEL%"=="1" GOTO UserDefault
IF "%ERRORLEVEL%"=="2" GOTO UserCustom
GOTO end

:UserDefault
echo Presets : "Default"
netsh advfirewall firewall add rule name="UplayOfflineMode" dir=out action=block program="%ProgramFiles% (x86)\Ubisoft\Ubisoft Game Launcher\upc.exe" enable=no
echo Firewall Outbound Rule "UplayOfflineMode" added. Enabled = no.
GOTO end

:UserCustom
echo Presets : "Custom"
set /P path=Enter Path: 
set usePath="%path%"
netsh advfirewall firewall add rule name="UplayOfflineMode" dir=out action=block program=%usePath% enable=no
echo Firewall Outbound Rule "UplayOfflineMode" added. Enabled = no.
echo Custom path : %usePath%
GOTO end

:end
pause