import csv
import matplotlib
import matplotlib.pyplot as plt
from location import *
from cell import *
from roadmap import Roadmap
import numpy as np
from roadmap import *
# import Image
from PIL import Image


class FileIO:
    @staticmethod
    def read_input(image_name):

        exits = []
        entries = []
        # open image
        im = Image.open(image_name)
        rgb_im = im.convert('RGB')
        pixels = rgb_im.load()
        w, h = rgb_im.size
        print "width, height is ", w, h
        # set color RGB
        red = (255,0,0)  # exit
        blue = (0,0,255) # entries
        gray = (192,192,172) # road
        white = (255,255,255) # road
        green = (179,212,136) # block

        # fill container
        container = [[None for i in range(h)] for j in range(w)]
        for i in range(w):
            for j in range(h):
                if pixels[i,j] == red:
                    container[i][j] = Exit_Cell('exit', 1)
                    exits.append(Exit(i,j,'exit'));
                elif pixels[i,j] == blue:
                    container[i][j] = Road_Cell('road')
                    entries.append(Entry(i,j,'entry'));
                elif pixels[i,j] == gray:
                    container[i][j] = Road_Cell('road')
                elif pixels[i,j] == white:
                    container[i][j] = Road_Cell('road')
                elif pixels[i,j] == green:
                    #container[i][j] = Block_Cell('grass')
                    container[i][j] = Block_Cell('block')
                else:
                    container[i][j] = Block_Cell('block')

        new_road_map = Roadmap(container, entries, exits)
        return new_road_map




if __name__ == "__main__":
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    scat = ax.scatter([], [], zorder=1)

    img = plt.imread("map.png")
    # print "show image"
    plt.imshow(img, zorder=0)
    plt.show()
    plt.pause(0.1)

    # for t in range(ts):
    x_vals = [253, 356]
    y_vals = [1000, 1000]
    scat.remove()
    scat = ax.scatter([254, 357], y_vals, zorder=1, color='b', s=0.5)
    scat = ax.scatter(x_vals, y_vals, zorder=1, color='r', s=0.5)

    plt.draw()
    name = "haha"+str(1)+".png"
    plt.savefig(name)
    plt.pause(2)
