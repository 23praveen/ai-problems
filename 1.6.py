def vacuum_cleaner(environment):
    """Simulates a vacuum cleaner agent cleaning an environment."""
    location = "A"  # Initial location
    while True:
        if environment[location] == "Dirty":
            print(f"Cleaning {location}...")
            environment[location] = "Clean"
        else:
            print(f"{location} is already clean.")

        # Move to the other location
        location = "B" if location == "A" else "A"

        # Check if both locations are clean
        if environment["A"] == "Clean" and environment["B"] == "Clean":
            print("Environment is clean. Exiting.")
            break

# Example usage:
environment = {"A": "Dirty", "B": "Dirty"}  # Initial environment state
vacuum_cleaner(environment)