## Install
 - Download eagle-dif.py somehwere on your path
 - Adjust eagle_path variable if it is different

## Prerequisites
 - PIL

## Git Setup
### Add this to your .gitconfig:

    [diff "eagle"]

        command = eagle-diff

### Add a .gitattributes file to your project with these lines:

    *.sch diff=eagle
    *.brd diff=eagle

## Try it out
### Clone this project then:
    git diff v1 v2 main.brd

## Example
### Top left: new
### Top right: old
### Bottom left: difference
### Bottom right: overlay
![pew pew pew](https://github.com/jotux/eagle-diff/raw/master/brd_example.png "lasers pew pew")

## Contribute
Feel free to send pull requests with fixes/upgrades/whatever.