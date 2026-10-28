from pydantic import BaseModel
from typing import Optional

class Libros(BaseModel):
    id: Optional[int] = None
    titulo: str
    autor: str
    genero: str