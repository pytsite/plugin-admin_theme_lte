"""PytSite AdminLTE Theme Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    """Hook
    """
    from pytsite import lang
    from plugins import assetman

    # Resources
    lang.register_package(__name__)
    assetman.register_package(__name__)

    # Assets
    assetman.t_js(__name__)
    assetman.t_css(__name__)
    assetman.t_less(__name__)
    assetman.js_module('admin-theme-lte', __name__ + '@AdminLTE/js/app', True, ['jquery', 'twitter-bootstrap'])


def plugin_install():
    """Hook
    """
    from plugins import assetman

    # Build assets
    assetman.build(__name__)


def plugin_load_uwsgi():
    """Hook
    """
    from pytsite import tpl
    from plugins import admin
    from ._theme import Theme

    # Resources
    tpl.register_package(__name__)

    # Register admin theme
    admin.register_theme(Theme())
