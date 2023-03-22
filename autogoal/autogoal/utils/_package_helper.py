import re
import pkg_resources

def find_packages(regex):
    """
    Example usage:

    >>> matching_packages = find_packages(r'^numpy')
    >>> print(matching_packages)
    [numpy 1.24.2 (/usr/local/lib/python3.9/site-packages)]
    """
    installed_packages = [d for d in pkg_resources.working_set]
    pattern = re.compile(regex)
    matching_packages = [package for package in installed_packages if pattern.search(str(package))]
    return matching_packages
