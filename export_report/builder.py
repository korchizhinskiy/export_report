from abc import ABC

import pandas

from export_report.sheet import ReportSheet


class ReportBuilder(ABC):
    """
    Interface of builder class for create analytics reports with configured parameters.
    """

    filename: str
    extension: str = "xlsx"
    sheets: list[ReportSheet] = []

    def __init__(self, filename: str, extension: str = "xlsx") -> None:
        self.extension = extension

    def add_sheet(self, sheet: ReportSheet) -> None:
        self.sheets.append(sheet)


class ListReportBuilder(ReportBuilder):
    """
    Abstrсе builder class for create analytics reports with configured parameters.
    """

    filename: str
    extension: str = "xlsx"
    sheets: list[ReportSheet] = []

    def __init__(self, filename: str, extension: str = "xlsx") -> None:
        self.extension = extension

    def add_sheet(self, sheet: ReportSheet) -> None:
        self.sheets.append(sheet)

    def write_to_excel(self):
        with pandas.ExcelWriter(  # type: ignore
            "da.xlsx", engine="xlsxwriter", datetime_format="mmm ss", date_format="mmmm dd yyyy"
        ) as writer:
            for sheet in self.sheets:
                main_dataframe = pandas.concat(sheet.components, ignore_index=True, axis=0)
                main_dataframe.to_excel(writer, index=False, header=False)
