@echo off
netsh advfirewall firewall set rule name="UplayOfflineMode" new enable=yes
echo "UplayOfflineMode" rule enabled
pause