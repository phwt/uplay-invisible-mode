# Uplay Invisible Mode

Add Invisible mode for your Uplay client.

## Features

- **Invisibility** Appear as offline to your friends but still be able to access in-game online services.

Disabled Features
- Friend List (including invitation to game)
- News Section, Store

## How it works?

The application will block the connection of `upc.exe` which transmit your online status to your friends. Your game connection will not be affected as this only blocks Uplay Client connection.

## Set-up

#### [Download the latest release here](https://github.com/phwt/uplay-invisible-mode/releases)

### 1. Extract ALL files from .zip file

You will extract some files and folders including `upcinvisible.exe` file.

### 2. Run `upcinvisible.exe` with admin rights

The application will prompt you to select `upc.exe` from your Uplay installation folder (Default path: `C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\upc.exe`) and Windows Firewall Outbound rule "Uplay Invisible Mode" will be created.

### 3. Finish!

The application will close and you are now ready to use.

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

### 5. When you are done.

When you have finished your game. Quit the game then type in `0` and press `Enter` to disable the rule. Same for enabling you will not instantly online. After Uplay client has established connection with the server. You can now sync your progress with the cloud.

## Built-With

- Python `3.7`
  - tkinter `8.6`
  - pyinstaller `3.4`

## Development setup

Install required library

    pip install PyInstaller

### Directory Structure
- `upcinvisible.py` - Application's main file
- `uplay_icon.ico` - Application's icon file

### Build
Build the application using `pyinstaller`

    pyinstaller --noconsole --icon=uplay_icon.ico upcinvisible.py
