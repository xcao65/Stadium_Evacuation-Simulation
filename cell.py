# cell class
__metaclass__ = type


class Cell:
    def __init__(self, celltype):
        self.ctype = celltype
        self.occupied = False

    def is_occupied(self):
        return self.occupied

    def get_cell_type(self):
        return self.ctype

    def set_occupied(self, occ):
        self.occupied = occ


class Block_Cell(Cell):
    def __init__(self, celltype):
        super(Block_Cell, self).__init__(celltype)
        self.occupied = True

    def is_occupied(self):
        return self.occupied

class Exit_Cell(Cell):
    def __init__(self, celltype, num):
        super(Exit_Cell, self).__init__(celltype)
        self.exit_num = num

    def get_exit_num(self):
        return self.exit_num

    def set_exit_num(self, num):
        self.exit_num = num


class Road_Cell(Cell):
    def __init__(self, celltype):
        super(Road_Cell, self).__init__(celltype)
        self.visit_times = 0

    def get_visit_times(self):
        return self.visit_times

    def add_visit_times(self):
        self.visit_times += 1


if __name__ == '__main__':
    cell = Cell(1)
    print "cell is occupied or not: ", cell.is_occupied()
    print "cell type is : ", cell.get_cell_type()
    block = Block_Cell(2)
    print "block cell is occupied or not: ", block.is_occupied()
    print "block cell type is : ", block.get_cell_type()
    exit = Exit_Cell(3, 0)
    print "Exit cell is occupied or not: ", exit.is_occupied()
    print "Exit cell type is : ", exit.get_cell_type()
    print "Before: Exit number is :", exit.get_exit_num()
    exit.set_exit_num(10)
    print "After: Exit number is :", exit.get_exit_num()
    road = Road_Cell(4)
    print "road cell is occupied or not: ", road.is_occupied()
    road.set_occupied(True)
    print "set road cell to occupied, then, ", road.is_occupied()
    print "road cell type is : ", road.get_cell_type()
    print "road cell visit time by default is ", road.get_visit_times()
    for i in range(10):
        road.add_visit_times()
    print "After: road cell visit time is ", road.get_visit_times()
