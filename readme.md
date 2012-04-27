## Install
 - Download somehwere on your path
 - Adjust eagle_path variable if it is different

## Prerequisites
 - PIL

## Git Setup
### Add this to your .gitconfig:

    [diff "eagle"]

        command = eagle-diff

### Add a .gitattributes file to your project with this line:

    *.sch diff=eagle
    *.brd diff=eagle

## Try it out
### Clone this project:
    git diff main.brd v2 v1