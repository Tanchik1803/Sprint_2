class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

        if self.hours is None and self.rest_days is not None:
            self.hours = self.get_hours(self.rest_days)

        if self.email is None:
            self.email = self.get_email(self.name)

    @classmethod
    def get_hours(cls, rest_days):
        return (7 - rest_days) * 8

    @classmethod
    def get_email(cls, name):
        return f"{name}@email.com"

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
          return self.hours * self.hourly_payment