from .interpolation import interpolation
from dip import *
import math

class Distort:
    def __init__(self):
        pass

    def distortion(self, image, k):
        """Applies distortion to the image
                image: input image
                k: distortion Parameter
                return the distorted image"""
        col_y, row_x, channel = image.shape
        xCenter = row_x // 2
        yCenter = col_y // 2

        distorted_image = zeros((col_y, row_x, channel))

        for i in range(col_y):
            for j in range(row_x):
                x_norm = j - xCenter
                y_norm = i - yCenter

                r = math.sqrt(x_norm ** 2 + y_norm ** 2)
                r_distort = (1 / (1 + k * r))

                x_distort = round(r_distort * x_norm) + xCenter
                y_distort = round(r_distort * y_norm) + yCenter

                if 0 <= y_distort < col_y and 0 <= x_distort < row_x:
                    distorted_image[y_distort, x_distort] = image[i, j]

        return distorted_image

    def correction_naive(self, distorted_image, k):
        """Applies correction to a distorted image by applying the inverse of the distortion function
        image: the input image
        k: distortion parameter
        return the corrected image"""
        col_y, row_x, channel = distorted_image.shape
        xCenter = row_x // 2
        yCenter = col_y // 2

        corrected_image = zeros((col_y, row_x, channel))
        for i in range(col_y):
            for j in range(row_x):
                x_dist = j - xCenter
                y_dist = i - yCenter

                r = math.sqrt(x_dist ** 2 + y_dist ** 2)
                r_inverse_distort = 1 + (k * r)

                x_correct = round(r_inverse_distort * x_dist) + xCenter
                y_correct = round(r_inverse_distort * y_dist) + yCenter

                if 0 <= y_correct < col_y and 0 <= x_correct < row_x:
                    corrected_image[y_correct, x_correct] = distorted_image[i, j]

        return corrected_image

    def correction(self, distorted_image, k, interpolation_type):
        """Applies correction to a distorted image and performs interpolation
                image: the input image
                k: distortion parameter
                interpolation_type: type of interpolation to use (nearest_neighbor, bilinear)
                return the corrected image"""
        col_y, row_x, channel = distorted_image.shape
        xCenter = row_x // 2
        yCenter = col_y // 2

        corrected_img = zeros((col_y, row_x, channel))

        for i in range(col_y):
            for j in range(row_x):
                x_dist = j - xCenter
                y_dist = i - yCenter

                r = math.sqrt(x_dist ** 2 + y_dist ** 2)
                r_distort = 1 + (k * r)
                x_cd = x_dist / r_distort
                y_cd = y_dist / r_distort

                x_correct = (x_cd) + xCenter
                y_correct = (y_cd) + yCenter

                interpolate = interpolation()
                if 0 <= y_correct < col_y and 0 <= x_correct < row_x:
                        if interpolation_type == "bilinear":
                            x1 = math.ceil(x_correct)
                            x2 = math.floor(x_correct)
                            y1 = math.ceil(y_correct)
                            y2 = math.floor(y_correct)

                            bilinear = interpolate.bilinear_interpolation(x_correct, y_correct, x1, x2, y1, y2, distorted_image)
                            corrected_img[i, j] = bilinear

                        elif interpolation_type == "nearest_neighbor":
                            corrected_img[i, j] = distorted_image[round(y_correct), round(x_correct)]

        return corrected_img