from django.test.runner import DiscoverRunner

class AppsDiscoverRunner(DiscoverRunner):
    def build_suite(self, test_labels=None, extra_tests=None, **kwargs):
        if not test_labels:
            test_labels = ['apps']
        return super().build_suite(test_labels=test_labels, extra_tests=extra_tests, **kwargs)