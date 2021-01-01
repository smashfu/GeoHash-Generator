from GeoHash_ada_bd import GeoHash_ada_bd
import pandas as pd

if __name__ == '__main__':

    way = input("v_up or h_right ??: ")
    if way == 'v':
        print('VVVVVV')
        obj1 = GeoHash_ada_bd()
        start_lat = float(input("start_lat: "))
        fixed_lng = float(input("fixed_lng: "))
        stop_lat = float(input("stop_lat: "))
        result = obj1.v_up(start_lat, fixed_lng, stop_lat)
        df = pd.DataFrame(result)
        print(df.to_string(index=False))
    elif way == 'h':
        print("HHHHHHH")
        obj2 = GeoHash_ada_bd()
        start_lng = float(input("start_lng: "))
        fixed_lat = float(input("fixed_lat: "))
        stop_lng = float(input("stop_lng: "))
        result = obj2.h_right(start_lng, fixed_lat, stop_lng)
        df = pd.DataFrame(result)
        print(df.to_string(index=False))
