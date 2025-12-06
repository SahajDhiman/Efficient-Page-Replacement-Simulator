# module3_visualization.py
# Member 2: Console visualization (and optional chart)

def show_visualization(pages, steps, hits, faults, algo_name):
    print("\n====================================")
    print(f"   {algo_name} Page Replacement")
    print("====================================")
    print("Step | Page | Frames")
    print("------------------------------------")

    for i, page in enumerate(pages):
        frame_state = ", ".join(str(x) for x in steps[i])
        print(f"{i+1:>4} | {page:>4} | [{frame_state}]")

    print("------------------------------------")
    print(f"Total Page Hits   : {hits}")
    print(f"Total Page Faults : {faults}")
    if len(pages) > 0:
        hit_ratio = hits / len(pages)
        print(f"Hit Ratio         : {hit_ratio:.2f}")
    print("====================================")


# OPTIONAL: extra marks – comparison chart
try:
    import matplotlib.pyplot as plt

    def show_fault_comparison(results):
        """
        results: dict like {"FIFO": faults_fifo, "LRU": faults_lru, "OPTIMAL": faults_opt}
        """
        algos = list(results.keys())
        faults = [results[a] for a in algos]

        plt.bar(algos, faults)
        plt.title("Page Fault Comparison")
        plt.xlabel("Algorithm")
        plt.ylabel("Number of Page Faults")
        plt.show()

except ImportError:
    # If matplotlib not installed, just ignore the chart feature
    def show_fault_comparison(results):
        print("\n(Matplotlib not installed – skipping chart.)")
