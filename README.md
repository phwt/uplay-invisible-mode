# Uplay Invisible Mode

Add Invisible mode for your Uplay client.

## Features

- **Invisibility** Appear as offline to your friends but still be able to access in-game online services.

Disabled Features
- Friend List (including an invitation to the game)
- News Section, Store

## How it works?

The application will block the connection of `upc.exe` which transmit your online status to your friends. Your game connection will not be affected as this only blocks Uplay Client connection.

## Set-up

#### [Download the latest release here](https://github.com/phwt/uplay-invisible-mode/releases)

### 1. Extract ALL files from .zip file

You will extract some files and folders including `upcinvisible.exe` file.

![The files](https://raw.githubusercontent.com/phwt/uplay-offline-mode/master/img/00_files.JPG)

**There are a lot of files extracted. So I recommend to place the files somewhere and create a shortcut for `upcinvisible.exe` from there**

### 2. Run `upcinvisible.exe` with admin rights

The application will prompt you to select `upc.exe` from your Uplay installation folder (Default path: `C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\upc.exe`) and Windows Firewall Outbound rule "Uplay Invisible Mode" will be created.

![Select upc.exe](https://raw.githubusercontent.com/phwt/uplay-offline-mode/master/img/01_exe_select.JPG)

### 3. Finish!

The application will close and you are now ready to use.

![Finish!](https://raw.githubusercontent.com/phwt/uplay-offline-mode/master/img/02_setup_finish.JPG)

## How to use

### 1. Run `upcinvisible.exe` with admin rights and launch Uplay client

You will see like this in the application do and not enable it yet.

![Main screen](https://raw.githubusercontent.com/phwt/uplay-offline-mode/master/img/03_mainscreen.JPG)

**In this phase you will still appear online to your friends**

### 2. Start the game and click `Enable` to enable invisible mode

Simply just click **Play** button at your game. **Do not enable until the `Synchronization your save games with the cloud` dialog disappear** after that you can click on `Enable`.

![Synchronization your save games with the cloud](https://raw.githubusercontent.com/phwt/uplay-offline-mode/master/img/04_uplay_sync.jpg)

**This will not instantly offline your Uplay status. It may take about a minute or half for you to completely appear offline to your friends.**

### 3. Enjoy!

You can check if it working or not by noticing Error appear at the bottom, Friend list appear as `Connecting...` and Store inaccessible.

![Example](https://raw.githubusercontent.com/phwt/uplay-offline-mode/master/img/offline_example.jpg)

If all this applies you are now completely invisible. Enjoy!

### 4. Disabling

When you have finished your game. Quit the game and click on `Disable` button (Like when enabling you will not immediately online). After your Uplay client has established the connection with the server. You can now sync your progress with the cloud.

## Built-With

- Python `3.6.3`
  - tkinter `8.6`
  - ~~pyinstaller `3.4`~~
  - cx_Freeze `5.0.2`

## Development setup

Install required library

    pip install cx_Freeze

### Directory Structure
- `upcinvisible.py` - Application's main file
- `uplay_icon.ico` - Application's icon file

### Build
Build the application using `cx_Freeze`

    py setup.py build

You will find your files at `\build\exe.win-amd64-3.6` and don't forget to put `uplay_icon.ico` along with the `.exe` file.
