# stats.py

def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    """
    Count every character (including spaces/punctuation) in lowercase.
    Returns a dict: {char: count, ...}
    """
    counts = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def sort_on(item):
    """Helper for .sort(): return the 'num' key for comparison."""
    return item["num"]


def sort_characters(char_dict):
    """
    Turn {char: count} into a list of dicts like
    [{'char': 'a', 'num': 123}, ...] and sort by 'num' desc.
    """
    items = [{"char": c, "num": n} for c, n in char_dict.items()]
    items.sort(key=sort_on, reverse=True)
    return items
