#class: AddressData

import requests #Used to make website requests
import json #Used to work with Json

#In General

import numpy as np
import pandas as pd
import os

class AddressData:

    def __init__(self):
        
        """
        Function that will start asking the user for an adress of a house and
        assign them to variables
        This function will return the variables: street_name, house_number, postal_code, town
        """
        
        self.street_name = input("Please enter a streetname: ")
        self.house_number = input("Please enter a house number: ")
        self.postal_code = input("Please enter a postal code: ")
        self.town = input("Please enter a town: ")

    
    def coordinates(self):
        
        """
        Function that will convert the given address into coordinates (EPSG:31370) using an API
        :API = https://api.basisregisters.vlaanderen.be/v1/adresmatch
        :attrib r_address wil contain the requests.get function
        :attrib data_address will contain the json.loads function
        This function will return the coordinates of the address
        """

        try: 
        
            r_address = requests.get("https://api.basisregisters.vlaanderen.be/v1/adresmatch",
                                    params={"straatnaam":self.street_name,
                                            "huisnummer":self.house_number,
                                            "postcode":self.postal_code,
                                            "gemeentenaam":self.town})
            data_address = json.loads(r_address.content)

            coordinates = data_address['adresMatches'][0]['adresPositie']['point']['coordinates']
        
            return coordinates, data_address

        except:
            print("THIS ADDRESS DOES NOT EXIST OR THE ADDRESS IS NOT YET IN THE GOVERNMENT DATABASE")
            print("PLEASE RESTART THE MAIN.PY SCRIPT AND TRY AGAIN")
    
    def polygon(self, data_address):
        
        """
        Function that will extract the polygon of a house using an API in coordinates (EPSG:31370) using and API
        :API = https://api.basisregisters.vlaanderen.be/v1/gebouweenheden/
        :attrib r_gebouweenheden wil contain the requests.get function
        :attrib data_gebouweenheden will contain the json.loads function
        :attrib r_polygon wil contain the requests.get function
        :attrib data_polygon will contain the json.loads function
        This function will return the coordinates (EPSG:3126) of the polygon shape of the house
        """
        
        objectId_adresserbareObjecten = data_address['adresMatches'][0]['adresseerbareObjecten'][0]['objectId'] 

        r_gebouweenheden = requests.get("https://api.basisregisters.vlaanderen.be/v1/gebouweenheden/" + objectId_adresserbareObjecten)
        data_gebouweenheden = json.loads(r_gebouweenheden.content)

        objectId_gebouw = data_gebouweenheden['gebouw']['objectId']

        r_polygon = requests.get("https://api.basisregisters.vlaanderen.be/v1/gebouwen/" + objectId_gebouw)
        data_polygon = json.loads(r_polygon.content)

        polygon = data_polygon['geometriePolygoon']['polygon']['coordinates']
        
        return polygon

