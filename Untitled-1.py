def backward_string_by_word(text: str) -> str:
    r=text.split()
    k=''
    for i in r:
        if k=='':
            k=i[::-1]
        else:
            k=k+' '+i[::-1]
    print(k)
    return k


if __name__ == '__main__':
    print("Example:")
    print (backward_string_by_word('welcome to a game'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
