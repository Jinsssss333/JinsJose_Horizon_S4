# 🚀 Rover Navigation System

A Python program that calculates the **distance** and **travel time** for a rover moving between two points on a 2D plane using basic kinematics.

---

## 📌 Functionality

### 📍 Distance
**Distance = √[(x₂ − x₁)² + (y₂ − y₁)²]**

---

### ⏱️ Time Calculation

Inputs:
- Initial velocity (v₀)
- Acceleration (a)
- Maximum speed (vₘₐₓ)

**Cases:**

- If the rover reaches the destination during acceleration:  
  **Time = [−v₀ + √(v₀² + 2ad)] / a**

- If the rover reaches maximum speed first:  
  **Total time = tₐcc + (remaining distance / vₘₐₓ)**

---

### ⚠️ Error Handling
- Handles non-numeric inputs  
- Prevents division by zero  
- Rejects invalid cases (e.g., zero velocity & acceleration, negative values)

---

## ▶️ Run

```bash
python main.py