from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    IntegerField,
                    OperationalError,
                    IntegrityError)
db = SqliteDatabase("artwork.db")

class Artwork(Model):
   
    name = CharField(max_length=1000, unique=True)
    description = TextField(default="Good image")
    thumbnail_link = CharField(max_length=1000)
    fullimage_link = CharField(max_length=1000)
   

    class Meta:
        database = db

def initialize():
    try:
        Artwork.create_table(safe=True)
    except OperationalError:
        pass
    try:
        Artwork.create(
          name="monkey_singing",
          description="Awesome Artistic Monkey",
          thumbnail_link="https://artwork-with-python--feliciahmtoka.repl.co/static/music2.jpg",
          fullimage_link="https://artwork-with-python--feliciahmtoka.repl.co/static/music1.jpg"
    )
    except IntegrityError:
            pass
    try:
        Artwork.create(
          name="water_splashing",
          description="Awesome water Splash",
          thumbnail_link="https://artwork-with-python--feliciahmtoka.repl.co/static/splashingsmall.jpg",
          fullimage_link="https://artwork-with-python--feliciahmtoka.repl.co/static/splashingbig.jpg"
    )

    
    except IntegrityError as e:
            pass


