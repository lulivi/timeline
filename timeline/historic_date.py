"""Historic date object."""

from typing import List, TextIO
import io


class HistoricDate(object):
    """Contains a date with events."""

    def __init__(self, year: int = 0, events: List[str] = []) -> None:
        """Class constructor."""
        super(HistoricDate, self).__init__()
        if isinstance(year, int):
            self.__year = year
        else:
            raise TypeError('year must be an integer')
        if isinstance(events, list):
            self.__events = events
        else:
            raise TypeError('events must be a list')

    def __repr__(self) -> str:
        """Set class representation."""
        return f'HistoricDate({self.__year}, {self.__events})'

    def __str__(self) -> str:
        """Printable representation."""
        return f'{self.__year}\n' + '\n'.join(f'*) {e}' for e in self.__events)

    @property
    def year(self) -> int:
        """Year property getter."""
        return self.__year

    @year.setter
    def year(self, year_value: int) -> None:
        """Year property setter."""
        if isinstance(year_value, int):
            self.__year = year_value
        else:
            raise TypeError('Year must be a number')

    @property
    def events(self) -> List[str]:
        """Events property getter."""
        return self.__events

    @events.setter
    def events(self, event_list: List[str]) -> None:
        """Events property setter."""
        if isinstance(event_list, list):
            self.__events = event_list
        else:
            raise TypeError('Events must be a list of strings')

    def events_amount(self) -> int:
        """Return the amount of events in the current historic date."""
        return len(self.events)

    def add_event(self, new_event: str) -> None:
        """Add a new event to the current historic date."""
        if isinstance(new_event, str):
            if new_event not in self.__events:
                self.__events.append(new_event)
        else:
            raise TypeError('The new event must be a string')

    def search_event(self, query: str) -> str:
        """Check if there is any event that contains the query string."""
        if isinstance(query, str):
            for e in self.__events:
                if query in e:
                    return e
        else:
            raise TypeError('The event query must be a string')

    def delete_event(self, query: str) -> None:
        """Delete the event containning the query string."""
        if isinstance(query, str):
            for e in self.__events:
                if query in e:
                    self.__events.remove(e)
        else:
            raise TypeError('The event query must be a '
                            'string: '.format(str(query)))

    def read_historic_date(self, file_descriptor: TextIO) -> None:
        """Read historic date from an input descriptor."""
        if isinstance(file_descriptor, io.TextIOWrapper):
            hd_line = file_descriptor.readline()[:-1]
            hd_splitted = hd_line.split('#')
            if hd_splitted[0].isnumeric():
                self.__year = int(hd_splitted[0])
            else:
                raise TypeError('The year string is not '
                                'numeric: '.format(hd_splitted[0]))
            self.__events = hd_splitted[1:]
        else:
            raise TypeError('The argument must be a file descriptor')
