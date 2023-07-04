#!/usr/bin/python3
"""Solves the lock boxes puzzle """

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n  # Initially, all boxes are locked
    unlocked[0] = True  # The first box is unlocked
    keys = boxes[0]  # Start with the keys from the first box

    """Iterate through the keys and unlock the corresponding boxes"""
    while keys:
        key = keys.pop(0)
        if key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    """Check if all boxes are unlocked"""
    return all(unlocked)
