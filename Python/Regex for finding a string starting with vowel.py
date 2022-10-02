import re

regex = '^[aeiouAEIOU][A-Za-z0-9_]*'

def check(string):
    if(re.search(regex, string)):
        print('Valid')
    
    else:
        print('Invalid')


if __name__ == '__main__':
    string = 'Mohsin'
    check(string)

    string = 'aniket'
    check(string)

    string = 'sandy'
    check(string)