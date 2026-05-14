from __future__ import annotations

def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2) and x1!=x2, or None if injective."""
    # === TODO ===
    # Your code here
    # This is a concept of using the data provided by the professor to find the non-injective pair. 
    seen_values = {}

    for key, value in mapping.items():
        if value in seen_values:
            return (seen_values[value], key)
        seen_values[value] = key

    return None
    pass
    # === END TODO ===

def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element with no input mapping to it, or None if surjective."""
    # === TODO ===
    # Your code here
    # This code is ment to find the non surjectivie element by using the data provided by the professor.
    used_values = set(mapping.values())

    for elem in target:
        if elem not in used_values:
            return elem
        
        return None
    pass
    # === END TODO ===

def my_floor(x: float) -> int:
    """Return floor(x) without using math.floor."""
    # === TODO ===
    # Your code here
    # This code is ment to find the floor of a number which are given randomly by the professor.
    
    i = int(x)

    if x<0 and x != i // 1:
        i -= 1
    
    return i
    
    pass
    # === END TODO ===


def my_ceil(x: float) -> int:
    """Return ceil(x) without using math.ceil."""
    # === TODO ===
    # Your code here
    # This code is suppose to use the ceilling function to find the ceilling of a number which are given randomly by the professor.
    i = int(x)
    if x>0 and x != i:
        i += 1
    return i

    pass
    # === END TODO ===
