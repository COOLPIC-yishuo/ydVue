from django import template
import hashlib
register = template.Library()

# str1 = hashlib.md5()
# str1.update(bytes("123456",encoding="utf-8"))
# print(str1.hexdigest())

@register.filter
def up(value):
    return value.upper()