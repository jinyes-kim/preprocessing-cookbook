# remove special character
def rm_sp_char(list_data):
    res_list = [''.join(x for x in word if x.isalnum()) for word in list_data]
    return res_list


# remove special character & number
def rm_sp_char_num(list_data):
    res_list = [''.join(x for x in word if x.isalpha()) for word in list_data]
    return res_list


# word count
def word_count(list_data):
    res_dict = {}
    for word in list_data:
        if word in res_dict:
            res_dict[word] += 1
        else:
            res_dict[word] = 1

    return res_dict


# example
sample = ['a!!123', 'a!', '!b', 'thisis###', 'c', 'c1']
tmp = word_count(rm_sp_char_num(sample))
print(tmp)





####################
# generator style


# remove special character
def rm_sp_char(list_data):
    res_list = [''.join(x for x in word if x.isalnum()) for word in list_data]
    for word in res_list:
        yield word
    return


# remove special character & number
def rm_sp_char_num(list_data):
    res_list = [''.join(x for x in word if x.isalpha()) for word in list_data]
    for word in res_list:
        yield word
    return


# word count
def word_count(list_data):
    res_dict = {}
    for word in list_data:
        if word in res_dict:
            res_dict[word] += 1
        else:
            res_dict[word] = 1

    return res_dict


# example
sample = ['a!!123', 'a!', '!b', 'thisis###', 'c', 'c1']

res = []
for word in rm_sp_char_num(sample):
    res.append(word)

print(res)

res = word_count(res)
print(res)
