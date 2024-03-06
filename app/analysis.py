from typing import List
from .models import DeviceStatistics
from sqlalchemy.orm import Session

def get_statistics(session: Session, device_id: int) -> List[float]:
    query = session.query(DeviceStatistics)
    query = query.filter(DeviceStatistics.device_id == device_id)
    return query.all()

def calculate_statistics(values: List[float]) -> dict:
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

