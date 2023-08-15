from export_report.builder import ListReportBuilder
from export_report.sheet import ReportSheet
from export_report.sheet_component import DataComponent, HeaderComponent, HeaderItem

report = ListReportBuilder(filename="test", extension="xlsx")
sheet_1 = ReportSheet(sheet_name="Первый")

composit_header = HeaderComponent(
    header=[
        [
            HeaderItem(header_name="first", header_preview_name="first", merge_range=((0, 0), (0, 3))),
        ],
        [
            HeaderItem(header_name="second", header_preview_name="second", merge_range=((1,0), (1,2))),
            [
                HeaderItem(header_name="third", header_preview_name="third", merge_range=((1,),())),
            ],
            [
                HeaderItem(header_name="fourth", header_preview_name="fourth"),
                HeaderItem(header_name="fourth", header_preview_name="fourth"),
            ],
        ],
    ]
)
data = DataComponent(
    data=[
        ["1", "yellow"],
        ["2", "blue"],
        ["3", "black"],
        ["4", "red"],
        ["5", "grey"],
    ],
)
sheet_1.add_component(data)
report.add_sheet(sheet_1)
report.write_to_excel()
