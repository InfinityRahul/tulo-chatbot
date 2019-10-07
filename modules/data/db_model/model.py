from mongoengine import *
from modules.utils.yaml_parser import Config
import json

url = Config.get_config_val(key="mongodb", key_1depth="url")
db = Config.get_config_val(key="mongodb", key_1depth="db")
connect(db, host=url)


class Circumstance(EmbeddedDocument):
    input_circumstance = StringField(required=False, max_length=100)
    output_circumstance = StringField(required=False, max_length=100)


class Variables(EmbeddedDocument):
    name = StringField(required=True, max_length=100)  # number_1
    type = StringField(required=True, max_length=100)  # @def.number
    value = StringField(required=True, max_length=100)  # $number1
    io_type = StringField(required=True, max_length=100)  # @def.input


class Response(EmbeddedDocument):
    text = ListField(StringField(required=False, max_length=1000))
    custom = StringField(required=False)


# This is the final class
class Train(Document):
    lang = StringField(required=True)
    category = StringField(required=True)
    circumstance = EmbeddedDocumentField('Circumstance')
    variables = ListField(EmbeddedDocumentField('Variables'))
    training_queries = ListField(StringField(required=True, max_length=1000))
    response = ListField(EmbeddedDocumentField('Response'))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
