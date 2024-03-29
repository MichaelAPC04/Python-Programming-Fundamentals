"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It allows plotting an Itinerary as the picture of a map.

@file map_plotting.py
"""
from mpl_toolkits.basemap import Basemap #have to do 'pip install basemap'
import matplotlib.pyplot as plt
from itinerary import Itinerary
from city import City

def plot_itinerary(itinerary: Itinerary, projection = 'robin', line_width=2, colour='b') -> None:
    """
    Plots an itinerary on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.

    :param itinerary: The itinerary to plot.
    :param projection: The map projection to use.
    :param line_width: The width of the line to draw.
    :param colour: The colour of the line to draw.
    """

    Itinerary_Map = Basemap(projection="robin", lon_0=0) #set longitude to 0
    Itinerary_Map.fillcontinents(color=(0.8, 0.467, 0.133)) #formatting continent fill
    Itinerary_Map.drawmapboundary(fill_color="aqua") #formatting colour to aqua
    Itinerary_Map.drawcoastlines() #draw coast lines

    for i in range(len(itinerary.cities)-1): #begin looping through cities in itinerary
        current_city = itinerary.cities[i]
        next_city = itinerary.cities[i+1] #iterate through
        Itinerary_Map.drawgreatcircle(current_city.coordinates[1], current_city.coordinates[0], next_city.coordinates[1], next_city.coordinates[0], linewidth=line_width, color=colour)

    plt.show()
    itinerary_list = [] #create new empty list
    for i in range(len(itinerary.cities)): #iterates through each city
        itinerary_list.append(itinerary.cities[i].name) #gets the name of each city and appends it to the list
    plt.savefig("_".join(itinerary_list))

if __name__ == "__main__":
    # create some cities
    city_list = list()

    city_list.append(City("Melbourne", (-37.8136, 144.9631), "primary", 4529500, 1036533631))
    city_list.append(City("Sydney", (-33.8688, 151.2093), "primary", 4840600, 1036074917))
    city_list.append(City("Brisbane", (-27.4698, 153.0251), "primary", 2314000, 1036192929))
    city_list.append(City("Perth", (-31.9505, 115.8605), "1992000", 2039200, 1036178956))

    # plot itinerary
    plot_itinerary(Itinerary(city_list))

