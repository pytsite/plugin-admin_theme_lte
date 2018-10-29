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
    from pytsite import plugman
    from plugins import admin
    from ._theme import Theme

    # Register admin theme
    admin.register_theme(Theme())

    # Events handlers
    plugman.on_install_all(_build_assets)


def plugin_install():
    _build_assets()
