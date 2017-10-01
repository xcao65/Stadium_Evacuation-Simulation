from FileIO import *
from simulation_engine import *
import time
from plot_map import *
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image

if __name__ == '__main__':
    # gt_map = FileIO.read_input("map.png","Destinations.csv")
    gt_map = FileIO.read_input("new_map.png")
    gt_entries = gt_map.get_entries()
    entry = {"xvals": [], "yvals": []}
    for e in gt_entries:
        entry["xvals"].append(e.get_x())
        entry["yvals"].append(e.get_y())
    print "entry size is ", len(entry["xvals"]), gt_map.get_entries_num()

    peds = []
    ts = 0
    print "start simulation"
    # plotted = Plot_map("map.png")
    plotted = Plot_map("new_map.png")
    simulator.initialize(gt_map, peds, ts)
    reached = False

    while ts < 15000:
        if len(peds) == 0: break
        simulator.update_map(gt_map, peds, ts)
        ts += 1
        if ts % 5 == 0:
            print "current time stamp is %s, peds number is %s" %(ts, len(peds))
        if len(peds) < 15000 and not reached:
            simulator.initialize(gt_map, peds, ts)
        else:
            reached = True

        if ts % 10 == 0:
            xy = simulator.get_update_xy(peds)
            name = "image_ts_"+str(ts)+".png"
            if ts % 500 == 0:
                plotted.update_plot(xy["xvals"], xy["yvals"], entry["xvals"], entry["yvals"], name, True)
            else:
                plotted.update_plot(xy["xvals"], xy["yvals"], entry["xvals"], entry["yvals"], name, False)
