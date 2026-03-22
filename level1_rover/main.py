import math

# --- STEP 1: DISTANCE CALCULATION ---
print("--- Rover Navigation: Task 1 ---")
x1 = float(input("Origin X1: "))
y1 = float(input("Origin Y1: "))
x2 = float(input("Destination X2: "))
y2 = float(input("Destination Y2: "))

# Euclidean distance: sqrt(dx^2 + dy^2)
dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# --- STEP 2: PHYSICS INPUTS ---
v0 = float(input("Initial Velocity (m/s): "))
a = float(input("Acceleration (m/s^2): "))
v_max = float(input("Top Speed (m/s): "))

# --- STEP 3: ACCELERATION PHASE ---
if a > 0:
    # Time and distance needed to reach top speed
    t_to_max = (v_max - v0) / a
    d_accel = (v0 * t_to_max) + (0.5 * a * (t_to_max**2))
else:
    t_to_max = 0
    d_accel = 0

# --- STEP 4: MOTION LOGIC ---
if d_accel >= dist:
    # Scenario: Destination reached while still accelerating
    if a > 0:
        # Solve quadratic: d = v0t + 0.5at^2
        total_time = (-v0 + math.sqrt(v0**2 + 2 * a * dist)) / a
    else:
        total_time = dist / v0
else:
    # Scenario: Reaches top speed then cruises at constant velocity
    remaining_dist = dist - d_accel
    t_cruise = remaining_dist / v_max
    total_time = t_to_max + t_cruise

# --- STEP 5: OUTPUT ---
print("\n--- TRAVEL SUMMARY ---")
print(f"Total distance: {dist:.2f} m")
print(f"Total time: {total_time:.2f} seconds")