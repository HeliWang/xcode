import random
class RandomizedSet(object):
    # No duplicate number
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # List + Dict
        self.vals, self.pos = [], {} # val -> pos

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.pos[val] = len(self.vals)
            self.vals.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False
        else:
            val_pos = self.pos[val]
            self.vals[val_pos] = self.vals[-1]
            self.pos[self.vals[val_pos]] = val_pos
            del self.pos[val]
            self.vals.pop()
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.vals:
            return self.vals[random.randrange(len(self.vals))]
