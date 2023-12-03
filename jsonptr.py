import re


def evaluate_token_array(token: str, data: tuple):
    if not re.fullmatch(r'-*[0-9]+', token):
        raise Exception("jsonptr: Requested Position \"{0}\" not a Number".format(token))
    position = int(token)
    if position >= 0 and len(data) <= position:
        raise Exception("jsonptr: Requested Position {1} to not in array with data length {0}".format(len(data), position))
    elif len(data) < abs(position):
        raise Exception("jsonptr: Requested Position {1} to not in array with data length {0}".format(len(data), position))
    return data[position]


def evaluate_token(token: str, data, default):
    token = re.sub(r'~1', '/', token)
    token = re.sub(r'~0', '~', token)

    if isinstance(data, list):
        return evaluate_token_array(token, data)
    elif isinstance(data, dict):
        return data.get(token, default)


def evaluate_ptrExpr(expr: str, data, default):
    if "" == expr:
        return data
    tokens = re.split('/', expr)
    for token in tokens[1:]:
        data = evaluate_token(token, data, default)
    return data


def get(expr: str, data, default=None):
    '''get value specified by expr from data
    Arguments;
        expr: "\foo\bar"  rfc6901 compliant jsonptr
        data: {'foo':'bar':1}
        default: default return value
    '''
    if data == None or expr == None:
        return default
    elif not isinstance(expr, str):
        raise Exception("jsonptr: expr {0} is not a string".format(expr) )
    return evaluate_ptrExpr(expr, data, default)