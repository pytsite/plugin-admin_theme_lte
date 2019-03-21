"""PytSite AdminLTE Theme Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _build_assets():
    from plugins import assetman

    assetman.build(__name__)


def plugin_load_wsgi():
    """Hook
    """
    from plugins import admin
    from ._theme import Theme

    # Register admin theme
    admin.register_theme(Theme())


def plugin_install():
    _build_assets()
