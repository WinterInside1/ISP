import re


def parse_dumps(obj):
    if obj is None:
        return "null"
    elif isinstance(obj, bool):
        return str(obj).lower()
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        return "\"" + obj.replace('\\', '\\\\').replace('\n', '\\n') + "\""
    elif isinstance(obj, list):
        return f"[{','.join(parse_dumps(o) for o in obj)}]"
    elif isinstance(obj, dict):
        return "{" + ",".join(f"\"{key}\":{parse_dumps(val)}" for key, val in obj.items()) + "}"


def parse_loads(string):
    string.replace("\n", "")
    ret = {}
    temp = ""
    key = ""
    k = 0
    l = len(string)
    while k < l:
        l = len(string)
        if string == "{":
            return ret
        try:
            i = string[k]
        except IndexError:
            print(string)
            return ret
        if i == ",":
            val = temp
            ret[key] = val
            temp = ""
            key = ""
            k += 1
            continue
        if i == ":":
            key = temp
            temp = ""
            k += 1
            if string[k + 1] == "{":
                test = string[(k + 1):]
                v = ""
                num = -1
                for i in test:
                    if i == "{":
                        num = num + 1
                    if i == "}" and num == 0:
                        v = v + i
                        break
                    if i == "}":
                        num = num - 1
                    v = v + i

                temp = parse_loads(v)
                print(v)
                string = string.replace(v, "")

            continue
        if i == "{":
            test = string[(k + 1):]
            ret = parse_loads(test)
            string = string.replace(test, "")
            key = ""
        if i == "}":
            ret[key] = temp
            return ret
        temp = temp + str(i)
        k += 1

    ret[key] = temp
    return ret
