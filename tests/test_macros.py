import pytest
import jinja2


TEMPLATE_DIR = 'nsadm/templates'
TEST_DIR = 'nsadm/templates/tests/'


class TestMacros():
    @pytest.fixture(scope='class')
    def env(self):
        template_loader = jinja2.FileSystemLoader(TEMPLATE_DIR)
        env = jinja2.Environment(loader=template_loader, trim_blocks=True, lstrip_blocks=True)

        yield env

    def test_gen_header_with_urls(self, env):
        template = env.get_template('tests/gen_header_with_urls_test.txt')

        assert template.render(current_dispatch='test1') == open(TEST_DIR + 'gen_header_with_urls_expected.txt').read()

    def test_gen_header_with_sub_urls(self, env):
        template = env.get_template('tests/gen_sub_urls_header_test.txt')

        assert template.render(current_dispatch='test1') == open(TEST_DIR + 'gen_sub_urls_header_expected.txt').read()

    def test_gen_header_with_no_urls(self, env):
        template = env.get_template('tests/gen_header_with_no_urls_test.txt')

        assert template.render(current_dispatch='test1') == open(TEST_DIR + 'gen_header_with_no_urls_expected.txt').read()

    def test_gen_subheader_with_urls(self, env):
        template = env.get_template('tests/gen_subheader_with_urls_test.txt')

        assert template.render(current_dispatch='test1') == open(TEST_DIR + 'gen_subheader_with_urls_expected.txt').read()



