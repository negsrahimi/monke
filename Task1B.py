# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""
    
    p = (52.2053, 0.1218)
    
    # Build list of stations
    stations = build_station_list()

    # Get distances of stations from the given coordinate
    distances = stations_by_distance(stations, p)
    list_to_print = []
    for x in distances:
        list_to_print.append((x[0].name, x[0].town, x[1]))

    print("The 10 closest stations to Cambridge city centre are:")
    print(str(list_to_print[:10]) + "\n")

    print("The 10 stations furthest away from Cambridge city centre are:")
    print(list_to_print[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***\n")
    run()
