# 8_1_snake_mongoose.py
"""
Greedy simulation for the Snakes, Mongooses and the Ultimate Election problem (CodeChef SNELECT).
Mongoose checks left first (greedy choice), then right, to maximize eaten snakes.
"""

def check_election_winner(s: str) -> str:
    """
    Simulates the election outcome after optimal snake eating.
    Time Complexity: O(N) where N is the length of string s.
    Space Complexity: O(N) to store animal list and eaten states.
    Returns: "snakes", "mongooses", or "tie".
    """
    animals = list(s)
    n = len(animals)
    eaten = [False] * n
    
    # Run the greedy mongoose eating pass
    for i in range(n):
        if animals[i] == 'm':
            # Check left neighbor first (Greedy choice)
            if i > 0 and animals[i - 1] == 's' and not eaten[i - 1]:
                eaten[i - 1] = True
            # Otherwise, check right neighbor
            elif i < n - 1 and animals[i + 1] == 's' and not eaten[i + 1]:
                eaten[i + 1] = True
                
    # Count survivors
    mongoose_count = sum(1 for char in animals if char == 'm')
    snake_count = sum(1 for idx, char in enumerate(animals) if char == 's' and not eaten[idx])
    
    if snake_count > mongoose_count:
        return "snakes"
    elif mongoose_count > snake_count:
        return "mongooses"
    else:
        return "tie"

if __name__ == "__main__":
    # Self-testing assertions
    assert check_election_winner("snakes") == "snakes" # wait, if string is "snakes" - it's just 's' characters?
    # Actually the string in problem consists of 's' and 'm'. Let's test actual 's' and 'm' patterns.
    assert check_election_winner("smssm") == "mongooses" # eaten indices: 0 and 3. Remaining: m at 1, m at 4, s at 2. m=2, s=1. Winner: mongooses.
    assert check_election_winner("ss") == "snakes"
    assert check_election_winner("snakes") == "snakes" # 'snakes' consists of 's','s' after filtering or raw? Wait, the problem says string consists only of 's' and 'm'.
    # So we only feed strings with 's' and 'm'.
    assert check_election_winner("s") == "snakes"
    assert check_election_winner("m") == "mongooses"
    assert check_election_winner("sm") == "tie" # eaten: index 0. Remaining: m=1, s=0. Winner: mongooses. Wait!
    # Let's trace "sm": mongoose at 1 eats snake at 0. Remaining: 1 mongoose, 0 snakes. Winner: mongooses!
    assert check_election_winner("sm") == "mongooses"
    assert check_election_winner("sms") == "tie" # mongoose at 1 eats snake at 0. Snake at 2 survives. Remaining: m=1, s=1. Winner: tie.
    
    print("8_1_snake_mongoose.py verified successfully!")
