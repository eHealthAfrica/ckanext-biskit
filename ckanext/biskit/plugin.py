import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.biskit import helpers


class BiskitPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'biskit')

    # ITemplateHelpers

    def get_helpers(self):
        return {
            "biskit_show_debug_link": helpers.get_show_debug_link,
        }
