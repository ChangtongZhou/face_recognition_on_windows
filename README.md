# Facial Recognition on Windows

## Part 1: Prerequisites
This contains instructions on how to install dlib and open_CV on Windows based on collections of other resources.

### Step1: Install Visual Studio 2015
Download and install Visual Studio 2015 community edition from https://www.visualstudio.com/vs/older-downloads/
It is better to use 2015 version because, Dlib cannot be compiled using Visual Studio 2017.
If you have Visual Studio 2017, Uninstall it completely to avoid conflicts with Visual Studio 2015 installation.

Run installer, select “Custom” in “type of installation”. 

![install_visual_studio_2015-1](https://user-images.githubusercontent.com/16125724/29197063-8e107ab0-7ded-11e7-940d-7ed3db68084f.png)

In next screen within Programming Languages, select Visual C++ and Python tools for Visual Studio. Click next.

![install_visual_studio_2015-2](https://user-images.githubusercontent.com/16125724/29197099-d5702dec-7ded-11e7-8baa-4b114056738c.png)

Now click next. It will take some time to complete the installation.

![install_visual_studio_2015-4](https://user-images.githubusercontent.com/16125724/29197100-d574334c-7ded-11e7-9b6c-231e0f51492a.png)

We have finished installation of Visual Studio 2015.

### Step2: Install CMake
Download and install CMake v3.8.2 from https://cmake.org/download/

![capture](https://user-images.githubusercontent.com/16125724/29197126-fed912f2-7ded-11e7-9e49-e1e09fdac4f1.PNG)

During installation select “Add CMake to system PATH”

![cmake_2](https://user-images.githubusercontent.com/16125724/29197125-fed8ea5c-7ded-11e7-9ffe-89c03fb91f8a.png)

### Step 3: Install Anaconda (a python distribution)
Anaconda is a Python distribution which comes with a lot of useful Python packages. Installing Python modules on Windows can be a huge pain sometimes. Installing Anaconda is not necessary for generating OpenCV binary for Python. You can use official Python and NumPy as well.
Download and install Anaconda 64-bit version from https://www.continuum.io/downloads. You can install Anaconda 2 or Anaconda 3 or both. (I used Anaconda3-4.2.0-Windows-x86.exe with python 3.5 from https://repo.continuum.io/archive/)

![anaconda](https://user-images.githubusercontent.com/16125724/29197217-aaa525da-7dee-11e7-9adb-4fc23266f94e.PNG)

While installing Anaconda make sure that you check both options:
Add Anaconda to my PATH environment variable
Register Anaconda as my default Python

![anaconda2](https://user-images.githubusercontent.com/16125724/29197216-aaa440ac-7dee-11e7-9966-4349505d3239.png)

### Step 4: Download Dlib 19.4:
Download it from http://dlib.net/compile.html

![dlib](https://user-images.githubusercontent.com/16125724/29197248-dc15bae4-7dee-11e7-928d-b6d604b2a742.PNG)

### Step 5: Build Dlib library:
Extract this downloaded dlib file. Open Windows PowerShell or Command Prompt and move to the directory where you have extracted this file.
If you are running these commands on Windows PowerShell replace ^ (caret) with  ` (backtick).
cd dlib-19.4\
mkdir build
cd build
 
#### If you don’t have Anaconda
cmake -G "Visual Studio 14 2015 Win64" -DCMAKE_INSTALL_PREFIX=install ..
  
#### If you have Anaconda installed on your machine (I used this one)
cmake -G "Visual Studio 14 2015 Win64" ^
-DJPEG_INCLUDE_DIR=..\dlib\external\libjpeg ^
-DJPEG_LIBRARY=..\dlib\external\libjpeg ^
-DPNG_PNG_INCLUDE_DIR=..\dlib\external\libpng ^ -DPNG_LIBRARY_RELEASE=..\dlib\external\libpng ^
-DZLIB_INCLUDE_DIR=..\dlib\external\zlib ^
-DZLIB_LIBRARY_RELEASE=..\dlib\external\zlib ^
-DCMAKE_INSTALL_PREFIX=install ..
 
cmake --build . --config Release --target INSTALL
cd ..
 
Dlib will be installed within dlib-19.4\build\install directory. This directory contains include and library folder which you can specify in Visual Studio to use Dlib.

### Step 6: Build Dlib examples:
If you are running these commands on Windows PowerShell replace ^ (caret) with  ` (backtick).
cd dlib-19.4/examples
mkdir build
cd build
 
#### If you don’t have Anaconda
cmake -G "Visual Studio 14 2015 Win64" ..
  
#### If you have Anaconda installed on your machine
cmake -G "Visual Studio 14 2015 Win64" ^
-DJPEG_INCLUDE_DIR=..\..\dlib\external\libjpeg ^
-DJPEG_LIBRARY=..\..\dlib\external\libjpeg ^
-DPNG_PNG_INCLUDE_DIR=..\..\dlib\external\libpng ` -DPNG_LIBRARY_RELEASE=..\..\dlib\external\libpng ^
-DZLIB_INCLUDE_DIR=..\..\dlib\external\zlib ^
-DZLIB_LIBRARY_RELEASE=..\..\dlib\external\zlib ^
..
 
cmake --build . --config Release
cd ..\..

### Step 7: Install Dlib’s Python module (Only Anaconda 3)
Compiling Python bindings for Dlib from source is non-trivial. You have to compile Boost.Python from scratch and configure some environment variables (such as BOOST_ROOT and BOOST_LIBRARYDIR) before you can compile Python module of Dlib. We are skipping that part for now. A complete tutorial on how to build Dlib Python bindings from source will be released in future.

To save time and efforts it is suggested to use Anaconda 3. You can install a compiled binary of dlib v19.4 from Anaconda.

#### conda install -c conda-forge dlib=19.4

After manually installing dlib, got to https://github.com/ageitgey/face_recognition to start working on face_recognition project.

try running "pip install face_recognition" to complete your installation of face_recognition module.

### Step 8: If you want to use real time webcam face recognition:
You need to download open_CV from: http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv

I chose this wheel: "opencv_python-3.2.0+contrib-cp35-cp35m-win_amd64.whl"

After finish downloading, cd to where you saved the .whl file and use “pip install opencv_python-3.2.0+contrib-cp35-cp35m-win_amd64.whl”.

Here is the reference: https://stackoverflow.com/questions/35466429/opencv-for-python-3-5-1

## Part 2:
After finishing downloading everything, you can pick any python sample programs from https://github.com/ageitgey/face_recognition to test. 

For example:

#### 1) To quick test if dlib works:
First, you need to provide a folder with one picture of each person you already know. There should be one image file for each person with the files named according to who is in the picture.

Next, you need a second folder with the files you want to identify, name them with unknown, unknown1, unknown2, etc,. 
Then in you simply run the command face_recognition, passing in the folder of known people and the folder (or single image) with unknown people and it tells you who is in each image:

cd to your folder which contains both known_pic folder and unknown_pic folder and run the following commands in your command prompt.

$ face_recognition ./pictures_of_people_i_know/ ./unknown_pictures/
/unknown_pictures/unknown.jpg,Barack Obama
/face_recognition_test/unknown_pictures/unknown.jpg,unknown_person
 
#### 2) To test if real-time webcam works:
Create a python file, copy and paste from https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py

Finally, use your command prompt to cd to this file and run: python filename.py

### For further information, please refer to the following links:
https://github.com/ageitgey/face_recognition
http://www.learnopencv.com/install-dlib-on-windows/
http://www.learnopencv.com/install-opencv3-on-windows/



