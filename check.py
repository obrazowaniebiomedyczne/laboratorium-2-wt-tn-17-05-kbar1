from solution import *
from obpng import read_png, write_png
from skimage import util, io, filters, morphology, data

print("- Ocena dostateczna")
renew_pictures()
#write_png(image, 'results/1.png')


"""
print("- Ocena dobra")
read_png("figures/crushed.png")
erosion = own_simple_erosion(image)
write_png("results/own_simple_erosion.png")
"""

"""
print("- Ocena bardzo dobra")
read_png("figures/crushed.png")
kernel = np.array([[0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0],
                   [1, 1, 1, 1, 1],
                   [0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0]])
erosion = own_erosion(image, kernel)
write_png("results/own_erosion.png")
"""
