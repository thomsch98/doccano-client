from unittest import TestCase

from doccano_api_client import objectify


class Objectify_Tests(TestCase):
    def test_objectify_from_kwargs(self):
        o = objectify(id=5, text='bla')
        assert o.id == 5
        assert o.text == 'bla'

    def test_objectify_from_dict_arg(self):
        o = objectify({'id': 5, 'text': 'bla'})
        assert o.id == 5
        assert o.text == 'bla'

    def test_objectify_from_list_arg(self):
        o = objectify([{'id': 5, 'text': 'bla'}])
        assert o[0].id == 5
        assert o[0].text == 'bla'
