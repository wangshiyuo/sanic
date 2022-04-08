def is_id_or_name(word):
    if len(word) == 5 and word.isdigit():
        return 'id'
    else:
        return 'name'
