# PhotoSorter

This is a python script I wrote to organize my photos when unloading them from my Fujifilm camera when shooting both RAW and JPG formats. "Automate the boring things" they say...

## Requirements

This script was written using Python 3. Install Python 3 from https://www.python.org

This script requires compilation into a `.exe` for use as a Send To shortcut in Windows.

I used PyInstaller, which can be installed via pip: `pip install pyinstaller`.

This was built and tested on Windows. No guarantees this will be useful on other operating systems.

## How to run

The folder the file came from will be sorted. Files that do not end in .JPG or .RAF will not be affected by the script.

This script is designed to be run from the Send To menu on Windows. Once added to the Send To menu, it can be run by selecting a photo, right clicking, Show more options (Win11), Send To, Sort Photos (or whatever custom name you make for the shortcut).

Instructions on adding to the Send To menu can be found [here.](#Add-to-Send-To-menu-Windows)


## Theory of Operation/nitty-gritty

The Fujifilm X-T5 outputs two file types when saving RAW and JPEG files. The files end with .RAF for RAW files, and .JPG for JPG files. If your camera uses different file types, the file types can be edited in the `main.py` script on lines 17 (JPG) and 21 (RAW).

This script uses `sys.argv[1]` which means that the script will only run if a file is passed to it via the "Send To" menu on Windows. [Add to Send To on Windows](#Add-to-Send-To-menu-Windows)

The file structure below is the INPUT for the script, where the root folder to be sorted is labeled `Photo_folder`. 

```
Photo_folder
├── filename1.JPG
├── filename1.RAF
├── filename2.JPG
├── filename2.RAF
└── ...
```

The script will create two new folders, `JPG` and `RAW`, inside `Photo_folder`.

```
Photo_folder
├── JPG
│   ├── filename1.JPG
│   ├── filename2.JPG
│   └── ...
├── RAF
│   ├── filename1.RAF
│   ├── filename2.RAF
│   └── ...
└── ...
```

All files that do not end in .RAF or .JPEG/.JPG will not be moved.

## Add to Send To menu Windows
Note: I wrote these instructions before I realized Windows silently shuttered python scripts from being able to be added to the Send To menu. To run these via Send To menu, they need to be made into .exe files.

The easiest way I found was to install PyInstaller via pip. `pip install pyinstaller`

Navigate to the folder via Command Line.

Run `pyinstaller Sort_Photos.py`

The .exe file will be created and placed in the following path: `../PhotoSorter/dist/Sort_Photos/Sort_Photos.exe`

To add to the Send To menu on Windows:
* Download the GitHub repository
* Extract the files and place the PhotoSorter folder in a known location
	* The folder can be placed on a NAS if you are connected to the server when trying to run the script!
	* If using the NAS for hosting the script folder, Python will still need to be installed on the computer trying to run the script
* Run pyinstaller command above
* Find compiled .exe file in the location above
* Select .exe file
* Right-click, Show more options (Win11), Create Shortcut
* Rename the shortcut to a friendlier name, ex: "Sort Photos"
* Cut the shortcut to the clipboard
* Press `Win+R` to open the Run menu
* Type `shell:sendto` and press Enter
* Paste the shortcut in the folder that opens

[Test the script out!](#How-to-run)

