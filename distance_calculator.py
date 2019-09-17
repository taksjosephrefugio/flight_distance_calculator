#################################################################
# This program takes in a textfile as an input. This textfile 
# contains data that the program can parse and recognize. 
# Using said data, this program can then calculate the distance
# covered between two locations as indicated by the data
#
# This is a program I developed as part of the requirements
# needed for an internship position for a trading firm
# 
# Code written by: Taks Joseph Refugio
# Code written for: Trading firm for internship opportunity
# 
# Version: Compilable and Stable but with Issue
# Issue: Formatting
# Last worked on:09/17/2019 18:48
################################################################

import fileinput
from math import acos, sin, cos, radians, floor
RADIUS_MILES = 3963

class DestinationCalculator:
    def __init__(self):
    	self.location = []
    	self.latitude = []
    	self.longitude = []

    	self. index = []
    	self.phi = []
    	self.kappa = []
    
    def process(self, line: str) -> str:
    	line = line.split(":")
    	
    	if line[0] == 'LOC':
    		self.location.append(line[1])
    		self.latitude.append(self.conv_rad(float(line[2])))
    		self.longitude.append(self.conv_rad(float(line[3])))

    	if line[0] == 'TRIP':
    		self.get_location_index(line[2])
    		self.get_location_index(line[3])

    		self.get_phi()
    		self.get_kappa()

    		distance = self.compute_distance(self.phi[0], self.phi[1], self.kappa[0], self.kappa[1])
    		distance = int(distance)
    		
    		print(line[1] + ":" + line[2] + ":" + line[3] + ":" + str(distance))

    def conv_rad(self, deg):
    	return deg * 3.141592 / 180

    def get_location_index(self, location_str):
    	index = 0
    	for loc in self.location:
    		if loc == location_str:
    			break
    		else:
    			index += 1
    	self.index.append(index)

    def get_phi(self):
    	for i in self.index:
    		self.phi.append(self.latitude[i])

    def get_kappa(self):
    	for i in self.index:
    		self.kappa.append(self.longitude[i])

    def compute_distance(self, phi1, phi2, kappa1, kappa2):
    	gamma = abs(kappa1 - kappa2)
    	omega = acos((sin(phi1) * sin(phi2)) + (cos(phi1) * cos(phi2) * cos(gamma)))
    	distance = RADIUS_MILES * omega
    	return distance

# FIXME: Solve file input issues
if __name__ == "__main__":
    dest_calc = DestinationCalculator()
	
    for line in fileinput.input('input.txt'):
        cleaned_line = line.replace("\n", "")
        print(dest_calc.process(cleaned_line))