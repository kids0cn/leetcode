from collections import OrderedDict
# 有顺序的字典类

favorite_languages = OrderedDict()
favorite_languages['jens'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
    print(name.title()+'favorite_languages is '+language.title()+'.')
