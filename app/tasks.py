from celery import shared_task
from typing import List

@shared_task
def async_calculate_statistics(values: List[float]) -> dict:
    sorted_values = sorted(values)
    count = len(sorted_values)

    if count % 2 == 0:
        median = (sorted_values[count // 2 - 1] + sorted_values[count // 2]) / 2
    else:
        median = sorted_values[count // 2]

    return {
        "min": min(values),
        "max": max(values),
        "sum": sum(values),
        "count": len(values),
        "median": median
    }
