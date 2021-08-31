from trie import Trie


def test_empty_dictionary():
    dictionary = []
    trie = Trie.create_from_dictionary(dictionary)
    assert not trie.is_in_dictionary('a')
    assert not trie.is_in_dictionary('')


def test_empty_string():
    dictionary = ['', 'abc', 'xvc']
    trie = Trie.create_from_dictionary(dictionary)
    assert trie.is_in_dictionary('')
    assert trie.is_in_dictionary('abc')
    assert trie.is_in_dictionary('xvc')

    assert not trie.is_in_dictionary('a')


def test_dictionary():
    dictionary = ['a', 'ab', 'abc', 'acs', 'aac', 'bc', 'bce']
    trie = Trie.create_from_dictionary(dictionary)
    assert trie.is_in_dictionary('a')
    assert trie.is_in_dictionary('abc')
    assert trie.is_in_dictionary('bce')

    assert not trie.is_in_dictionary('')
    assert not trie.is_in_dictionary('xxd')
    assert not trie.is_in_dictionary('abca')


def test_get_dictionary():
    dictionary = ['', 'a', 'ab', 'abc', 'acs', 'aac', 'bc', 'bce']
    trie = Trie.create_from_dictionary(dictionary)
    print(trie.get_dictionary())
    assert set(trie.get_dictionary()) == set(dictionary)

