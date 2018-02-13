"""PytSite AdminLTE Theme Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Union as _Union
from pytsite import html as _html, tpl as _tpl, router as _router, package_info as _package_info, lang as _lang
from plugins import admin as _admin, widget as _widget


class Theme(_admin.Theme):
    @property
    def name(self):
        return 'lte'

    @property
    def description(self):
        return 'AdminLTE'

    @staticmethod
    def _render_sidebar(sidebar: _admin.SideBar) -> _html.Aside:
        """Render admin's sidebar
        """
        aside = _html.Aside(css='main-sidebar')
        sidebar_section_em = _html.Section(css='sidebar')
        aside.append(sidebar_section_em)

        root_menu_ul = _html.Ul(css='sidebar-menu')
        sidebar_section_em.append(root_menu_ul)

        sections, menus = sidebar.items

        # Do actual rendering
        for section in sections:
            li = _html.Li(_lang.t(section['title']), css='header', data_section_weight=section['weight'])
            root_menu_ul.append(li)

            # Building top level menu item
            for menu in menus[section['sid']]:
                # Link
                a = _html.A(href=_router.url(menu['path'], lang=_lang.get_current()))

                # Icon
                if menu['icon']:
                    a.append(_html.I(css=menu['icon']))

                # Title
                a.append(_html.Span(_lang.t(menu['title'])))

                # Label
                if menu['label']:
                    label_class = 'label pull-right label-' + menu['label_class']
                    a.append(_html.Span(_lang.t(menu['label']), css=label_class))

                # List element
                li = _html.Li(data_menu_weight=menu['weight'])

                # Active state
                if menu['active']:
                    li.set_attr('css', 'active')

                li.append(a)
                root_menu_ul.append(li)

        return aside

    def render(self, navbar: _admin.NavBar, sidebar: _admin.SideBar, content: _Union[str, _html.Element]):
        return _tpl.render('admin_theme_lte@html', {
            'admin_sidebar': self._render_sidebar(sidebar),
            'admin_language_nav': _widget.select.LanguageNav('admin-language-nav', dropdown=True),
            'content': content,
            'core_name': _package_info.name('pytsite'),
            'core_url': _package_info.url('pytsite'),
            'core_version': _package_info.version('pytsite'),
            'sidebar_collapsed': _router.request().cookies.get('adminSidebarCollapsed') is not None,
        })
