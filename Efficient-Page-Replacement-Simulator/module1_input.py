# Test update - checking GitHub link
def get_user_input():
    print("🔹 Efficient Page Replacement Simulator 🔹")
    pages = list(map(int, input("Enter reference string (space-separated): ").split()))
    frames = int(input("Enter number of frames: "))
    print("Choose Algorithm:")
    print("1. FIFO\n2. LRU\n3. OPTIMAL")
    choice = int(input("Enter choice (1/2/3): "))
    algo = {1: "FIFO", 2: "LRU", 3: "OPTIMAL"}[choice]
    return pages, frames, algo