# Uplay Offline Mode

Commandline for enabling/disabling offline mode for Ubisoft Uplay Client

## Features

- Appear as offline to your friends but still be able to access in-game online services.

Disabled Features
- Friend List (including invitation to game)
- News Section, Store

## Set-up

First download `upc_invisible.zip` [here!](
https://github.com/phwt/uplay-offline-mode/raw/master/python/build/exe.win32-3.6/upc_invisible.zip)

Administrator rights is required to run the program.

### 1. Run `add_rule.bat` with admin rights

The command will ask you did you install Uplay in its default location or not. If not you need to manually input the location of `upc.exe` in your PC

After that "UplayOfflineMode" ourbound rules will be created.

### 2. Run `enable_rule.bat` with admin rights

Rule is disabled by default you need to run this to enable it.

After you finish testing you can run `disable_rule.bat`(with admin rights) to disable them.

## How to use

After you have done the set-up step.

- Use `enable_rule.bat` to enable offline/invisible mode. (With admin rights)
- Use `disable_rule.bat` to disable offline/invisible mode. (With admin rights)

Note: Don't enable before you launch the game or your game will not be able to launch. And disable it before you close the game (for cloud synchronization)

Enabling this will not instantly put you in offline mode. It may took about 30s - 1m for you to be completely offline. Same for disabling it took about 30s - 1m to appear online again.
