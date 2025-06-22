from typing import Any

from .cache import get_data_with_cache
from .logger import log


def get_UserStats() -> None:
    data = get_data_with_cache(
        endpoint_name="user_data", url="https://habitica.com/api/v3/user"
    )

    stats: Any = data["stats"]

    current_stats: dict[str, Any | int] = {
        "class": stats["class"],
        "lvl": stats["lvl"],
        "hp": stats["hp"],
        "exp": stats["exp"],
        "mp": stats["mp"],
    }

    for i, j in enumerate(current_stats, start=1):
        log.info(f"{i}. {j} = {stats[j]}")
