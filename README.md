# Uplay Offline Mode

Commandline for enabling/disabling offline mode for Ubisoft Uplay Client

## Set-Up Guide

There are 3 .bat files in this repo.

- `add_rule.bat` - Add rule to Windows Firewall
- `disable_rule.bat` - Enable rule
- `enable_rule.bat` - Disable rule

Administrator rights is required to run command.

### 1. Run `add_rule.bat` with admin rights

This will simply create rule named `UplayOfflineMode` in Windows Firewall Outbound Rule.

Note : You need to edit `upc.exe` path if you didn't install Uplay Client in default location. (Default is `%ProgramFiles% (x86)\Ubisoft\Ubisoft Game Launcher\upc.exe`)

### 2. Run `enable_rule.bat` with admin rights

Rule is disabled by default you need to run this to enable it.

After you finish testing you can run `disable_rule.bat`(with admin rights) to disable them.
