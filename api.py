from peewee import *

db = SqliteDatabase('data.db')

class Company(Model):

    ticker = CharField(unique=True)

    class Meta:

        database = db

class Record(Model):

    company = ForeignKeyField(Company, related_name="records")
    date = DateField()
    high = DecimalField()
    low = DecimalField()
    last_price = DecimalField()
    open = DecimalField()
    px_last = DecimalField()

    class Meta:

        database = db

db.connect()
db.create_tables([Company,Record], safe=True)
