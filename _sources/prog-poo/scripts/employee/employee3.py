class Employee:
    """
    >>> Employee.org_domain
    'example.org'
    >>> a = Employee('A', 'BcD', 100)
    >>> b = Employee('F', 'G', '200')
    >>> b.pay
    200.0
    >>> a.email
    'a.bcd@example.org'
    >>> Employee.num_of_employees
    2
    >>> Employee.set_org_domain('edufr.ch')
    >>> Employee.org_domain
    'edufr.ch'
    >>> c = Employee('I', 'J', 300)
    >>> c.email
    'i.j@edufr.ch'

    >>> Employee.raise_amount
    1.04
    >>> a.apply_raise()
    >>> a.pay
    104.0

    >>> Employee.set_raise_amount(1.06)
    >>> Employee.raise_amount
    1.06
    >>> b.apply_raise()
    >>> b.pay
    212.0

    >>> e = Employee.from_string('A-B-100')
    >>> e.firstname
    'A'
    >>> e.lastname
    'B'
    >>> e.email
    'a.b@edufr.ch'
    >>> e.pay
    100.0

    >>> e2 = Employee.from_string('F-G-200')
    >>> Employee.num_of_employees
    5

    >>> import datetime
    >>> Employee.is_workday(datetime.date(2023, 11, 24))
    True
    >>> Employee.is_workday(datetime.date(2023, 11, 25))
    False
    >>> Employee.is_workday(datetime.date(2023, 11, 26))
    False
    >>> Employee.is_workday(datetime.date(2023, 11, 27))
    True

    >>> e.fullname()
    'A B'

    """

    raise_amount = 1.04
    num_of_employees = 0
    org_domain = "example.org"

    def __init__(self, firstname, lastname, pay=200_000):
        self.firstname = firstname
        self.lastname = lastname
        self.email = "{fname}.{lname}@{domain}".format(
            fname=self.transform_name(firstname),
            lname=self.transform_name(lastname),
            domain=self.org_domain
        )
        self.pay = float(pay)

        # incrémentation automatique du nombre d'employés
        Employee.num_of_employees += 1

    def apply_raise(self):
        self.pay *= Employee.raise_amount

    @staticmethod
    def transform_name(name: str) -> str:
        return name.lower().replace(" ", "")

    @classmethod
    def from_string(cls, emp_string, sep="-"):
        try:
            firstname, lastname, pay = emp_string.split(sep)
            return cls(firstname, lastname, pay)
        except Exception as e:
            raise ValueError(
                f"Invalid format: ({emp_string})"
            )

    @staticmethod
    def is_workday(day):
        return day.weekday() not in [5, 6]

    @classmethod
    def set_org_domain(cls, new_domain):
        cls.org_domain = new_domain

    @classmethod
    def set_raise_amount(cls, new_amount):
        cls.raise_amount = new_amount

    def fullname(self):
        return f"{self.firstname} {self.lastname}"


try:
    import doctest

    doctest.testmod()
except:
    print(
        "Utilisez le Python standard pour bénéficier des doctests"
    )
