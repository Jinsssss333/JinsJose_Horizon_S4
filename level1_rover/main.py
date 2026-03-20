import math

def calculate_rover_motion():
    print("--- Rover Navigation System: Task 1 ---")
    
    try:
        # Part A: Rover Coordinates
        x1 = float(input("Enter Origin X1: "))
        y1 = float(input("Enter Origin Y1: "))
        x2 = float(input("Enter Destination X2: "))
        y2 = float(input("Enter Destination Y2: "))

        # Calculate Euclidean Distance
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        # Part B: Motion Parameters
        v0 = float(input("Enter Initial Velocity (m/s): "))
        a = float(input("Enter Acceleration (m/s^2): "))
        v_max = float(input("Enter Top Speed (m/s): "))

        # Error Handling for physical impossibilities
        if a <= 0 and v0 == 0:
            print("Error: Rover cannot move with zero acceleration and zero initial velocity.")
            return
        if distance < 0 or v0 < 0 or v_max < 0:
            print("Error: Distance and velocity values must be non-negative.")
            return

        # Time to reach top speed: v = v0 + at  => t = (v - v0) / a
        if a > 0:
            t_accel = (v_max - v0) / a
            # Distance covered during acceleration: s = v0t + 0.5at^2
            d_accel = (v0 * t_accel) + (0.5 * a * (t_accel**2))
        else:
            t_accel = 0
            d_accel = 0

        if d_accel >= distance:
            # Case 1: Rover reaches destination before hitting top speed
            # Solve quadratic: 0.5*a*t^2 + v0*t - distance = 0
            if a > 0:
                # Quadratic formula: t = (-b + sqrt(b^2 - 4ac)) / 2a
                t_total = (-v0 + math.sqrt(v0**2 + 2 * a * distance)) / a
            else:
                t_total = distance / v0
        else:
            # Case 2: Rover hits top speed, then cruises
            d_remaining = distance - d_accel
            t_cruise = d_remaining / v_max
            t_total = t_accel + t_cruise

        # Output Results
        print("\n--- Results ---")
        print(f"Distance to destination: {distance:.2f} m")
        print(f"Time required: {t_total:.2f} seconds")

    except ValueError:
        print("Error: Please enter valid numerical values.")
    except ZeroDivisionError:
        print("Error: Division by zero encountered. Check acceleration and velocity inputs.")

if __name__ == "__main__":
    calculate_rover_motion()