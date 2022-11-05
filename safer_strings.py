def safe_string(string: str):
    # Define swear_words
    # There isn't a lot here right now, you could get creative with it
    swear_words: [str] = [
        'damn',
        'goddamn',
        'shit',
        'shitload',
        'shitface',
        'chick',
        'dick',
        'shithead'
        'crap',
        'hell',
        'mf',
        'fuck',
        'fucking',
        'motherfucking',
        'motherfucker',
        'bitch',
        'bastard',
        'bastards',
        'retard',
        'retards',
        'retarded',
        'degenerate',
        'degenerates',
        'perverted',
        'pervert',
        'perverted',
        'incel',
        'incels'
    ]  # More trash words lol

    # Strip string of additional clutter
    clean_str: str = string.strip('.?!').replace('*', '')

    # Convert string to all lowercase
    l_str: str = clean_str.lower()

    # Create an array from the string
    chars: [] = l_str.split(' ')

    # Construct a safe string
    safe_str: str = ''

    # Keep track of how many swear words there are
    swear_words_count = 0

    # Loop through the array replacing swear words with '--'
    for char in chars:
        # Does the string contain a comma?
        if char.__contains__(','):
            fix = char.replace(',', '')
            if swear_words.__contains__(fix):
                safe_str += '--, '
                swear_words_count += 1
            else:
                safe_str += f'{char} '

        # Are quotes used?
        elif char.__contains__("'"):
            fix = char.split("'")[0]  # Word contains a ' and some other letters
            if swear_words.__contains__(fix):
                safe_str += '-- '
                swear_words_count += 1
            else:
                safe_str += f'{char} '

        else:
            if swear_words.__contains__(char):
                safe_str += '-- '
                swear_words_count += 1
            else:
                safe_str += f'{char} '

    print(safe_str)


# Accept use input as a string
# test -> 'caught some retards peeping at the girls' dressing room again, such perverted degenerates'
print('-- Strings should be more polite! --')
safe_string(str(input("TYPE IN HERE: ")))
