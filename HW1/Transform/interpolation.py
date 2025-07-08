from dip import *
import math
class interpolation:

    def linear_interpolation(self, pt, x1, x2, ix1, ix2):
        """Computes the linear interpolation value at some iD location x between two 1D points (Pt1 and Pt2).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes two 1D points Pt1 and Pt2, and their intensitites I(Pt1), I(Pt2).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for linear interpolation here
        if x1 == x2:
            return ix1
        linear = (((x2 - pt) / (x2-x1)) * ix1) + (((pt - x1) / (x2 - x1)) * ix2)
        return linear

    def bilinear_interpolation(self,x_cor, y_cor, px1, px2, py1, py2, image):
        """Computes the bilinear interpolation value at some 2D location x between four 2D points (Pt1, Pt2, Pt3, and Pt4).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes four 2D points Pt1, Pt2, Pt3, and Pt4, and their intensitites I(Pt1), I(Pt2), I(Pt3), and I(Pt4).
        return the interpolated intensity value (I(x)) at location x """
        # Write your code for bilinear interpolation here
        # Recall that bilinear interpolation performs linear interpolation three times
        # Please reuse or call linear interpolation method three times by passing the appropriate parameters to compute this task
        Q11 = image[py1, px1]
        Q21 = image[py1, px2]
        Q12 = image[py2, px1]
        Q22 = image[py2, px2]

        R1 = self.linear_interpolation(x_cor, px1, px2, Q11, Q21)
        R2 = self.linear_interpolation(x_cor, px1, px2, Q12, Q22)
        i = self.linear_interpolation(y_cor, py1, py2, R1, R2)

        return i

