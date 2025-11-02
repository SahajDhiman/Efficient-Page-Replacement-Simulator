# Test update - checking GitHub link
def fifo(pages, frames):
    frame = []
    page_faults = 0
    steps = []
    for page in pages:
        if page not in frame:
            if len(frame) < frames:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_faults += 1
        steps.append(frame.copy())
    hits = len(pages) - page_faults
    return hits, page_faults, steps


def lru(pages, frames):
    frame = []
    page_faults = 0
    steps = []
    for i, page in enumerate(pages):
        if page not in frame:
            if len(frame) < frames:
                frame.append(page)
            else:
                used = {p: i - max(j for j in range(i) if pages[j] == p) if p in pages[:i] else i+1 for p in frame}
                victim = max(used, key=used.get)
                frame.remove(victim)
                frame.append(page)
            page_faults += 1
        steps.append(frame.copy())
    hits = len(pages) - page_faults
    return hits, page_faults, steps


def optimal(pages, frames):
    frame = []
    page_faults = 0
    steps = []
    for i in range(len(pages)):
        page = pages[i]
        if page not in frame:
            if len(frame) < frames:
                frame.append(page)
            else:
                next_use = {f: (pages[i+1:].index(f) if f in pages[i+1:] else float('inf')) for f in frame}
                victim = max(next_use, key=next_use.get)
                frame.remove(victim)
                frame.append(page)
            page_faults += 1
        steps.append(frame.copy())
    hits = len(pages) - page_faults
    return hits, page_faults, steps