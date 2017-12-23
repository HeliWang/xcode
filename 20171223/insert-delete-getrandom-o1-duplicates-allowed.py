class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # List + Dict
        self.vals, self.pos = [], {} # val -> pos list

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        pos_lst = self.pos.get(val, set())
        pos_lst.add(len(self.vals))
        self.pos[val] = pos_lst
        self.vals.append(val)
        return len(self.pos[val]) == 1

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False
        else:
            val_pos_list = self.pos[val]
            val_pos = val_pos_list.pop()
            if val_pos != len(self.vals) - 1:
                self.vals[val_pos] = self.vals[-1]
                self.pos[self.vals[val_pos]].remove(len(self.vals) - 1)
                self.pos[self.vals[val_pos]].add(val_pos)
            self.vals.pop()
            if len(val_pos_list) == 0:
                del self.pos[val]
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.vals:
            return self.vals[random.randrange(len(self.vals))]
