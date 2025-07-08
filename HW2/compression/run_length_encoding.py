from dip import *

class Rle:
    def __init__(self):
        pass

    def encode_image(self,binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """
        imgList = [j for sub in binary_image for j in sub]
        rle_list = []
        a = imgList[0]
        rle_list.append(int(imgList[0]))
        c = 0
        for j in range(len(imgList)):
            if imgList[j] == a:
                c = c + 1
            else:
                rle_list.append(c)
                c = 1
                a = imgList[j]
        rle_list.append(c)
        return rle_list  # replace zeros with rle_code zeros(100)

    def decode_image(self, rle_code, height , width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        a = 1
        temp = []
        for i in range(len(rle_code)):
            if rle_code[i] == '255':
                a = 1
            elif rle_code[i] == '0':
                a = 0
            else:
                if a == 1:
                    temp.append(255 * ones((rle_code[i])))
                    a = 0
                else:
                    temp.append(zeros((rle_code[i])))
                    a = 1

        decoded = [item for sublist in temp for item in sublist]
        decoded_image = array(decoded).reshape(height, width)
        return decoded_image   # replace zeros with image reconstructed from rle_Code zeros((100,100), uint8)





        




