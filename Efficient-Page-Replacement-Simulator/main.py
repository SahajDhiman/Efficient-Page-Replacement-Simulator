# Test update - checking GitHub link
from module1_input import get_user_input
from module2_algorithms import fifo, lru, optimal
from module3_visualization import show_visualization

if __name__ == "__main__":
    pages, frames, algo = get_user_input()

    if algo == "FIFO":
        hits, faults, steps = fifo(pages, frames)
    elif algo == "LRU":
        hits, faults, steps = lru(pages, frames)
    else:
        hits, faults, steps = optimal(pages, frames)

    show_visualization(pages, steps, hits, faults)