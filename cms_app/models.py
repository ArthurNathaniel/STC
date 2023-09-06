from django.db import models
from django.db import models
from PIL import Image


class ChurchMember(models.Model):
    profile_image = models.ImageField(
        upload_to='profile_images/', default='N/A')
    surname = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    digital_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    emergency_contact_number = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )
    gender = models.CharField(max_length=20, choices=GENDER,)
    nationality = models.CharField(max_length=100)
    martial_status = models.CharField(max_length=100, choices=[('Single', 'Single'), (
        'Married', 'Married'),  ('Widowed', 'Widowed')])
    if_married = models.CharField(max_length=100, choices=[('Nothing', 'Nothing'), 
    ('Holy Matrimony', 'Holy Matrimony'), ('Traditional Marriage', 'Traditional Marriage')])
    spouse_name = models.CharField(max_length=100)
    number_of_children = models.IntegerField()
    children_names = models.CharField(max_length=500)
    mother_name = models.CharField(max_length=100)
    is_mother_alive = models.CharField(
        max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    mother_religious_denomination = models.CharField(
        max_length=100, choices=[('Catholics', 'Catholic'), ('Other', 'Other')])
    father_name = models.CharField(max_length=100)
    is_father_alive = models.CharField(
        max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    father_religious_denomination = models.CharField(
        max_length=100, choices=[('Catholics', 'Catholic'), ('Other', 'Other')])
    place_of_employment = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    baptized = models.CharField(max_length=3, choices=[
                                ('Yes', 'Yes'), ('No', 'No')])
    baptized_place = models.CharField(max_length=100)
    confirmed = models.CharField(max_length=3, choices=[
                                 ('Yes', 'Yes'), ('No', 'No')])
    confirmation_place = models.CharField(max_length=100)
    number_of_society = models.IntegerField()
    society = models.CharField(max_length=700)
    # society = models.CharField(max_length=100, choices=[
    #     ('Sacred Heart of Confraternity', 'Sacred Heart of Confraternity'),
    #     ('Youth Choir', 'Youth Choir'),
    #     ('Legion of Mary', 'Legion of Mary'),
    #     ('Charismatic', 'Charismatic'),
    #     ('St Theresa Society', 'St Theresa Society'),
    #     ('Cosra', 'Cosra'),
    #     ('Children of Mary', 'Children of Mary'),
    #     ('Knight of Marshall', 'Knight of Marshall'),
    #     ('Young Mens', 'Young Mens'),
    #     ('Mary Mother of Mothers', 'Mary Mother of Mothers'),
    #     ('Theresa Mma Kuo', 'Theresa Mma Kuo'),
    #     ('Mens Society', 'Mens Society'),
    #     ('Senior Choir', 'Senior Choir'),
    #     ('Lay Readers', 'Lay Readers'),
    #     ('Ushers', 'Ushers'),
    #     ('St Anthony Guild', 'St Anthony Guild'),
    #     ('Northern Union', 'Northern Union'),
    #     ('CYO', 'CYO'),
    #     ('St Theresa Guild', 'St Theresa Guild'),
    #     ('KLBS', 'KLBS'),
    #     ('Knight and Ladies of St John', 'Knight and Ladies of St John')

    #        ])
    

    def __str__(self):
        return self.first_name


class Payment(models.Model):
    name = models.CharField(max_length=100)
    # date = models.DateTimeField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    PAYMENT_TYPE = (
        ('Welfare', 'Welfare'),
        ('Church', 'Church'),
        ('Harvest', 'Harvest'),
    )
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE,)

    def __str__(self):
        return self.name

class Document(models.Model):
    document_name = models.CharField(max_length=255)
    document_image = models.ImageField(upload_to="document_image")

    def __str__(self):
        return self.document_name
