from typing import Union

from pydantic import BaseModel


class CarSpecification(BaseModel):
    id: Union[int, None]
    make: Union[str, None]
    model: Union[str, None]
    body_style: Union[str, None]
    production_years: Union[str, None]
    horse_power: Union[int, None]
    weight_kg: Union[int, None]
    engine: Union[str, None]
    engine_size: Union[str, None]
