from pandas import DataFrame

from export_report.sheet_component import SheetComponent


class ReportSheet:
    """Sheet class for use in report builder."""

    sheet_name: str
    components: list[DataFrame] = []

    def __init__(self, sheet_name: str) -> None:
        self.sheet_name = sheet_name

    def add_component(self, component: SheetComponent) -> None:
        self.components.append(component.export_into_dataframe())

