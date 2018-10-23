"""Historic date object."""

from typing import List, TextIO


class HistoricDate(object):
    """Contains a date with events."""

    def __init__(self, year: int = 0, events: List[str] = []) -> None:
        """Class constructor."""
        super(HistoricDate, self).__init__()

    def __repr__(self) -> str:
        """Set class representation."""
        pass

    def __str__(self) -> str:
        """Printable representation."""
        pass

    @property
    def year(self) -> int:
        """Year property getter."""
        pass

    @year.setter
    def year(self, year_value: int) -> None:
        """Year property setter."""
        pass

    @property
    def events(self) -> List[str]:
        """Events property getter."""
        pass

    @events.setter
    def events(self, event_list: List[str]) -> None:
        """Events property setter."""
        pass

    def events_amount(self) -> int:
        """Return the amount of events in the current historic date."""
        pass

    def add_event(self, new_event: str) -> None:
        """Add a new event to the current historic date."""
        pass

    def search_event(self, query: str) -> str:
        """Check if there is any event that contains the query string."""
        pass

    def delete_event(self, query: str) -> None:
        """Delete the event containning the query string."""
        pass

    def read_historic_date(self, file_descriptor: TextIO) -> None:
        """Read historic date from an input descriptor."""
        pass
