from django.db import models

# Create your models here.


ACTOR = [
    ('DENUNCIANTE', 'Denunciante'),
    ('AGRESOR', 'Agresor'),
    ('VICTIMA', 'Victima'),
    ('ACUDIENTE', 'Acuediente')
]

DOCUMENT_TYPE = [
    ('NUIP', 'nuip'),
    ('T.I', 't.i.'),
    ('C.C', 'c.c.'),
    ('C.E.', 'c.e.'),
    ('SIN IDENTIFICACION', 'Sin identificación'),
    ('NIT', 'nit')
]

HEALTH = [
    ('NINGUNA', 'Ninguna'),
    ('CONTRIBUTIVO', 'Contributivo'),
    ('SUBSIDIADO', 'Subsidiado'),
    ('ESPECIAL', 'Especial')
]

MARITAL_STATUS = [
    ('SOLTERO', 'Soltero'),
    ('CASADO', 'Casado'),
    ('UNION LIBRE', 'Union libre'),
    ('UNION DE HECHO', 'Union de hecho'),
    ('SEPARADO', 'Separado'),
    ('DIVORCIADO', 'Divorciado'),
    ('VIUDO', 'Viudo'),
    ('NOVIAZGO', 'Noviazgo')
]

WORKDAY = [
    ('DIURNA', 'Diurna'),
    ('TARDE', 'Tarde'),
    ('NOCTURNA', 'Nocturna')
]

EDUCATION = {
    ('ANALFABETA', 'Analfabeta'),
    ('PREESCOLAR', 'Preescolar'),
    ('PRIMARIA', 'Primaria'),
    ('SECUNDARIA', 'Secundaria'),
    ('SUPERIOR', 'Superior'),
    ('POSTGRADO', 'Postgrado')
}

GENDER = [
    ('MASCULINO', 'Masculino'),
    ('FEMENINO', 'Femenino')
]


class Person(models.Model):
    name_1 = models.CharField(max_length=45)
    name_2 = models.CharField(max_length=45)
    lastname_1 = models.CharField(max_length=45)
    lastname_2 = models.CharField(max_length=45)
    email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name_1


class Department(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Municipality(models.Model):
    name = models.CharField(max_length=45)

    department = models.ForeignKey(
        'Department',
        related_name='municipalities',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Vereda(models.Model):
    name = models.CharField(max_length=45)

    municipality = models.OneToOneField(
        'Municipality',
        related_name='vereda',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Disability(models.Model):
    name = models.CharField(max_length=45)

    citizen = models.ForeignKey(
        'Citizen',
        related_name='disabilities',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'disabilities'

    def __str__(self):
        return self.name


class Ethnicity(models.Model):
    name = models.CharField(max_length=45)

    citizen = models.ForeignKey(
        'Citizen',
        related_name='ethnicities',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'ethnicities'

    def __str__(self):
        return self.name


class Telephone(models.Model):
    number = models.IntegerField()

    citizen = models.ForeignKey(
        'Citizen',
        related_name='telephones',
        on_delete=models.CASCADE
    )
    officer = models.ForeignKey(
        'Officer',
        related_name='telephones',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.number)


class Adjunt(models.Model):
    name = models.CharField(max_length=45)
    path = models.CharField(max_length=100)

    citizen = models.ForeignKey(
        'Citizen',
        related_name='adjunts',
        on_delete=models.CASCADE
    )
    work_orden = models.ForeignKey(
        'WorkOrden',
        related_name='adjunts',
        on_delete=models.CASCADE
    )
    fact = models.ForeignKey(
        'Fact',
        related_name='adjunts',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Relationship(models.Model):
    name = models.CharField(max_length=45)

    citizen = models.ForeignKey(
        'Citizen',
        related_name='relationships',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Transfer(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    # id entidad
    proceedings = models.CharField(max_length=45)
    reason = models.TextField()

    adjunts = models.ManyToManyField('Adjunt')
    municipality = models.OneToOneField(
        'Municipality',
        related_name='transfer',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.datetime.strftime("%d/%m/%Y, %H:%M:%S")


class Entity(models.Model):
    nit = models.IntegerField()
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    principal = models.CharField(max_length=45)
    url_web_site = models.CharField(max_length=45)
    slogan = models.CharField(max_length=45)
    slogan = models.CharField(max_length=45)
    url_icon = models.CharField(max_length=100)

    municipality = models.OneToOneField(
        'Municipality',
        related_name='entity',
        on_delete=models.CASCADE
    )
    telephone = models.ForeignKey(
        'Telephone',
        related_name='entities',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'entities'

    def __str__(self):
        return self.name


class WorkOrden(models.Model):
    # TODO: expediente
    datetime = models.DateTimeField(auto_now_add=True)
    study = models.CharField(max_length=45)

    officer = models.OneToOneField(
        'Officer',
        related_name='work_orden',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.datetime.strftime("%d/%m/%Y, %H:%M:%S")


class Fact(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    facts = models.TextField()
    pretension = models.CharField(max_length=45)

    complaints = models.ManyToManyField('Complaint')
    vereda = models.OneToOneField(
        'Vereda',
        related_name='fact',
        on_delete=models.CASCADE
    )
    municipality = models.OneToOneField(
        'Municipality',
        related_name='fact',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.datetime.strftime("%d/%m/%Y, %H:%M:%S")


class Officer(Person):
    profession = models.CharField(max_length=45)
    position = models.CharField(max_length=45)
    vereda = models.OneToOneField(
        'Vereda',
        related_name='officer',
        on_delete=models.CASCADE
    )
    municipality = models.OneToOneField(
        'Municipality',
        related_name='officer',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name_1


class Citizen(Person):
    actor = models.CharField(max_length=45, choices=ACTOR)
    document_type = models.CharField(max_length=45, choices=DOCUMENT_TYPE)
    identification = models.IntegerField()
    date_birth = models.DateField()
    health = models.CharField(max_length=45, choices=DOCUMENT_TYPE)
    eps = models.BooleanField(default=False)
    occupation = models.CharField(max_length=45)
    gender = models.CharField(max_length=45, choices=DOCUMENT_TYPE)
    marital_status = models.CharField(max_length=45, choices=MARITAL_STATUS)
    address = models.CharField(max_length=45, blank=True, null=True)
    institute = models.CharField(max_length=45, blank=True, null=True)
    workday = models.CharField(max_length=45, choices=WORKDAY)
    education = models.CharField(max_length=45, choices=EDUCATION)
    head_family = models.BooleanField(blank=True, null=True)
    pregnant = models.BooleanField(blank=True, null=True)

    department_expedition = models.OneToOneField(
        'Department',
        related_name='citizen',
        on_delete=models.CASCADE
    )
    municipality = models.OneToOneField(
        'Municipality',
        related_name='citizen',
        on_delete=models.CASCADE
    )
    vereda = models.OneToOneField(
        'Vereda',
        related_name='citizen',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name_1


class Complaint(models.Model):
    status = models.CharField(max_length=45)
    # TODO: expediente

    whistleblower = models.ForeignKey(
        'Citizen',
        related_name='whistleblowers',
        on_delete=models.CASCADE
    )
    denounced = models.ForeignKey(
        'Citizen',
        related_name='denounceds',
        on_delete=models.CASCADE
    )
    victim = models.ForeignKey(
        'Citizen',
        related_name='victims',
        on_delete=models.CASCADE
    )
    hostess = models.ForeignKey(
        'Citizen',
        related_name='hostess',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.status
