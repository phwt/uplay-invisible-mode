@echo off

net session >nul 2>&1
if %errorLevel% == 0 (
	netsh advfirewall firewall set rule name="UplayOfflineMode" new enable=no
	echo "UplayOfflineMode" rule enabled
	pause
) else (
	echo Administrator Priviliages required to run this task.
	pause
	exit
)