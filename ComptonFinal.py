#CS 241 Final Project
class Donations:

    class node:
    
        def __init__(self,data,less=None,more=None):
            self.data = data
            self.kids = [less,more]

    class Donation:

        def line_to_arr(self, line):
            loc = line.find("\"")
            new_str = line[:loc] + line[loc:].replace(",","_",1).strip()
            return new_str.split(",")

        def __repr__(self):
            return "DONOR: " + self.info[1] + " DONEE: " + self.info[2] + " VAL: " + self.info[0]
            
        def __str__(self):
            return self.__repr__()

        def __init__(self, line):
            arr = self.line_to_arr(line)
            #print(len(arr))
            #print(line)
            self.info = [arr[35], arr[13], arr[1]]
            
    def bst_insert(self, bst, ind, donation):
        if bst == None:
            return self.node(donation)
        if bst.data.info[ind] > donation.info[ind]:
            bst.kids[0] = self.bst_insert(bst.kids[0],ind,donation)
            #print('left')
        else:
            bst.kids[1] = self.bst_insert(bst.kids[1],ind,donation)
            #print('right')
        return bst

    def __init__(self,name):
        file = open(name,"r")
        file.readline()
        self.all_donations = []
        self.trees = [None, None, None]
        prefix = ""
        for line in file:
            line = prefix + line
            splits = line.split(",")
            #print(line)
            if len(splits) < 70:
                prefix = line
            else:
                curr = self.Donation(line)
                self.all_donations.append(curr)
                for i in [0,1,2]:
                    self.trees[i] = (self.bst_insert(self.trees[i],i,curr))
                    #print(self.trees[i].data)
            prefix = ""

    def bst_contains(self, bst, ind, string, same_donations):
        #print(bst.data.info[ind])
        #print(same_donations)
        if bst.data.info[ind] == string:
            #print('same')
            #print(bst.data)
            #print(same_donations)
            same_donations.append(bst.data) #attempting to recurse through and get all of the donations from this person
            if bst.kids[0] != None:
                self.bst_contains(bst.kids[0],ind,string, same_donations)
            if bst.kids[1] != None:
                self.bst_contains(bst.kids[1],ind,string, same_donations)
            return same_donations
        if bst.data.info[ind] > string and bst.kids[0]:
            #print('larger')
            return self.bst_contains(bst.kids[0],ind,string, same_donations)
        elif bst.kids[1]:
            #print('smaller')
            return self.bst_contains(bst.kids[1],ind,string, same_donations)

    # val, donor, donee
    def contains(self, ind, str):
        str = str.replace(",","_")
        if self.trees[ind]:
            return self.bst_contains(self.trees[ind], ind, '"' + str + '"', [])
            
        
ret = Donations("fec2.csv")
print(ret.all_donations[1])
print(ret.contains(1, "SCHMELING, MARK A. MR."))
#credit to Professor you for the majority of this code from in class