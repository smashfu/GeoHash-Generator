import numpy as np
import pygeohash as gh
import pandas as pd


class GeoHash_ada_bd:
    def __init__(self):
        pass

    def v_up(self, start_lat, fixed_lng, stop_lat):
        gap = 0.001375
        start_lat = start_lat + (gap / 2)
        stop_lat = stop_lat - (gap / 2)
        lat_list = np.arange(start_lat, stop_lat, gap)
        print(lat_list)
        if len(lat_list) == 0:
            lat_list = [(start_lat + stop_lat) / 2]
            print(lat_list)
        hash_list = []
        for lat in lat_list:
            hash_list.append(gh.encode(lat, fixed_lng, precision=7))
        return hash_list

    def h_right(self, start_lng, fixed_lat, stop_lng):
        gap = 0.001375
        start_lng = start_lng + (gap / 2)
        stop_lng = stop_lng - (gap / 2)
        lng_list = np.arange(start_lng, stop_lng, gap)
        print(lng_list)
        if len(lng_list) == 0:
            lng_list = [(start_lng + stop_lng) / 2]
            print(lng_list)
        hash_list = []
        for lng in lng_list:
            hash_list.append(gh.encode(fixed_lat, lng, precision=7))
        return hash_list