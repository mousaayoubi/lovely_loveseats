lovely_loveseat_description = """
Lovely Loveseat. Tufted polyster blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_settee_price = 180.50
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15

#Set sales tax to 8.8%
sales_tax = 0.088

#First customer total
customer_one_total = 0

#First customer itemization
customer_one_itemization = ""

#First customer purchased the Loveseat
customer_one_total = lovely_loveseat_price

#Add Lovely Loveseat descirtion to customer one itemization
customer_one_itemization = lovely_loveseat_description

#First customer also purchased the Luxurious Lamp
customer_one_total += luxurious_lamp_price

#Add Luxurious Lamp descirtion to customer one itemization
customer_one_itemization +=luxurious_lamp_description

#Calculate the sales tax
customer_one_tax = customer_one_total * sales_tax

#Add sales tax to customer one total
customer_one_total += customer_one_tax

#Print Receipt
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)