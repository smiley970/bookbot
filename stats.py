
def splitter(text):
    num_word = 0
    for a in text.split():
        num_word += 1
    return num_word    

def number(num):
    dic = {}
    for i in num.lower():
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic       

def list_dict(listed):
    new = []
    for a,b in listed.items():
        new_d = {}
        new_d = {"char": a, "num": b}
        new.append(new_d)
    new.sort(reverse=True, key=sort_on)
    return new

def sort_on(items):
    return items["num"] 