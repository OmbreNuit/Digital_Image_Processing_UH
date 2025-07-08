class BinaryImage:
    def __init__(self):
        pass

    def compute_histogram(self, image):
        """ Computes the histogram of the input image
        takes as input:
        image: a greyscale image
        returns a histogram as a list """

        hist = [0]*256
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                hist[image[i, j]] += 1

        return hist

    def find_threshold(self, hist):
        """ analyses a histogram to find the optimal threshold assuming that the input histogram is bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value
        Note: Use the iterative method to calculate the histogram. Do not use the Otsu's method
        Write your code to compute the optimal threshold method.
        This should be implemented using the iterative algorithm discussed in class (See Week 4, Lecture 7, slide 40
        on teams). Do not implement the Otsu's thresholding method. No points are awarded for Otsu's method.
        """
        #Initialize T = K/2 => 255/2 = 127.5 => 128 assumption
        threshold = 128
        expectedValue = 1

        while expectedValue != 0:
            no1, no2 = 0, 0
            mean1, mean2 = 0, 0
            for i in range(256):
                if i < threshold:
                    no1 += hist[i]
                    mean1 += i * hist[i]
                else:
                    no2 += hist[i]
                    mean2 += i * hist[i]
            # checking for zeros to avoid division by zero error
            if no1 == 0:
                mean1 = 0
            else:
                mean1 /= no1

            if no2 == 0:
                mean2 = 0
            else:
                mean2 /= no2
            # new threshold is average of those 2 expectations
            newThreshold = int((mean1 + mean2) / 2)
            expectedValue = abs(newThreshold - threshold)
            threshold = newThreshold
        # when the change in mean from previous iteration to current iteration is 0 STOP, return threshold
        return threshold

    def binarize(self, image, threshold):
        """ Comptues the binary image of the input image based on histogram analysis and thresholding
        takes as input
        image: a greyscale image
        threshold: to binarize the greyscale image
        returns: a binary image """

        bin_img = image.copy()
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                pixel = image[i, j]
                if pixel < threshold:
                    bin_img[i, j] = 0
                elif pixel >= threshold:
                    bin_img[i, j] = 255

        return bin_img


