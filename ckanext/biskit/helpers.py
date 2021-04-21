from paste.deploy.converters import asbool
from ckan.common import config


def get_show_debug_link():
    """Indicates whether to show the debug link in the footer or not.
    """
    value = config.get('ckanext.biskit.show_debug_link', 'True')
    return asbool(value)
