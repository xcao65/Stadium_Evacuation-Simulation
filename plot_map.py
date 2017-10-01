import matplotlib
import matplotlib.pyplot as plt

class Plot_map():
    def __init__(self, pngname):
        plt.ion()
        fig = plt.figure()
        self.ax = fig.add_subplot(1, 1, 1)
        self.scat = self.ax.scatter([], [], zorder=1)
        self.scat2 = self.ax.scatter([], [], zorder=2)

        img = plt.imread(pngname)
        plt.imshow(img, zorder=0)
        plt.show()
        plt.pause(0.0001)

    def update_plot(self, x_vals, y_vals, entry_x, entry_y, name, status):
        self.scat.remove()
        self.scat2.remove()
        self.scat = self.ax.scatter(x_vals, y_vals, zorder=1, color='r', s=2)
        self.scat2 = self.ax.scatter(entry_x, entry_y, zorder=2, color='b', s=2)
        plt.draw()
        if status == True:
            plt.savefig(name)
        plt.pause(0.0001)
