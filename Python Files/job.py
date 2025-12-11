class Job:

    def __init__(self, name, category, rate, date, hours):
        self._name = name
        self._category = category
        self._rate = rate
        self._date = date
        self._hours = hours

    def get_name(self):
        return self._name

    def get_category(self):
        return self._category

    def get_rate(self):
        return self._rate

    def get_date(self):
        return self._date

    def get_hours(self):
        return self._hours

    def __eq__(self, other):
        if (self._name == other.get_name() and
            self._category == other.get_category() and
            self._rate == other.get_rate() and
            self._date == other.get_date() and
            self._hours == other.get_hours()):
            return True
        else:
            return False

    def __hash__(self):
        attributes = (self._name, self._category, self._rate, self._date, self._hours)
        return hash(attributes)

    def __str__(self):
        return f'Job("{self._name}", "{self._category}", {self._rate}, "{self._date}", {self._hours})'

    def __repr__(self):
        return self.__str__()
