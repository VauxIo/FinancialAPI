import falcon
import json
from peewee import *
from wsgiref import simple_server

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

class TickerCollection:

    def on_get(self, req, resp):

        tickers = [company.ticker for company in Company.select()]

        resp.body = json.dumps(tickers)

app = falcon.API()
app.add_route('/tickers/', TickerCollection())

if __name__ == '__main__':

    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
