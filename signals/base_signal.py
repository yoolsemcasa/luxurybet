from dataclasses import dataclass
from datetime import datetime


@dataclass
class Signal:

    title: str

    message: str

    level: str

    created_at: datetime = datetime.now()