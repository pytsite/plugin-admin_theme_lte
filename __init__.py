"""PytSite AdminLTE Theme Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load_wsgi():
    """Hook
    """
    from plugins import admin
    from ._theme import Theme

    # Register admin theme
    admin.register_theme(Theme())
