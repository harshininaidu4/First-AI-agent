for iteration in range(1, 4):
  print(f"\n--- Iteration {iteration} ---")

  # 1. Observe
  observation = input("Observe: Enter current situation: ")
  normalized_observation = observation.lower()

  # 2. Decide
  if "rain" in normalized_observation:
    decision = "Carry an umbrella"
  elif "hot" in normalized_observation:
    decision = "Drink water"
  else:
    decision = "Continue normally"

  print("Decide:", decision)

  # 3. Act
  print("Act:", decision)

print("\nAgent loop completed after 3 iterations.")