import random
import sys
def generate_exact_speed_coeffs():
    """
    Generates three machine speed coefficients with exact decimal parts.
    """
    return [round(random.uniform(1, 2), 2) for _ in range(3)]

def generate_and_save_problem_instances(start=50, end=500, step=50):
    
    for n in range(start, end + 1, step):
        # Generate machine speed coefficients
        speed_coeffs = generate_exact_speed_coeffs() + [1, 1, 1]  # Ensuring at least two machines have coefficient 1

        # Generate task parameters
        tasks = []
        for _ in range(n):
            p = random.randint(*time_range)  # Task duration
            r = random.randint(0, p * 2)  # Readiness time
            d_factor = random.uniform(*due_date_factor)
            d = r + int(p * d_factor)  # Due date
            tasks.append((p, r, d))

        # Format the output
        output = f"{n}\n"
        output += " ".join([f"{b:.2f}" for b in speed_coeffs]) + "\n"
        for p, r, d in tasks:
            output += f"{p} {r} {d}\n"

        with open('in_148240_' +str(n) +'.txt', 'w') as file:
            file.write(output)

time_range = (1, 100)
due_date_factor = (1.5, 2.0)

generate_and_save_problem_instances()
