import random

def get_wrestlers():
    return ["Triple H", "The Undertaker", "Shawn Michaels", "The Rock", 
            "Stone Cold Steve Austin", "Hulk Hogan", "John Cena", "Randy Orton"]

def create_matches(wrestlers):
    random.shuffle(wrestlers)
    matches = []
    for i in range(0, len(wrestlers), 2):
        matches.append((wrestlers[i], wrestlers[i+1]))
    return matches

def print_card(matches):
    """Print the match card."""
    print("________________THE CARD________________")
    for i, match in enumerate(matches, 1):
        print(f"Match {i}: {match[0]} vs {match[1]}")
    print("________________________________________")

def main():
    wrestlers = get_wrestlers()
    
    if len(wrestlers) % 2 != 0:
        print("Error: Number of wrestlers must be even.")
        return

    try:
        matches = create_matches(wrestlers)
        print_card(matches)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
