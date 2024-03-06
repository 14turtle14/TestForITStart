from sqlalchemy.orm import Session

from app.models import Device, DeviceStatistics


def get_aggregated_analysis(session: Session, user_id: int) -> dict:
    devices = session.query(Device).filter(Device.user_id == user_id).all()

    aggregated_statistics = {
        "min": float('inf'),
        "max": float('-inf'),
        "sum": 0,
        "count": 0,
        "median": None
    }

    for device in devices:
        device_statistics = session.query(DeviceStatistics).filter(DeviceStatistics.device_id == device.id).all()
        values = [statistic.value for statistic in device_statistics]

        aggregated_statistics["min"] = min(aggregated_statistics["min"], min(values))
        aggregated_statistics["max"] = max(aggregated_statistics["max"], max(values))
        aggregated_statistics["sum"] += sum(values)
        aggregated_statistics["count"] += len(values)

    if aggregated_statistics["count"] > 0:
        sorted_values = sorted(values)
        count = aggregated_statistics["count"]
        if count % 2 == 0:
            aggregated_statistics["median"] = (sorted_values[count // 2 - 1] + sorted_values[count // 2]) / 2
        else:
            aggregated_statistics["median"] = sorted_values[count // 2]

    return aggregated_statistics


def get_device_analysis(session: Session, user_id: int, device_id: int) -> dict:
    device_statistics = session.query(DeviceStatistics).filter(DeviceStatistics.device_id == device_id).all()
    values = [statistic.value for statistic in device_statistics]

    device_analysis = {
        "min": min(values),
        "max": max(values),
        "sum": sum(values),
        "count": len(values),
        "median": None
    }

    if device_analysis["count"] > 0:
        sorted_values = sorted(values)
        count = device_analysis["count"]
        if count % 2 == 0:
            device_analysis["median"] = (sorted_values[count // 2 - 1] + sorted_values[count // 2]) / 2
        else:
            device_analysis["median"] = sorted_values[count // 2]

    return device_analysis
