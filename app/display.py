from typing import List

from .models import Metric


def clean(metrics: List[Metric]) -> List[Metric]:
    """Post-process tile labels."""
    for i in metrics:
        i.label = (
            i.label.lower()
            .replace("number of", "")
            .replace("in ohio", "")
            .replace("expanded case definition (probable)", "expanded cases")
            .replace("expanded death definition (probable)", "expanded deaths")
            .title()
            .replace("Cdc", "CDC")
            .replace("Icu", "ICU")
            .strip()
        )
        i.value = i.value.replace("*", "").replace("-", "–")
    return metrics


def display(metrics: List[Metric]) -> None:
    """Output metrics tiles to console."""
    # todo: update these?
    divider_indices = (2, 3, 6, 7, 9)
    for idx, i in enumerate(metrics):
        print(i, end=("\n\n" if idx in divider_indices else "\n"))
