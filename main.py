import argparse
import math
from PIL import Image, ImageDraw

def add(left, right):
    """
    Returns an image that is the sum of left and right image

    left: type TODO
    right: type TODO
    """
    return Image.blend(left, right)

if __name__ == '__main__':

    #setup
    parser.add_argument('--name', type=str)
    parser.add_argument('--rows', type=int)
    parser.add_argument('--cols', type=int)


    args = parser.parse_args()

    # given the name of the file create an image
    template = Image.open(args.name,'r')
    temp_outline = Image.open("outline.svg",'r')

    base = template.resize((args.cols, args.rows))
    outline = temp_outline((args.cols, args.rows))
    # perform an add operation on the base file, and the puzzle template
    jigsaw = Image.blend(base, outline)
    jigsaw.load()
    jigsaw.save(args.name + "-puzzle","png")

    # output the sum of the two images
