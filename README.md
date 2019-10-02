# ProcessingPack
!["One Piece at a Time"](/resources/chip-working.png)

## Overview
ProcessingPack is a set of classes and functions to execute MITOMI image processing (feature finding and quantification). 

It is designed around the following paradigm:
 - Imaging of a *ChipImage* is *single* or *series*
 	- A given *ChipImage* is a 2-D array of *Stamps*
 	- A *Stamp* contains feature with attributes. Principle features are:
 		- *Chamber*: the primary reaction chamber
 		- *Button*: the contact area of the button on the slide

## Dev Notes:
- Check package requirements: use `pipreqs` on directory containing runpack 
- Install: `pip install -e git+https://github.com/FordyceLab/RunPack.git#egg=processingpack`
    + Note `-e` makes package editable
- Register venv with Jupyter: `python -m ipykernel install --user --name=processingpack`
