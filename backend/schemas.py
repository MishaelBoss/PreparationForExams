from typing import Literal
from pydantic import BaseModel
from datetime import datetime


CategoryType = Literal['Обновление', 'Событие', 'Техническое', 'Анонс', 'Конкурс']


class User(BaseModel):
    id: int | None = None
    usename: str
    password: str
    created_at: datetime | None = None