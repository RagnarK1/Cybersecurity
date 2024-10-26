# Inspector Image

## Table of Contents
- ### [General Information](#general-information)
- ### [Setup](#setup)
- ### [Usage](#usage)
- ### [Authors](#authors)

### General Information
This project aims to explore various aspects of passive analysis, including basic image recognition approaches and steganography. By decoding steganography from images, the program reveals hidden information such as PGP keys and the location where the photo was taken.

## Setup
Clone the repository
```
git clone https://01.kood.tech/git/Ragnar/inspector-image
```
Proceed to next step.

## Usage
Install phyton3 with command (if you have a Ubuntu/Debian Linux)
```
sudo apt install python3  
```
Use the program with these commands
```
python3 inspector.py -map resources/image.jpeg
python3 inspector.py -steg resources/image.jpeg
```

## Author
- Ragnar Küüsmaa