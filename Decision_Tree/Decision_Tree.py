# Render our plots inline
 
import pandas as pd
import matplotlib.pyplot as plt
import random
from sklearn import tree
import numpy as np
import math
import copy

class Decision_Tree:
    def __init__(self):
        self.start = None
    
    def set_Start(self,group):
        atr_max = 0
        for i in range(1,group.get_SL()):
            if group.get_I(i).get_Gain() > group.get_I(atr_max).get_Gain():
                atr_max = i
        self.start = Leaf(group.get_I(atr_max))

    def print_Start(self):
        print("= = = = = = = =     start     = = = = = = = =")
        self.start.print_At()

class Leaf:
    def __init__(self):
        self.node = None 
        self.next = None
    def set_note(self,group):
        self.node = group
    def set_next(self,group):
        self.node = group

    

class Group_Cata:
    def __init__(self):
        self.group = []
        self.SL = 0

    def get_I(self,pos):
        return self.group[pos]
    def get_SL(self):
        return self.SL

    def add_Group(self,cata):
        self.group.append(cata)
    def sort_Cata(self,a,b):
        n = len(a)
        for i in range(n): 
            for j in range(0, n-i-1):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    b[j], b[j+1] = b[j+1], b[j]
    def chia_Nhom(self,line,y_train):
        a = line
        b = copy.copy(y_train)
        self.sort_Cata(a,b)

        n = len(a)
        so_luong = n
        so_luong_thuoc_tinh = 0
        thuoc_tinh_CTL = []
        num_of_y = 0
        num_of_n = 0

        for i in range(0,n-1):
            if b[i] == 1:
                num_of_y += 1
            else:
                num_of_n += 1

            if a[i] != a[i+1]:
                thuoc_tinh_CTL.append(Atribute(num_of_y,num_of_n))
                so_luong_thuoc_tinh += 1
                num_of_y = 0
                num_of_n = 0

        if b[n-1] == 1:
            num_of_y += 1
        else:
            num_of_n += 1
        thuoc_tinh_CTL.append(Atribute(num_of_y,num_of_n))
        so_luong_thuoc_tinh += 1

        self.SL += 1
        self.add_Group(Catalog("Thuoc tinh " + str(self.SL),so_luong,so_luong_thuoc_tinh,thuoc_tinh_CTL))

class Result:
    def __init__(self):
        self.num_of_yes = 0
        self.num_of_no = 0
        self.tong = 0
        self.entropy_s = 0;
    
    def set_Y(self,num_of_yes):
        self.num_of_yes = num_of_yes
    def set_N(self,num_of_no):
        self.num_of_no = num_of_no
    def set_Y_N_T(self,b):
        n = len(b)
        for i in range(0,n):
            if b[i] == 1:
                self.num_of_yes += 1
            else:
                self.num_of_no += 1
        self.tong = self.num_of_yes + self.num_of_no
        print("Y N : ",self.num_of_yes, " ", self.num_of_no)
    # Co the dung ham ao
    def set_Entropy_S(self):
        value_y = (self.num_of_yes)/(self.num_of_yes+self.num_of_no)
        print("value_y: ",value_y)
        value_n = (self.num_of_no)/(self.num_of_yes+self.num_of_no)
        print("value_n: ",value_n)
        if value_y == 0 or value_n == 0:
            self.entropy_s = 0
        else: 
            self.entropy_s = -1*(value_y*math.log2(value_y) + value_n*math.log2(value_n))
        print("Entropy S: ",self.entropy_s)
    
    def get_Y(self):
        return self.num_of_yes
    def get_N(self):
        return self.num_of_no
    def get_Entropy_S(self):
        return self.entropy_s


class Catalog:
    def __init__(self,name, so_luong,so_luong_thuoc_tinh,thuoc_tinh_CTL):
        self.name = name
        self.so_luong = so_luong
        self.so_luong_thuoc_tinh = so_luong_thuoc_tinh
        self.thuoc_tinh_CTL = thuoc_tinh_CTL
        self.entro_cata = 0.0
        self.gain = 0.0

    def set_So_Luong(self,so_luong):
        self.so_luong = so_luong 
    def set_So_Luong_Thuoc_Tinh(self,so_luong_thuoc_tinh):
        self.so_luong_thuoc_tinh = so_luong_thuoc_tinh
    def set_Thuoc_Tinh_CTL(self,thuoc_tinh_CTL):
        self.thuoc_tinh_CTL = thuoc_tinh_CTL
    def set_Entro_Cata(self):
        for i in range(0,self.so_luong_thuoc_tinh):
            self.thuoc_tinh_CTL[i].set_Entro_Atri()
            rate = (self.thuoc_tinh_CTL[i].get_Tong()) / (self.so_luong)
            self.entro_cata += rate*self.thuoc_tinh_CTL[i].get_Entro_Atri()
    def set_Gain(self,entro_s):
        self.gain = entro_s - self.entro_cata
    
    def get_So_Luong(self):
        return self.so_luong
    def set_So_Luong_Thuoc_Tinh(self):
        return self.so_luong_thuoc_tinh
    def get_Thuoc_Tinh_CTL(self):
        return  self.thuoc_tinh_CTL
    def get_Entro_Cata(self):
        return self.entro_cata
    def get_Gain(self):
        return self.gain

    def print_At(self):
        #print(self.so_luong)
        #print(self.so_luong_thuoc_tinh)
        #for i in range(0,self.so_luong_thuoc_tinh):
        #    self.thuoc_tinh_CTL[i].print_YN()
        print(self.name, " : ")
        print("Entropy: ",self.entro_cata)
        print("Gain: ",self.gain)
        print("= = = = = = = = = = = = = = = = = = = = = = =")    


class Atribute:
    def __init__(self,num_of_yes,num_of_no):
        self.num_of_yes = num_of_yes
        self.num_of_no = num_of_no
        self.entro_atri = 0
        self.tong = num_of_yes + num_of_no

    def set_Y(self,num_of_yes):
        self.num_of_yes = num_of_yes
    def set_N(self,num_of_no):
        self.num_of_no = num_of_no
    # Co the dung ham ao
    def set_Entro_Atri(self):
        value_y = (self.num_of_yes)/(self.num_of_yes+self.num_of_no)
        value_n = (self.num_of_no)/(self.num_of_yes+self.num_of_no)
        if value_y == 0 or value_n == 0:
            self.entro_atri = 0
        else: 
            self.entro_atri = -1*(value_y*math.log2(value_y) + value_n*math.log2(value_n))
    
    def get_Y(self):
        return self.num_of_yes
    def get_N(self):
        return self.num_of_no
    def get_Tong(self):
        return self.tong
    def get_Entro_Atri(self):
        return self.entro_atri

    def print_YN(self):
        print(self.num_of_yes, " ", self.num_of_no)


sheet_df = pd.read_csv('tennis.csv')
print(sheet_df)
print("======================")

row, col = sheet_df.shape

data_train = sheet_df.iloc[0:row, 1:col-1].values
result_data_train = sheet_df.iloc[0:row, col-1:col].values

table = np.transpose(data_train)
result_data_train = np.transpose(result_data_train)

num_of_catalog, num_of_data = table.shape

group_cata = Group_Cata()

result = Result()
result.set_Y_N_T(result_data_train[0])
result.set_Entropy_S()
decision_tree = Decision_Tree()
print()
print()

for i in range(0,num_of_catalog):
    print("=========     ", "Catalog ", i+1, "     =========")
    group_cata.chia_Nhom(table[i],result_data_train[0])
    group_cata.get_I(i).set_Entro_Cata()
    group_cata.get_I(i).set_Gain(result.get_Entropy_S())
    group_cata.get_I(i).print_At()
    print()
    print()

decision_tree.set_Start(group_cata)
decision_tree.print_Start()



#print("Entropy S : ",result.get_Entropy_S) 
#print("======================")
#for i in range(0,num_of_catalog):
#    print("Entropy ", i+1, " : ", group_cata.get_I(i).get_Entro_Cata())
#print("======================")
#for i in range(0,num_of_catalog):
#    print("Gain ", i+1, " : ",group_cata.get_I(i).get_Gain())
print("\n\n========================")
    







