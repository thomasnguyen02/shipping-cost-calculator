weight = 1

# Ground Shipping 
if weight <= 2: 
  ground_cost = (weight * 1.50) + 20.00
elif weight <= 6: 
  ground_cost = (weight * 3.00) + 20.00
elif weight <= 10: 
  ground_cost = (weight * 4.00) + 20.00
else: 
  ground_cost = (weight * 4.75) + 20.00 
print("Ground Shipping Cost:", ground_cost)

# Ground Shipping Premium 
premium_cost = 125.00
print("Ground Shipping Premium Cost:", premium_cost)

# Drone Shipping
if weight <= 2: 
  drone_cost = (weight * 4.50)
elif weight <= 6: 
  drone_cost = (weight * 9.00)
elif weight <= 10: 
  drone_cost = (weight * 12.00)
else: 
  drone_cost = (weight * 14.25)
print("Drone Shipping Cost:", drone_cost)

cheapest = min(ground_cost, premium_cost, drone_cost)
print("Cheapest Option: $", cheapest)
