import random
import matplotlib.pyplot as plt
stock_prices = []
def simulate_stock_price(current_price, days):
    #Iterate through the amount of days required for simulation
    for i in range(days):
        #Add stock price to a list for graphing purposes
        stock_prices.append(current_price)
        #Generate a random number between 0 and 1 inclusive
        random_number = random.uniform(0, 1)
        # if the random number is less than .45, price movement is increase
        if random_number < 0.45:
            movement = "increase"
        # if the random number is between 0.45 and 0.75, price movement is same
        elif random_number < 0.75:
            movement = "same"
        # if the random number is between 0.75 and 1, price movement is decrease
        else:
            movement = "decrease"
        
        # Step 2
        if movement == "increase":
            # CDF of the price change amounts
            change_probabilities = [0.40, 0.57, 0.69, 0.79, 0.87, 0.94, 0.98, 1]
            
            change_amounts = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1]
            # Generate another random number
            random_number = random.uniform(0, 1)
            # Iterate through the CDF of change probabilities
            for j in range(8):
                # change amount will be the change amount that corresponds with the first change probability
                # in the CDF that is greater than the random number
                # This ensures that each change amount is selected with the correct proportion with 
                # respect to the given stock price change PDF
                
                if random_number < change_probabilities[j]:
                    current_price += current_price * change_amounts[j]
                    
                    break
        # if movement is same, do nothing 
        elif movement == "same":
            pass
        # same logic as for a price increase, with the change amounts as negative numbers to reflect
        # a price decrease
        else:
            change_probabilities = [0.12, 0.27, 0.45, 0.66, 0.80, 0.90, 0.95, 1]
            change_amounts = [-0.125, -0.25, -0.375, -0.5, -0.625, -0.75, -0.875, -1]
            random_number = random.uniform(0, 1)
            for j in range(8):
                if random_number < change_probabilities[j]:
                    current_price += current_price * change_amounts[j]
                    
                    break
    # After simulating the stock price for each day out of the total days return the current price
    return current_price

current_price = 62
days = 365
simulated_price = simulate_stock_price(current_price, days)
print(simulated_price)
plt.plot([x for x in range(1,days+1)],stock_prices)
plt.xlabel("DAY")
plt.ylabel("STOCK PRICE")
plt.title("Stock price on day")
plt.show()

