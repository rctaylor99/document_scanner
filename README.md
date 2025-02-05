# Document Scanner

Making a document scanner for my desk at home! Ultimate goal is to automatically detect, scan, and upload documents to my Google Drive.
<br>
## Hardware

Deciding now on the end hardware to use, though it will likely be one of these options:

* SK-AM62B-P1
* BeagleBone Black
* BeagleY-AI
* Raspberry Pi 4B

## Software

I want to focus on the following development tools for this project, which will help me deploy to the embedded device:

* OpenCV
* Google Drive APIs

### Additional Notes:

* Installation of imutils on MacOS:
    * imutils is available to be downloaded through Homebrew on MacOS. To get around this dependency, we must use a virtual environment:

`$ python -m venv <path_to_project>/virtual`
This command makes a new directory within our project and places a configuration file within it. To invoke the virtual environment, use the following command:
`$ source <path_to_project>/virtual/bin/activate`
Your bash shell should now have a (virtual) in front of the prompt. When this is available, you can install imutils as normal:
`$ python3 -m pip install imutils`