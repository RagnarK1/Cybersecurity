# Active

## Table of Contents
- ### [General Information](#general-information)
- ### [Setup](#setup)
- ### [Usage](#usage)
- ### [Author](#authors)

### General Information
The goal of this project is to develop a binder that merges two programs into on.

## Setup
Clone the repository
```
git clone https://01.kood.tech/git/Ragnar/injector
```
Proceed to next step.

## Usage
Compile "bin" and "helloworld" 
```
gcc -o bin bin.c
gcc -o helloworld helloworld.c
```
Use the script and replace 1 and 2 with desired message
```
./injector.sh bin helloworld "1" " 2"
```

## Author
- Ragnar Küüsmaa