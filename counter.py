# import os
# import pandas
# from pprint import pprint
from collections import OrderedDict
# import logging

## from framechecker we get the frame number and the time period
# import frame_checker

# frame
#     frame_num
#     frame_time
#     dict
#         small_car
#         big_car
#         buses
#         three_wheeler
#         LCV
#         two_wheeler
#         trucks
#         bycycle
#         pedestrian
#     mv_data
#

class count():
    def __init__(self):

        # self.data = {-1:{"frame_path":"",
        #                "classes":{  "small_car":[],
        #                             "big_car":[],
        #                             "buses":[],
        #                             "three_wheeler":[],
        #                             "LCV":[],
        #                             "two_wheeler":[],
        #                             "trucks":[],
        #                             "bicycle":[],
        #                             "pedestrian":[]
        #                               },
        #                  "target_frame": True
        #                  }
        #
        #         }
        self.data = {}


    def set(self, imagename):
        imageparams = imagename.strip().split("/")[-1].split("_")
        frame = imageparams[1].split("time")[0]
        time = float(imageparams[-1].split(".jpg")[0])

        self.data[int(frame)] = {"frame_path":imagename,
                       "frame_time":time,
                       "classes":{  "small_car":[],
                                    "big_car":[],
                                    "buses":[],
                                    "three_wheeler":[],
                                    "LCV":[],
                                    "two_wheeler":[],
                                    "trucks":[],
                                    "bicycle":[],
                                    "pedestrian":[]
                                      },
                            "target_frame":False
                         }
    def set_target_as_zero(self):
        self.data[0]["target_frame"] = True

    def sort_dict(self):
        # pprint(self.data.items())
        self.data = OrderedDict(sorted(self.data.items()))

    def find_target_frame(self):
        # print(type(self.data))
        for keys, vals in self.data.items():
            # print(keys, self.data[keys]["frame_path"], self.data[keys]["target_frame"])
            if self.data[keys]["target_frame"] == True:
                return keys

    def set_target_frame(self, k):
        if k > len(self.data) or k < 0:
            return False, ""
        else:
            for keys, vals in self.data.items():
                self.data[keys]["target_frame"] = False
            self.data[k]["target_frame"] = True
            return True, self.data[k]["frame_path"]

    def add_entity(self, entity):
        keyy = self.find_target_frame()
        self.data[keyy]["classes"][entity].append(1)

    def remove_entity(self, entity):
        keyy = self.find_target_frame()
        self.data[keyy]["classes"][entity] = self.data[keyy]["classes"][entity][:-1]


    def clear_data(self):
        # to clear all the values in the dictionary for new video
        for value in self.data:
            print(value)

    def display_all(self):
        return self.data

    def display(self, k):
        return self.data[k]

    # def addValue(self, item):
    #     self.data
