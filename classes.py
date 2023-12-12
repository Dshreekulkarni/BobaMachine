""" This module contains the classes and all the functions that implement the 
    features of the boba machine. 
    
    Classes : 
    ---------
    Stock
    ShowMenu
    FulfillOrder
    
    Functions : 
    -----------
    working()
    
"""


import pandas as pd  


class Stock():
    """ Class that stores inventory information and methods to update inventory."""
    
    def __init__(self):
        
        #class attrivutes initialized when an object is created
        self.recipes = {
            'Starwberry boba milk tea' : ['Tea' , 'Milk' , 'Honey Boba' , 'Brown Sugar Syrup' , 'Strawberry pulp'] , 
            'Chocolate boba milk tea' : ['Tea' , 'Milk' , 'Honey Boba' , 'Brown Sugar Syrup' , 'Chocolate Syrup'] , 
            'Mocha boba milk tea' : ['Tea' , 'Milk' , 'Honey Boba' , 'Brown Sugar Syrup' , 'Espresso' , 'Chocolate Syrup'] ,
            'Mango boba milk tea' : ['Tea' , 'Milk' , 'Honey Boba' , 'Brown Sugar Syrup' , 'Mango extract'] , 
            'Graperfruit boba milk tea' : ['Tea' , 'Milk' , 'Honey Boba' , 'Brown Sugar Syrup' , 'Graperfruit extract'] 
            }
        
        self.drink_names = list(self.recipes.keys())
        self.items = list(self.ingredients.keys())
        self.units = list(self.ingredients.values())
    
    #class attribute
    ingredients = { 
            'Tea' : 10 ,  
            'Milk' : 0 , 
            'Honey Boba' : 10 ,
            'Brown Sugar Syrup' : 10 ,
            'Chocolate Syrup' : 5 ,
            'Espresso' : 5 , 
            'Strawberry pulp' : 10 , 
            'Graperfruit extract' : 5 , 
            'Mango extract' : 10 , 
            }
   
    #class method
    def display(self, item):
        """Displays whether the item s in stock or out of stock. 
        
        Parameters 
        ----------
        item : string 
            String that contains the name of a ingredient.
            
        Returns 
        -------
        in_stock : Boolean 
            Boolean that contains the status of the stock of the item. 
        """
        
        in_stock = True
        if self.ingredients[item] > 0 : 
            in_stock = True 
        else : 
            in_stock = False 
            print("Restock " , item , " .")
        return in_stock
        
    def restock(self, item):
        """Updates the stock list based on how many units of an item were 
            restocked. 
            
            Parameters
            ----------
            item : string
                Stores the name of the ingredient to be restocked.

            Returns 
            -------
            ingredients : dictionary 
                Dictionary of the ingredients and their current stock.
        """
        
        #while loop to assist staff if they accidentally type an invalid response.
        valid = True
        while valid == True:
            units = input("How many units did you restock?")
            try :
                self.ingredients[item] = int(units)
                break 
            except :
                print("Enter a number!") 
        
        return self.ingredients
                    
    def update_stock(self, item):
        """Updates the stock everytime an ingredient is used.
        
            Parameters
            ----------
            item : string 
                String that stores the name of the ingredient.
                
            Returns 
            -------
            ingredients : dictionary 
                Dictionary of the ingredients and their current stock.
        """
        
        if self.ingredients[item] > 0 : 
            self.ingredients[item] -= 1
        return (self.ingredients)
        
    def check_stock(self):
        """Displays a dataframe of the inventory if the staff wishes to see it. """
        
        #creating a dataframe of the inventory. 
        dict = {'    Item     ' : self.items , ' Units ' : self.units}
        df = pd.DataFrame(dict , [1, 2, 3, 4, 5, 6, 7, 8, 9])  
        print(df)
        
        
class ShowMenu():
    """Class that displays the menu with prices of the drinks."""
    
    def __init__(self):
        #class attrbutes 
        self.price = 6.5
        
    def display(self):
        """Displays the menu as a dataframe."""
                
        #creating a dataframe of the menu. 
        dict = {'     Drink         ' : Stock().drink_names , ' Price' : self.price}
        df = pd.DataFrame(dict , [1, 2, 3, 4, 5])
        print(df)
        print()
             
            
class FulfillOrder():
    """Class that helps in taking, making and billing orders."""    
    
    def order(self):
        """Takes an order."""
        
        #while loop to assist staff if they accidentally type an invalid response.
        valid = True
        while valid == True:
            drink_number = int(input("Drink number: "))
            print()
            try :
                drink = Stock().drink_names[drink_number - 1]  #getting the name of the drink      
                print(f"Make {drink}.")
                break 
            except :
                print("You typed a wrong number.")
                print()
        
        #calls the instructions method and passes the drink name through it. 
        self.instructions(drink)
        
    def instructions(self, drink_name):
        """Displays instructions to make the drink.
        
        Parameters 
        ----------
        drink_name : string 
            Stores the name of the drink to be made.     
        """
        #for loop to add ingredients in order.
        for item in Stock().recipes[drink_name]:
            
            #if item is in stock
            if Stock().display(item) :  
                print(f"Add {item}. \n    Then press enter.")
                input()            
            #if item is not in stock.
            else :  
                restocked = input("Press enter after restocking to continue.")
                Stock().restock(item)  #calling the restock method from Stock class.
                print()
                print(f"Add {item}. \n    Then press enter.")
                input()
                print()
                
            Stock().update_stock(item)  #calling the update_stock method from Stock class.
             
            
        print("Proceed to billing.")
        print()
           
    def generate_bill(self):
        """Generates the bill."""
        
        bill = 0.0
        make_bill = input("Press enter when customer is ready to pay: ") 
        bill = ShowMenu().price  #calculates the bill.
        print(f"Amount due: ${bill} .")
        
        self.calculate_change(bill)  #calls the calculate_change method.
    
    def calculate_change(self, bill):
        """Calculates the change to be paid back to the customer.
        
        Parameters 
        ----------
        bill : float 
            Amount to be paid by the customer
        """
        
        #while loop to assist staff if they accidentally type an invalid response.
        valid = True
        while valid == True:
            money_received = input("Money recieved: ")  #how much did the customer pay?
            try :
                change = float(money_received) - bill  #how much to return to the customer
                print(f"Return ${change} .")
                break 
            except :
                print("Enter a number!") 
                                
    def check_stock(self):
        """Ask the staff if they want to review the stock of items."""
    
        #while loop to assist staff if they accidentally type an invalid response.
        valid = True
        while valid == True:
            check = input("Do you want to check the current stock of ingredients? Y or N?").lower()    
            if check == 'y' :
                Stock().check_stock()  #calling the check_stock method from Stock class.
                break
            elif check == 'n' :
                break
            else : 
                print("Invalid. Y or N? ")
                     
    def next_order(self, take_order = True):
        """Begins the next order when the staff is ready.
        
           Parameters 
           ----------
           take_order : Boolean 
               Boolean that stores if the next order should begin.
        """
        
        #while loop to assist staff if they accidentally type an invalid response.
        next_order = True
        while next_order == True:
            take_order = input("Press Y to begin next order.").lower()
            if take_order == 'y':
                #go through the entire ordering process again.
                print()
                ShowMenu().display()
                self.order()  
                self.generate_bill()
                self.check_stock()
            else : 
                print("Invalid")
                print()
                
                            
def working():
    """Creating objects and calling methods in sequence."""
    
    boba_order = ShowMenu()
    boba_order.display()
    boba_order = FulfillOrder()
    boba_order.order()
    boba_order.generate_bill()
    boba_order.check_stock()
    boba_order.next_order()
            
        
        
        