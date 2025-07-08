import math
from dip import *
"""
Do not import cv2, numpy and other third party libs
"""


class Operation:

    def __init__(self):
        pass

    def flip(self, image, direction="horizontal"):
        """
          Perform image flipping along horizontal or vertical direction

          image: the input image to flip
          direction: direction along which to flip

          return: output_image
          """

        #Solve The assignment flipping
        height = len(image)

        if direction == "horizontal":
            for i in range(height):
                image[i] = image[i][::-1]
        elif direction == "vertical":
                image = image[::-1]

        return image

    def chroma_keying(self, foreground, background, target_color, threshold):
        """
        Perform chroma keying to create an image where the targeted green pixels is replaced with
        background

        foreground_img: the input image with green background
        background_img: the input image with normal background
        target_color: the target color to be extracted (green)
        threshold: value to threshold the pixel proximity to the target color

        return: output_image
        """

        # add your code here
        output_image = background
        for i in range(foreground.shape[0]):
            for j in range(foreground.shape[1]):
                distance = math.sqrt(sum((foreground[i, j] - target_color) ** 2))

                if distance < threshold:
                    output_image[i, j] = background[i, j]
                else:
                    output_image[i, j] = foreground[i, j]

        # Please do not change the structure
        return output_image # Currently the input image is returned, please replace this with the color extracted image

   
