__metaclass__ = type


class Location:
    def __init__(self, x, y, ltype):
        self.loc_type = ltype
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_loc_type(self):
        return self.loc_type


class Entry(Location):
    def __init__(self, x, y, ltype):
        super(Entry, self).__init__(x, y, ltype)


class Exit(Location):
    def __init__(self, x, y, ltype):
        super(Exit, self).__init__(x, y, ltype)
        self.weight = None
        self.path = []

    def set_weight(self, w):
        self.weight = w

    def get_weight(self):
        return self.weight

    def set_path(self, p):
        self.path = p

    def get_path(self):
        return self.path


class Pedestrian(Location):
    def __init__(self, x, y, ltype, num):
        super(Pedestrian, self).__init__(x, y, ltype)
        self.exit_num = num

    def set_exit_num(self, num):
        self.exit_num = num

    def get_exit_num(self):
        return self.exit_num

    def set_location(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    loc = Location(0,0,0)
    print "this loc type is %s, axes are (%s, %s)" % (loc.get_loc_type(), loc.get_x(), loc.get_y())
    entry = Entry(1,1,1)
    print "this loc type is %s, axes are (%s, %s)" % (entry.get_loc_type(), entry.get_x(), entry.get_y())
    exit = Exit(3,3,3,10)
    print "before: this loc type is %s, axes are (%s, %s), weight is %s" \
                % (exit.get_loc_type(), exit.get_x(), exit.get_y(), exit.get_weight())
    exit.set_x(100)
    exit.set_y(200)
    exit.set_weight(50)
    print "after: this loc type is %s, axes are (%s, %s), weight is %s" \
            % (exit.get_loc_type(), exit.get_x(), exit.get_y(), exit.get_weight())
    ped = Pedestrian(4,4,4,0)
    print "before: this loc type is %s, axes are (%s, %s), weight is %s" \
            % (ped.get_loc_type(), ped.get_x(), ped.get_y(), ped.get_exit_num())
    ped.set_x(150)
    ped.set_y(50)
    ped.set_exit_num(99)
    print "after: this loc type is %s, axes are (%s, %s), weight is %s" \
            % (ped.get_loc_type(), ped.get_x(), ped.get_y(), ped.get_exit_num())
