"""PytSite AdminLTE Theme Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import htmler
from typing import Union
from pytsite import tpl, router, package_info, lang
from plugins import admin, widget


class Theme(admin.Theme):
    @property
    def name(self):
        return 'lte'

    @property
    def description(self):
        return 'AdminLTE'

    @staticmethod
    def _render_sidebar(sidebar: admin.SideBar) -> htmler.Aside:
        """Render admin's sidebar
        """
        aside = htmler.Aside(css='main-sidebar')
        sidebar_section_em = htmler.Section(css='sidebar')
        aside.append_child(sidebar_section_em)

        root_menu_ul = htmler.Ul(css='sidebar-menu')
        sidebar_section_em.append_child(root_menu_ul)

        sections, menus = sidebar.items

        # Do actual rendering
        for section in sections:
            li = htmler.Li(lang.t(section['title']), css='header', data_section_weight=section['weight'])
            root_menu_ul.append_child(li)

            # Building top level menu item
            for menu in menus[section['sid']]:
                # Link
                a = htmler.A(href=router.url(menu['path'], lang=lang.get_current()))

                # Icon
                if menu['icon']:
                    a.append_child(htmler.I(css=menu['icon']))

                # Title
                a.append_child(htmler.Span(lang.t(menu['title'])))

                # Label
                if menu['label']:
                    label_class = 'label pull-right label-' + menu['label_class']
                    a.append_child(htmler.Span(lang.t(menu['label']), css=label_class))

                # List element
                li = htmler.Li(data_menu_weight=menu['weight'])

                # Active state
                if menu['active']:
                    li.set_attr('css', 'active')

                li.append_child(a)
                root_menu_ul.append_child(li)

        return aside

    def render(self, navbar: admin.NavBar, sidebar: admin.SideBar, content: Union[str, htmler.Element]):
        return tpl.render('admin_theme_lte@html', {
            'admin_sidebar': self._render_sidebar(sidebar),
            'admin_language_nav': widget.select.LanguageNav('admin-language-nav', dropdown=True, bs_version=3),
            'content': content,
            'core_name': package_info.name('pytsite'),
            'core_url': package_info.url('pytsite'),
            'core_version': package_info.version('pytsite'),
            'sidebar_collapsed': router.request().cookies.get('adminSidebarCollapsed') is not None,
        })
