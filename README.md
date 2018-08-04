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

### 1. Extract ALL files from .zip file

Make sure you have all these files and folder.

    - lib
    - python36.dll
    - upcoffline.exe

### 2. Run `upcoffline.exe` with admin rights

You will get `Windows Firewall Outbound Rules "UplayOfflineMode" added` if your `upc.exe` file is in its default location. (Default location is: `C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\upc.exe`)

If not you will be prompted into pointing out the correct path of the `upc.exe` files.

*Example Valid Path - `K:/My Program/Ubisoft Game Launchery/upc.exe`*

**After that Windows Firewall Outbound rules "UplayOfflineMode" will be created.**

### 3. Finish!

The status will be shown and you are now ready to use!

## How to use

### 1. Launch Uplay and the game.

You need to launch Uplay and game before enable the rule or you will not be able to establish connection with its server. You can continue when you game is fully started.

**In this phase your Uplay will still appear online to your friends**

### 2. Run `upcoffline.exe` with admin rights

The status will be shown similar to this:

    Current Status
    Enabled: False
    
    Change Rule Status (0 = Disable, 1 = Enable, -1 = Exit): 

### 3. Enable the rule

Typing `1` then press `Enter` and the status will be shown similar to this:

    Rule Status Updated
    Enabled: True
    
    Change Rule Status (0 = Disable, 1 = Enable, -1 = Exit):

**This will not instantly offline your Uplay status. It may took about 30s to 1m for you to completely appear offline to your friends.**

### 4. Enjoy your game!

You can check the status by noticing Error Text appear at the bottom, Friend list appear as `Connecting...` and Store inaccessible.

![Example](https://raw.githubusercontent.com/phwt/uplay-offline-mode/master/offline_example.jpg)

If all this applies your Uplay are now completely offlined! Enjoy!

When you are done type in anything except `0` or `1` or just simply press the `X` button on top-right corner and the process will be terminated.

### Notes

- Don't enable before you launch the game or your game will not be able to launch. And disable it before you close the game (for cloud synchronization)
- Enabling this will not instantly put you in offline mode. It may took about 30s - 1m for you to be completely offline. Same for disabling it took about 30s - 1m to appear online again.
