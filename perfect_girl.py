# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:44:05 2020
@author: EKMARTI
"""
class Girl:
    
    def __init__(self, first_name, last_name, skin_color, eye_color, hair_color):
        self.first_name = first_name
        self.last_name = last_name
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.hair_color = hair_color
        
    def describe_girl(self):
        print("\nPerfect Girl:")
        print("-------------------------------")
        print("First name: " + self.first_name + " " + self.last_name + ".")
        print("Skin color: " + self.skin_color)
        print("Eye color: " + self.eye_color)
        print("Hair color: " + self.hair_color)
        print("-------------------------------")
        
    def compliment_girl(self):
        
        comp = "\n"+ self.first_name + ",\n\n" + "Charming name!\nI see the heavens in your eyes.\n" + \
              "Would you take me there?,\n" + "to the space where it burns,\n" + "like the fire in your big, stunning\n" + \
              "beautiful, shinny " + self.eye_color + " eyes.\n\n" + \
              "Let the color of your " + self.skin_color + " skin\n" + "get along with mine,\n" + \
              "like the colors in my canvas,\n" + "precious " + self.first_name +"\n\n" + \
              "Would you cover my shadows\n" + "under your heavenly, bold, long \n" + self.hair_color + " hair?\n"
        print(comp)

def runner():
    print("\nEnter desired details: \n")
    name_get = input("\nEnter her first name: ")
    last_name_get = input("Enter her last name: ")
    skin_color_get = input("Enter her skin color: ")
    eye_color_get = input("Enter her eye color: ")
    hair_color_get = input("Enter her hair color: ")

    girl = Girl(name_get, last_name_get, skin_color_get, eye_color_get, hair_color_get)

    girl.describe_girl()
    girl.compliment_girl()

if __name__ == "__main__":
    runner()