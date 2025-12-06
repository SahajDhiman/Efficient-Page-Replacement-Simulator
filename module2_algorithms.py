# module2_algorithms.py
# Member 1: FIFO, LRU, OPTIMAL algorithms

from math import inf


def fifo(pages, frames):
    frame = []
    faults = 0
    steps = []

    for page in pages:
        if page not in frame:
            if len(frame) < frames:
                frame.append(page)
            else:
                # remove oldest page (front of list)
                frame.pop(0)
                frame.append(page)
            faults += 1
        steps.append(frame.copy())

    hits = len(pages) - faults
    return hits, faults, steps


def lru(pages, frames):
    frame = []
    last_used = {}
    faults = 0
    steps = []

    for i, page in enumerate(pages):
        if page in frame:
            # hit
            last_used[page] = i
        else:
            # fault
            if len(frame) < frames:
                frame.append(page)
            else:
                # find least recently used page in frame
                victim = min(frame, key=lambda p: last_used.get(p, -1))
                frame[frame.index(victim)] = page
            faults += 1
            last_used[page] = i

        steps.append(frame.copy())

    hits = len(pages) - faults
    return hits, faults, steps


def optimal(pages, frames):
    frame = []
    faults = 0
    steps = []

    n = len(pages)

    for i, page in enumerate(pages):
        if page in frame:
            # hit
            steps.append(frame.copy())
            continue

        # page fault
        if len(frame) < frames:
            frame.append(page)
        else:
            # look ahead to choose victim
            next_use = {}
            for f in frame:
                if f in pages[i+1:]:
                    next_use[f] = pages[i+1:].index(f)
                else:
                    next_use[f] = inf

            victim = max(next_use, key=next_use.get)
            frame[frame.index(victim)] = page

        faults += 1
        steps.append(frame.copy())

    hits = n - faults
    return hits, faults, steps
