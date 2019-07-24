# Face-Detector

Detects face of a person in any given Image

This face detector is written so that a face can be detected in an image using only command line.

To run this code, in command line run:

cd Face-Detector

python face_detector.py -i path_to_your_image


path_to_your_image is the location where the image exists in your pc wrt to current directory.

There are other optional arguments:

-r red value of the rgb tuple used for the color of rectangle.

-g green value of the rgb tuple used for the color of rectangle.

-b blue value of the rgb tuple used for the color of rectangle.

-w width of the rectangle.

-s Scaling factor for image, for more information please refer to openCV Documentation.

-n Minimum Neighbors for Cascade configuration, for more information please refer to openCV Documentation.
