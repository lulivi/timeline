"""Timeline object."""

from typing import List, TextIO
from .historic_date import HistoricDate


class Timeline(object):
    """Contains a list of HistoricDate's."""

    def __init__(self, historic_dates: List[HistoricDate] = []) -> None:
        """Class constructor."""
        super(Timeline, self).__init__()

    def __repr__(self) -> str:
        """Set class representation."""
        pass

    def __str__(self) -> str:
        """Printable representation."""
        pass

    @property
    def historic_dates(self) -> List[HistoricDate]:
        """Historic Dates property getter."""
        pass

    @historic_dates.setter
    def historic_dates(self, historic_date_list: List[str]) -> None:
        """Historic Dates property setter."""
        pass

    def historic_dates_amount(self) -> int:
        """Return the amount of historic dates in the current timeline."""
        pass
    def events_amount(self, year: int) -> int:
        """Return the amount of events in the queried year."""
        pass

    def add_historic_date(self, new_historic_date: HistoricDate) -> None:
        """Add a new historic date to the current timeline."""
        pass

    def add_event(self, year: int, new_event: str) -> None:
        """Add new event to an existent historic date."""
        pass

    def search_historic_date(self, year: int) -> HistoricDate:
        """Check if there is any event that contains the query string."""
        pass

    def search_event(self, year: int, query: str) -> str:
        """Return the historic date in which the event happened."""
        pass

    def delete_historic_date(self, year: int) -> None:
        """Delete one historic date by it year."""
        pass

    def delete_event(self, year: int, query: str) -> None:
        """Delete an event from an historic date by it year and substring."""
        pass

    def read_timeline(self, file_descriptor: TextIO) -> None:
        """Read timeline from an input descriptor."""
        pass
