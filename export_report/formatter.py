from abc import ABC


class Formatter(ABC):
    """Class for create format of objects in report sheet."""

    # TODO: Do after MVP
    @property
    def bold_text(self):
        return {"text": "bold"}

    @property
    def italic_text(self):
        return {"text": "italic"}

    @property
    def font_size(self):
        return {"text": "italic"}
