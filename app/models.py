from pydantic import BaseModel


class Metric(BaseModel):
    """A metric."""

    label: str
    value: str

    def __str__(self) -> str:
        return f"{self.value.rjust(7)}  {self.label}"
