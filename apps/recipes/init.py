from .models import IngredientManager, Ingredients
import requests
import json
from xml.dom.minidom import parse, parseString
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps
import re
import xml.etree.cElementTree as et

data=[]
data.append(['Organic Baby Carrots','Organic Baby Carrots 16 oz'])
data.append(['80% Lean Ground Beef','1.30 LB 80% Lean Ground Beef Market 20% Fat'])
data.append(['Oven Roasted Chicken Breast ','Butterball Oven Roasted Chicken Breast'])
data.append(['Garlic Bread In Foil Bag','Garlic Bread In Foil Bag'])
data.append(['Organice Garlic','Earthbound Farm ORGANIC GARLIC 12/8Z'])
data.append(['Tomatoes on the Vine','Farm Fresh Tomatoes on the vine'])
data.append(['Spaghetti Sauce Seasoning Mix','Lawrys Spaghetti Sauce Seasoning Mix'])
data.append(['Spaghetti','Safeway Spaghetti'])
data.append(['Pure 100% Natural Canola Oil','Wesson Pure 100% Natural Canola Oil'])
data.append(['Oil Extra Virgin Olive Oil','Bertolli Oil Extra Virgin Olive Oil'])
data.append(['Fine Sea Salt','Morton Fine Sea Salt'])
data.append(['Ground Black Pepper','Mccormick Ground Black Pepper'])
data.append(['Garlic Powder','Mccormick Garlic Powder'])
data.append(['Seasoned Salt','Lawrys Seasoned Salt'])
data.append(['Soy Sauce','Kikkoman Soy Sauce '])
data.append(['Sesame Oil Pure','Dynasty Specialty Food Sesame Oil Pure '])
data.append(['Red Fresh Onion','Red Fresh Onion '])
data.append(['Sweet Fresh Onion','Sweet Fresh Onion '])
data.append(['Onion Powder','Safeway Onion Powder '])
data.append(['Chicken Broth','Safeway Chicken Broth  '])
data.append(['Beef Broth','Progresso 100% Natural Beef Broth '])
data.append(['Tomato Sauce','Hunts Tomato Sauce '])
data.append(['Parmesan Shredded','Sargento(R) Artisan Blends Parmesan Shredded'])
data.append(['Hot Dog Buns','Ball Park Hot Dog Buns '])
data.append(['Beef Franks Bun Length','Farm Fresh Tomatoes on the vine'])
data.append(['Celery','Celery'])
data.append(['White Fresh Potato','Whole White Fresh Potato'])
data.append(['French Bread Baguette','Safeway SELECT Artisan French Bread Baguette - Each'])
data.append(['Tombstone Extra Cheese Pizza','Tombstone Original Extra Cheese'])
data.append(['Cream Cheese','Kraft Philadelphia Cream Cheese '])
data.append(['Grade AA Large Eggs','Egglands Best Grade AA Large Eggs'])
data.append(['Cheese Fish Goldfish','Goldfish Cheddar Cheese Fish Goldfish '])
data.append(['Butter Half Sticks','Land O Lakes Butter Half Sticks '])
data.append(['Organic 2% Reduced Fat Milk','Horizon Organic 2% Reduced Fat Milk'])
data.append(['All Purpose Flour','Gold Medal All Purpose Flour - 5 Lb'])
data.append(['Fine Granulated Sugar','Safeway Fine Granulated Sugar'])
data.append(['Crushed Red Pepper','Spice Islands Crushed Red Pepper '])
data.append(['Honey Crisp Apples','Apples HONEY CRISP'])
data.append(['Whole Kosher Dill Pickles','Claussen Whole Kosher Dill Pickles'])
data.append(['Pork Shoulder Country Style Ribs','2 LB Pork Shoulder Country Style Ribs Boneless'])
data.append(['Stubbs Regular Original Barbecue Sauce','Stubbs Regular Original Barbecue Sauce '])
data.append(['Orange Juice','Floridas Natural Growers Style Orange Juice'])
data.append(['Whole Milk Mozzarella Cheese','Precious Whole Milk Mozzarella Cheese'])
data.append(['Long Grain White Rice','Long Grain White Rice '])
data.append(['Lettuce Green Leaf','Lettuce Green Leaf'])
data.append(['Bold and Spicy Brown Mustard','Frenchs Bold and Spicy Brown Mustard'])
data.append(['Easy Squeeze Ketchup','Heinz Easy Squeeze Ketchup'])
data.append(['Bagels Plain','Sara Lee Plain Mini Bagels '])
data.append(['Pepperoni Sliced','Hormel Pepperoni Sliced'])
data.append(['Dry Yeast','Fleischmanns Rapid Rise Yeast'])
data.append(['Specialty Herbs And Spices Ground','Specialty Herbs And Spices Ground '])
data.append(['Clover Honey Bear','Sue Bee Clover Honey Bear '])
data.append(['Water','NOITEM'])
data.append(['A&W Root Beer','A and W Root Beer Soda '])


def startup():
    for item in data:
        Ingredients.objects.addIngredient(item[0],item[1])
    return True
