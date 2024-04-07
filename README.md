# Gamecube Swiss Updater

Simple Python script to download the newest release of Swiss [https://github.com/emukidid/swiss-gc](https://github.com/emukidid/swiss-gc), extract the `DOL` file, renames it to `IPL.dol` and copies it to the
first detected mounted FAT32 USB/SD card

## Requirements

- Python 3.x installed
- Internet connection
- GameCube with Swiss homebrew software
- USB or microSD card (the only external drive plugged in)

## Installation

1. Clone the repo
```sh
git clone https://github.com/nolanwinsman/gc_swiss_updater.git
```

2. Install Python pip packages.
```sh
pip install -r requirements.txt
```

## Getting Started

- Have whatever drive you want to store your Swiss homebrew on. It should be a FAT32 external drive.
- Do not have **ANY** other drives mounted on your computer.
- Run `python main.py`
- Script will run downloading the newest Swiss `DOL` file and renaming/copying it to your Swiss drive.

## Contact

Nolan Winsman - [@Github](https://github.com/nolanwinsman) - nolanwinsman@gmail.com

Project Link: [https://github.com/nolanwinsman/gc_swiss_updater](https://github.com/nolanwinsman/gc_swiss_updater)

## Contributers
- nolanwinsman

## Files

- main.py : main Python script
- usb_operations.py : Class to handle finding the Swiss drive to copy the files to and also get some basic info on said drive.
- github_release_downloader.py : Class to download the desired file for the newest release for whatever repo you choose.
- util.py : Utility class. Currently only used to extract a `.7z` file
- README.md : this file
- requirements.txt
- .gitignore : includes `swiss-releases/` and `__pycache__/`

## Credits

This project is inspired by and utilizes the Swiss Homebrew Software developed by emukidid.

Repo Link: [https://github.com/emukidid/swiss-gc](https://github.com/emukidid/swiss-gc)

