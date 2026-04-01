weight = 400

#Ground Shipping 
if weight <= 2: 
  ground_cost = (weight * 1.50) + 20.00
  print("Ground Shipping: ", ground_cost)
elif weight > 2 and weight <= 6: 
  ground_cost = (weight * 3.00) + 20.00
  print("Ground Shipping: ", ground_cost) 
elif weight > 6 and weight <= 10: 
  ground_cost = (weight * 4.00) + 20.00
  print("Ground Shipping: ", ground_cost)
else: 
  ground_cost = (weight * 4.75) + 20.00
  print("Ground Shipping: ", ground_cost)

#Ground Shipping Premium 
premium_cost = 125
print("Ground Shipping Premium: ", premium_cost)

#Drone Shipping
if weight <= 2: 
  drone_cost = (weight * 4.50)
  print("Drone Shipping: ", drone_cost)
elif weight > 2 and weight <= 6: 
  drone_cost = (weight * 9.00)
  print("Drone Shipping: ", drone_cost)
elif weight > 6 and weight <= 10: 
  drone_cost = (weight * 12.00)
  print("Drone Shipping: ", drone_cost)
else: 
  drone_cost = (weight * 14.25)
  print("Drone Shipping: ", drone_cost)

cheapest = min(ground_cost, premium_cost, drone_cost)
print("Cheapest Option: ", "$", cheapest)

