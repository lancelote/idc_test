from django.db import models
from django.core.validators import RegexValidator


class Patient(models.Model):
    family_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patronymic_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    MALE = 'М'
    FEMALE = 'Ж'
    SEX = (
        (MALE, 'мужской'),
        (FEMALE, 'женский'),
    )
    sex = models.CharField(max_length=1, choices=SEX)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Требуемый формат номера: '+999999999'"
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=15, default='+899999999'
    )

    def __str__(self):
        return '{0}, '.format(self.id) + ' '.join(
            (self.family_name, self.first_name, self.patronymic_name)
        )


class Document(models.Model):
    """
    Document of identification
    """
    patient = models.ForeignKey(Patient)
    PASSPORT = 'Паспорт'
    DOCUMENTS = (
        (PASSPORT, 'Паспорт'),
    )
    doc_name = models.CharField(
        choices=DOCUMENTS, default=PASSPORT, max_length=20
    )

    serial = models.IntegerField()
    number = models.IntegerField()
    date_of_issue = models.DateField()

    def __str__(self):
        return self.patient.__str__()


class Address(models.Model):
    """
    Basic address class
    """
    patient = models.ForeignKey(Patient)
    city = models.CharField(max_length=20, default='Тула')
    street = models.CharField(max_length=20)
    house = models.IntegerField()
    apartment = models.IntegerField()
    postal_code = models.IntegerField(default=300000)

    class Meta:
        abstract = True

    def __str__(self):
        return self.patient.__str__()


class RegAddress(Address):
    """
    Registered address
    """
    pass


class ActAddress(Address):
    """
    Actual address
    """
    pass
