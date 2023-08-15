from abc import ABC, abstractmethod
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, Optional, TypeAlias, TypeVar

from pandas import DataFrame


class SheetComponent(ABC):
    """Abstract component for create components in sheet of report."""

    def __init__(self, data: Any) -> None:
        pass

    @abstractmethod
    def export_into_dataframe(self) -> DataFrame:
        ...


ColumsCoordinates: TypeAlias = tuple[int, int]
MergeRange: TypeAlias = tuple[ColumsCoordinates, ColumsCoordinates]


@dataclass
class HeaderItem:
    """:param header_preview_name: The name of header, which will be used in file view.
    :param header_name: The name of header, which use in collection (data)

    Example:
    -------
        {"new_title": "The best swimming pool in Russia."}
        In this collection - key of dict is a header_name, which use in code, but header_preview_name may be similar,
        or another of this.
    :param merge_range: This optional value define mergered cells and range of this range.
    """

    header_preview_name: str
    header_name: str
    merge_range: Optional[MergeRange] = None


T = TypeVar("T", bound="HeaderRow")
HeaderRow: TypeAlias = Sequence[HeaderItem | T]
HeaderList: TypeAlias = Sequence[HeaderRow]


class HeaderComponent(SheetComponent):
    """Component for header."""

    _header: HeaderList

    def __init__(self, *, header: HeaderList) -> None:
        self._header = header

    def export_into_dataframe(self) -> DataFrame:
        return DataFrame([header.header_preview_name for header in self._header]).T


class CompositHeaderComponent(SheetComponent):
    """Composit component for header."""

    _header: HeaderList

    def __init__(self, *, header: HeaderList) -> None:
        self._header = header

    def export_into_dataframe(self) -> DataFrame:
        return DataFrame([header.header_preview_name for header in self._header]).T


DataItem: TypeAlias = Sequence[str | int]
DataList: TypeAlias = Sequence[DataItem]


class DataComponent(SheetComponent):
    """Component for main data."""

    _data: DataList

    def __init__(self, *, data: DataList) -> None:
        self._data = data

    def export_into_dataframe(self) -> DataFrame:
        return DataFrame([data_item for data_item in self._data])


