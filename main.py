# main.py
# Member 2: Final integration using Member 1 modules + visualization

from module1_input import get_user_input
from module2_algorithms import fifo, lru, optimal
from module3_visualization import show_visualization, show_fault_comparison


def run_single_algorithm(pages, frames, algo):
    if algo == "FIFO":
        hits, faults, steps = fifo(pages, frames)
    elif algo == "LRU":
        hits, faults, steps = lru(pages, frames)
    else:  # OPTIMAL
        hits, faults, steps = optimal(pages, frames)

    show_visualization(pages, steps, hits, faults, algo)
    return hits, faults


def run_all_algorithms(pages, frames):
    # For comparison chart – runs all three
    results = {}

    for algo_name, func in (("FIFO", fifo), ("LRU", lru), ("OPTIMAL", optimal)):
        hits, faults, steps = func(pages, frames)
        results[algo_name] = faults

    show_fault_comparison(results)


if __name__ == "__main__":
    pages, frames, algo = get_user_input()

    # Run chosen algorithm
    run_single_algorithm(pages, frames, algo)

    # Uncomment this line if you also want the comparison chart at the end:
    # run_all_algorithms(pages, frames)
