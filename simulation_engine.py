# this is the class for simulation engine
import random
import numpy as np
from roadmap import *

class simulator:
    @staticmethod
    def initialize(roadmap, peds, ts): # pass in seed if needed
        total_entry_size = roadmap.get_entries_num()
        if len(peds) < 8000:
            curr_entry_size = np.random.poisson(total_entry_size)
        elif len(peds) < 12000:
            curr_entry_size = np.random.poisson(total_entry_size/2)
        else:
            curr_entry_size = np.random.poisson(total_entry_size/3)

        curr_entry_size = total_entry_size if curr_entry_size > total_entry_size else curr_entry_size
        '''
        if len(peds) > 10000:
            curr_entry_size = 0
            print "peds size and curr_entry_size are ", len(peds), curr_entry_size
            return peds
        '''
        print "curr_entry_size after is :", curr_entry_size
        status_array = [False] * curr_entry_size
        for i in range(curr_entry_size):
            curr_idx = int(random.random()*curr_entry_size)
            while status_array[curr_idx]:
                curr_idx = int(random.random()*curr_entry_size)
            # fetch the entry ehich is false
            status_array[curr_idx] = True
            new_entry = roadmap.get_entries()[curr_idx]
            new_x, new_y = new_entry.get_x(), new_entry.get_y()
            new_cell = roadmap.get_cell(new_x, new_y)
            # print "x, y are", new_x, new_y
            if not new_cell.is_occupied():
                exit_number = int(random.random() * roadmap.get_exit_num())
                peds.append(Pedestrian(new_x, new_y, "Pedestrian", exit_number))
                new_cell.set_occupied(True)

        print "peds size is ", len(peds)
        return peds

    @staticmethod
    def get_update_xy(peds):
        if not peds:
            print "invalid input"
            return None
        ans = {"xvals": [], "yvals": []}
        for p in peds:
            ans["xvals"].append(p.get_x())
            ans["yvals"].append(p.get_y())
        return ans
        # return type is a dictionary, which has two keys: xvals, and yvals

    @staticmethod
    def arrival(roadmap, peds, idx): # return T/F of ped arrival status
        curr_ped = peds[idx]
        x, y = curr_ped.get_x(), curr_ped.get_y()
        curr_cell = roadmap.get_cell(x, y)
        if curr_cell.get_cell_type() == "exit":
            curr_cell.set_occupied(False)
            del peds[idx]
            return True
        else:
            return False

    @staticmethod
    def update_map(roadmap, peds, ts):
        peds_size = len(peds)
        i = 0
        while i < peds_size:
            new_ped = peds[i]
            simulator.update_peds(roadmap, new_ped)
            if simulator.arrival(roadmap, peds, i):
                peds_size -= 1
                i -= 1
            i += 1


    @staticmethod
    def update_peds(roadmap, ped):
        exit_number = ped.get_exit_num()
        curr_exit = roadmap.get_exits()[exit_number]
        shortest_path = curr_exit.get_path()
        x, y = ped.get_x(), ped.get_y()

        neighbor_path = [[0]*3 for i in range(3)]
        _sum = 0.0
        neighbor_prob = [[0]*3 for i in range(3)]
        ratio = [1, 10, 15]

        for i in range(3):
            for j in range(3):
                if x+i-1 >= 0 and y+j-1 >=0 and x+i-1 < len(shortest_path) and \
                   y+j-1 < len(shortest_path[0]) and shortest_path[x+i-1][y+j-1] != -1 and \
                   not roadmap.get_cell(x+i-1, y+j-1).is_occupied():
                   neighbor_path[i][j] = \
                       shortest_path[x][y] - shortest_path[x+i-1][y+j-1] + 1
                else:
                    neighbor_path[i][j] = 10

        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    if neighbor_path[i][j] != 10:
                        _sum += ratio[neighbor_path[i][j]]

        if _sum == 0: return False

        prev_cell = roadmap.get_cell(x, y)
        prev_cell.set_occupied(False)
        prev_cell.add_visit_times()

        for i in range(3):
            for j in range(3):
                if i!=1 or j!=1:
                    if neighbor_path[i][j] != 10:
                        neighbor_prob[i][j] = ratio[neighbor_path[i][j]]/_sum

        rand = 1.0 - random.random()
        flag = False
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    if rand <= neighbor_prob[i][j]:
                        ped.set_location(x+i-1, y+j-1)
                        new_cell = roadmap.get_cell(x+i-1, y+j-1)
                        new_cell.set_occupied(True)
                        flag = True
                        break
                else:
                    # print "neighbor_prob[i][j] is", neighbor_prob[i][j]
                    rand = rand - neighbor_prob[i][j]
            if flag: break
        return True



if __name__ == '__main__':
    container = [[Cell(1), Cell(2)], [Cell(0),Cell(3)]]
    entries = []
    entries.append(Entry(1,2,2))
    exits = []
    exits.append(Exit(0,0,3))
    exits.append(Exit(1,1,3))

    m = Roadmap(container, entries, exits)
    peds = []
    ts = 0
    print "start simulation"
    simulator.initialize(m, peds, ts)
    while ts < 10:
        simulator.update_map(m, peds, ts)
        ts += 1
        print ts
        simulator.initialize(m, peds, ts)
