class JobManager:

    def __init__(self, jobs=None):
        if jobs is None:
            self._jobs = []
        else:
            self._jobs = jobs

    def get_jobs(self):
        return self._jobs

    def __str__(self):
        return f"JobManager({self._jobs})"

    def __repr__(self):
        return self.__str__()

    def add_job(self, job):
        if job.get_rate() <= 0:
            print("Only positive values for rate allowed")
            return False
        if job.get_hours() <= 0:
            print("Only positive values for hours allowed")
            return False
        if job.get_hours() > 6:
            print("Cannot allocate more than 6 hours per job")
            return False

        total_hours_today = 0
        for existing_job in self._jobs:
            if (existing_job.get_name() == job.get_name() and
                existing_job.get_date() == job.get_date()):
                total_hours_today += existing_job.get_hours()

        if total_hours_today + job.get_hours() > 8:
            print("Cannot allocate more than 8 hours per worker per day")
            return False

        self._jobs.append(job)
        return None

    def remove_job(self, job):
        if job not in self._jobs:
            print("Job does not exist")
            return False
        self._jobs.remove(job)
        return None

    def edit_job(self, old_job, new_job):
        if old_job not in self._jobs:
            print("Job does not exist")
            return False

        if new_job.get_rate() <= 0:
            print("Only positive values for rate allowed")
            return False
        if new_job.get_hours() <= 0:
            print("Only positive values for hours allowed")
            return False
        if new_job.get_hours() > 6:
            print("Cannot allocate more than 6 hours per job")
            return False

        total_hours_today = 0
        for existing_job in self._jobs:
            if existing_job == old_job:
                continue

            if (existing_job.get_name() == new_job.get_name() and
                existing_job.get_date() == new_job.get_date()):
                total_hours_today += existing_job.get_hours()

        if total_hours_today + new_job.get_hours() > 8:
            print("Cannot allocate more than 8 hours per worker per day")
            return False

        self._jobs.remove(old_job)
        self._jobs.append(new_job)
        return None

    def search_by_category(self, category):
        matches = []
        for job in self._jobs:
            if job.get_category() == category:
                matches.append(job)
        return matches

    def search_by_rate(self, rate):
        matches = []
        for job in self._jobs:
            if job.get_rate() == rate:
                matches.append(job)
        return matches

    def search_by_name_and_date(self, name, date):
        matches = []
        for job in self._jobs:
            if job.get_name() == name and job.get_date() == date:
                matches.append(job)
        return matches

    def get_total_cost_per_name(self, names):
        result = {}

        for job in self._jobs:
            name = job.get_name()
            if name in names:
                cost = job.get_rate() * job.get_hours()
                result[name] += cost
        return result

    def get_category_count_per_name(self):
        result = {}

        for job in self._jobs:
            name = job.get_name()
            category = job.get_category()
            result[name][category] += 1

            if name not in result:
                result[name] = {}
            if category not in result[name]:
                result[name][category] = 0

            return result
        return None

    def load_from_file(self, file_name):
        import csv
        from job import Job

        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)

            for name, category, rate, date, hours in reader:
                job = Job(name, category, float(rate), date, int(hours))
                self.add_job(job)

    def save_to_file(self, file_name):
        import csv

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            for job in self._jobs:
                writer.writerow([
                    job.get_name(),
                    job.get_category(),
                    job.get_rate(),
                    job.get_date(),
                    job.get_hours()
                ])
