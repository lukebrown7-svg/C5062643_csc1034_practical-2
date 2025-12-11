class Job:

    def __init__(self, name, category, rate, date, hours):
        self._name = name
        self._category = category
        self._rate = rate
        self._date = date
        self._hours = hours

    def get_name(self):
        return self._name
        pass

    def get_category(self):
        return self._category
        pass

    def get_rate(self):
        return self._rate
        pass

    def get_date(self):
        return self._date
        pass

    def get_hours(self):
        return self._hours
        pass

    def __eq__(self, other):
        pass

    def __hash__(self):
        pass

    def __str__(self):
        return f'Job("{self._name}", "{self._category}", {self._rate}, "{self._date}", {self._hours})'

    def __repr__(self):
        return self.__str__()
