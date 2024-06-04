import string
import random

from .models import Promocode


symbols = list(string.ascii_letters) + [str(x) for x in range(10)]


def generate_code(prefix):

    code = prefix

    for i in range(10-len(prefix)):
        code += random.choice(symbols)
    
    return code


def create_promocodes(count:int, prefix:str, amount:int):
    queryset = []
    for i in range(count):
        queryset.append(
            Promocode.objects.create(
                code=generate_code(prefix)
            )
        )
    return queryset