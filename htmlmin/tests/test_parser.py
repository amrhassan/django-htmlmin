# -*- coding: utf-8 -*-
import unittest

from htmlmin.parser import HtmlMinifyParser


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.parser = HtmlMinifyParser('<section><p><section></section></p></section>')

    def test_should_be_able_to_nest_section_tag(self):
        assert 'section' in self.parser.NESTABLE_BLOCK_TAGS, '<section> should be nestable'

    def test_should_be_able_to_nest_header_tag(self):
        assert 'header' in self.parser.NESTABLE_BLOCK_TAGS, '<header> should be nestable'

    def test_should_be_able_to_nest_article_tag(self):
        assert 'article' in self.parser.NESTABLE_BLOCK_TAGS, '<article> should be nestable'

    def test_should_be_able_to_nest_menu_tag(self):
        assert 'menu' in self.parser.NESTABLE_BLOCK_TAGS, '<menu> should be nestable'

    def test_should_be_able_to_nest_footer_tag(self):
        assert 'footer' in self.parser.NESTABLE_BLOCK_TAGS, '<footer> should be nestable'

    def test_should_not_reset_nesting_on_section_tag(self):
        assert self.parser.RESET_NESTING_TAGS['section'] is None, '<section> should not reset nesting'

    def test_should_not_reset_nesting_on_header_tag(self):
        assert self.parser.RESET_NESTING_TAGS['header'] is None, '<header> should not reset nesting'

    def test_should_not_reset_nesting_on_article_tag(self):
        assert self.parser.RESET_NESTING_TAGS['article'] is None, '<article> should not reset nesting'

    def test_should_not_reset_nesting_on_footer_tag(self):
        assert self.parser.RESET_NESTING_TAGS['footer'] is None, '<footer> should not reset nesting'
