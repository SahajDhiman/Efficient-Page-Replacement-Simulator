# module1_input.py
# Member 1: Input handling

def get_user_input():
    """
    Takes input from the user:
    - reference string (space-separated integers)
    - number of frames
    - algorithm choice

    Returns:
        pages (list[int]), frames (int), algo (str)
    """
    print("🔹 Efficient Page Replacement Simulator 🔹")

    while True:
        try:
            raw = input("Enter reference string (space-separated integers): ").strip()
            pages = list(map(int, raw.split()))
            if not pages:
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Example: 7 0 1 2 0 3 0 4")

    while True:
        try:
            frames = int(input("Enter number of frames: "))
            if frames <= 0:
                raise ValueError
            break
        except ValueError:
            print("Frames must be a positive integer.")

    print("\nChoose Algorithm:")
    print("1. FIFO")
    print("2. LRU")
    print("3. OPTIMAL")

    while True:
        try:
            choice = int(input("Enter choice (1/2/3): "))
            if choice not in (1, 2, 3):
                raise ValueError
            break
        except ValueError:
            print("Please enter 1, 2, or 3.")

    algo_map = {1: "FIFO", 2: "LRU", 3: "OPTIMAL"}
    algo = algo_map[choice]

    return pages, frames, algo
