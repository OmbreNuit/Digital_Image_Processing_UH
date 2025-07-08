import dip
from dip import *
import math
class ShapeCounting:
    def __init__(self):
        pass

    def blob_coloring(self, image):
        """Implement the blob coloring algorithm
        takes as input:
        image: binary image
        return: a list/dict of regions
        """
        [height, width] = image.shape
        region = zeros((height, width))
        counter = 1
        for row in range(height):
            for col in range(width):
                if row == 0 and col == 0:
                    if image[row, col] == 255:
                        region[row, col] = counter
                        counter += 1

                elif row == 0:
                    if image[row, col] == 255:
                        if image[row, col - 1] == 0:
                            region[row, col] = counter
                            counter += 1
                        else:
                            region[row, col] = region[row, col - 1]
                elif col == 0:
                    if image[row, col] == 255:
                        if image[row - 1, col] == 0:
                            region[row, col] = counter
                            counter += 1
                        else:
                            region[row, col] = region[row - 1, col]

                elif image[row, col] == 255 and image[row, col - 1] == 0 and image[row - 1, col] == 0:
                    region[row, col] = counter
                    counter += 1

                elif image[row, col] == 255 and image[row, col - 1] == 0 and image[row - 1, col] == 255:
                    region[row, col] = region[row - 1, col]

                elif image[row, col] == 255 and image[row, col - 1] == 255 and image[row - 1, col] == 0:
                    region[row, col] = region[row, col - 1]

                elif image[row, col] == 255 and image[row, col - 1] == 255 and image[row - 1, col] == 255:
                    region[row, col] = region[row - 1, col]
                    if region[row, col - 1] != region[row - 1, col]:
                        l = row
                        m = col
                        while image[l, m] == 255:
                            m = m - 1
                            if image[l, m] != 0:
                                x = l
                                y = m
                                region[l, m] = region[row, col]
                                while image[x, y] == 255:
                                    x = x - 1
                                    if image[x, y] != 0:
                                        region[x, y] = region[l, m]
                        counter -= 1
        return region

    def identify_shapes(self, region):
        """Compute shape features area and centroid, and shape
        Ignore shapes smaller than 10 pixels in area.
        takes as input
        region: a list/dict of pixels in a region
        returns: shapes, a data structure with centroid, area, and shape (c, s, r, or e) for each region
        c - circle, s - squares, r - rectangle, and e - ellipse
        """

        # Please print your shape statistics to stdout, one line for each shape
        # Region: <region_no>, centroid: <centroid>, area: <shape area>, shape: <shape type>
        # Example: Region: 871, centroid: (969.11, 51.11), area: 707, shape: c

        shapes = []
        regions = array(region)

        for region_label in range(1, int(regions.max() + 1)):
            indices = []
            for i in range(len(regions)):
                for j in range(len(regions[i])):
                    if regions[i][j] == region_label:
                        indices.append((i, j))
            region_indices = indices

            area = len(region_indices)
            if area < 10:
                continue

            min_row = array(region_indices)[:, 0].min()
            max_row = array(region_indices)[:, 0].max()
            min_col = array(region_indices)[:, 1].min()
            max_col = array(region_indices)[:, 1].max()

            centroid_i = (min_row + max_row) / 2
            centroid_j = (min_col + max_col) / 2
            centroid = (centroid_i, centroid_j)

            upLcorner = (min_row, min_col)
            corner_area = [point for point in region_indices if math.sqrt((point[1] - upLcorner[1]) ** 2 + (point[0] - upLcorner[0]) ** 2) < 5]
            true_area = len(region_indices)
            height = abs(min_row - max_row)
            width = abs(max_col - min_col)

            if any(point in corner_area for point in region_indices):
                if abs((width ** 2) - (height ** 2)) / true_area < 0.03:
                    shape = "s"
                else:
                    shape = "r"
            else:
                if abs((3.14159 * (width / 2) ** 2) - true_area) / true_area < 0.05:
                    shape = "c"
                else:
                    shape = "e"

            stats = {
                'region': region_label,
                'centroid': centroid,
                'area': area,
                'shape': shape
            }
            shapes.append(stats)

        for shapee in shapes:
            stats_str = f"Region: {shapee['region']}, centroid: ({shapee['centroid'][1]:.2f}, {shapee['centroid'][0]:.2f}), area: {shapee['area']}, shape: {shapee['shape']}"
            print(stats_str)

        return shapes

    def count_shapes(self, shapes_data):
        """Compute the count of shapes using the shapes data returned from identify shapes function
           takes as input
           shapes_data: a list/dict of regions, with centroid, shape, and area for each shape
           returns: a dictionary with count of each shape
           Example return value: {'circles': 21, 'ellipses': 25, 'rectangles': 31, 'squares': 23}
           """

        shape_count = {'circles': 0, 'ellipses': 0, 'rectangles': 0, 'squares': 0}

        for shape in shapes_data:
            shape_type = shape['shape']
            if shape_type == 'c':
                shape_count['circles'] += 1
            elif shape_type == 'e':
                shape_count['ellipses'] += 1
            elif shape_type == 'r':
                shape_count['rectangles'] += 1
            elif shape_type == 's':
                shape_count['squares'] += 1

        return shape_count
        # return {"circles": 0, "ellipses": 0, "rectangles": 0, "squares": 0}

    def mark_image_regions(self, image, shapes_data):
        """Creates a new image with computed stats for each shape
        Make a copy of the image on which you can write text.
        takes as input
        image: binary image
        shapes_data: a list/dict of regions, with centroid, shape, and area for each shape
        returns: image marked with center and shape_type"""

        marked_image = image.copy()
        for shape in shapes_data:
            (x, y) = shape['centroid']
            shape_type = shape['shape']

            dip.putText(marked_image, shape_type, (int(y), int(x)), FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, 5)

        return marked_image


