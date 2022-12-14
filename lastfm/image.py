from typing import Any, Dict, Optional

__all__ = ["Image"]


class Image:
    def __init__(self, data: Dict[Any, Any]) -> None:
        self._data = data

    @property
    def small(self) -> Optional[str]:
        try:
            return self._data[0]["#text"]
        except (KeyError, IndexError):
            return None

    @property
    def medium(self) -> Optional[str]:
        try:
            return self._data[1]["#text"]
        except (KeyError, IndexError):
            return None

    @property
    def large(self) -> Optional[str]:
        try:
            return self._data[2]["#text"]
        except (KeyError, IndexError):
            return None

    @property
    def extra_large(self) -> Optional[str]:
        try:
            return self._data[3]["#text"]
        except (KeyError, IndexError):
            return None

    @property
    def mega(self) -> Optional[str]:
        try:
            return self._data[4]["#text"]
        except (KeyError, IndexError):
            return None

    @property
    def extra_mega(self) -> Optional[str]:
        """Not sure what to call this as last.fm doesn't give a proper name it's just empty and is rarely used."""
        try:
            return self._data[5]["#text"]
        except (KeyError, IndexError):
            return None
