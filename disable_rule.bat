@echo off
netsh advfirewall firewall set rule name="UplayOfflineMode" new enable=no
echo "UplayOfflineMode" rule disabled
pause