from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    max=0
    topper_name=""
    for name, score in scores:
        if score > max:
            max=score
            topper_name=name
    return topper_name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
