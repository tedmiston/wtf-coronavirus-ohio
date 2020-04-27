from app import Metric, clean


def test_clean() -> None:
    actual = clean(
        metrics=[
            Metric(label="Confirmed Cases in Ohio", value="4,043"),
            Metric(label="Number of ICU admissions", value="346"),
            Metric(label="Number of Hospitalizations in Ohio", value="1,104"),
            Metric(label="Number of Deaths", value="119"),
            Metric(label="Age Range", value="<1–101"),
            Metric(label="Median Age", value="53"),
            Metric(label="Sex - Males", value="48%*"),
            Metric(label="Sex - Females", value="51%*"),
        ]
    )

    expected = [
        Metric(label="Confirmed Cases", value="4,043"),
        Metric(label="ICU Admissions", value="346"),
        Metric(label="Hospitalizations", value="1,104"),
        Metric(label="Deaths", value="119"),
        Metric(label="Age Range", value="<1–101"),
        Metric(label="Median Age", value="53"),
        Metric(label="Sex - Males", value="48%*"),
        Metric(label="Sex - Females", value="51%*"),
    ]

    assert expected == actual
