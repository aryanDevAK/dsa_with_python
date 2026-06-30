# 7_3_evacuate_to_moon.py
"""
Greedy solution for the EVacuate to Moon problem (CodeChef MOONSOON).
Pairs the largest electric car battery capacities with the largest charging outlet outputs descendingly.
"""

def max_energy_stored(cars: list, outlets: list, hours: int) -> int:
    """
    Calculates the maximum total energy (in Wh) stored after hours charging.
    Time Complexity: O(N log N + M log M) where N is len(cars) and M is len(outlets).
    Space Complexity: O(1) auxiliary space (descending sort in-place).
    Returns: Max total stored energy.
    """
    # Sort both arrays in descending order to match largest capacities with largest charging outputs
    cars.sort(reverse=True)
    outlets.sort(reverse=True)
    
    total_energy = 0
    # Pair-match capacities and outlet powers
    for i in range(min(len(cars), len(outlets))):
        charging_limit = outlets[i] * hours
        total_energy += min(cars[i], charging_limit)
        
    return total_energy

if __name__ == "__main__":
    # Self-testing assertions
    # Cars capacities: [10, 20, 30], Outlets outputs: [5, 10], Hours: 2
    # Outlets capacity-per-outlet: [5*2, 10*2] = [10, 20]
    # Descending capacities: [30, 20, 10]
    # Descending outlet capacity limits: [20, 10]
    # Match: min(30, 20) + min(20, 10) = 20 + 10 = 30 Wh.
    assert max_energy_stored([10, 20, 30], [5, 10], 2) == 30
    
    # 2 cars, 3 outlets, 1 hour
    # Cars: [15, 10], Outlets: [20, 15, 5] -> capacity limits: [20, 15, 5]
    # Match: min(15, 20) + min(10, 15) = 15 + 10 = 25 Wh.
    assert max_energy_stored([10, 15], [20, 15, 5], 1) == 25
    
    # Empty cases
    assert max_energy_stored([], [10, 20], 5) == 0
    assert max_energy_stored([10, 20], [], 5) == 0
    assert max_energy_stored([10, 20], [10, 20], 0) == 0
    
    print("7_3_evacuate_to_moon.py verified successfully!")
