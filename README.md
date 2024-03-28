### Gamecube Swiss Updater

Simple Python script to download the newest release of Swiss [https://github.com/emukidid/swiss-gc](https://github.com/emukidid/swiss-gc), extract the file and copy the contents to the 
first detected USB/SD card


## Installation

1. Clone the repo
```sh
git clone https://github.com/nolanwinsman/gc_swiss_updater.git
```

## Getting Started

## Features

# Contact

Nolan Winsman - [@Github](https://github.com/nolanwinsman) - nolanwinsman@gmail.com

Project Link: [https://github.com/nolanwinsman/bulk_renamer](https://github.com/nolanwinsman/bulk_renamer)

# Contributers
- nolanwinsman

## Files

- main.py : main Python script
- usb_operations.py : Class to handle finding the Swiss drive to copy the files to and also get some basic info on said drive.
- github_release_downloader.py : Class to download the desired file for the newest release for whatever repo you choose.
- util.py : Utility class. Currently only used to extract a `.7z` file
- README.md : this file
- requirements.txt
- .gitignore : includes `swiss-releases/` and `__pycache__/`



