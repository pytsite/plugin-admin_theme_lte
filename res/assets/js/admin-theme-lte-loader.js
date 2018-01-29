require(['jquery', 'cookie', 'assetman', 'twitter-bootstrap', 'admin-theme-lte'], function ($, cookie) {
    $('.sidebar-toggle').click(function () {
        if ($('body').hasClass('sidebar-collapse'))
            cookie.remove('adminSidebarCollapsed');
        else
            cookie.set('adminSidebarCollapsed', '1', {expires: 3650});
    });
});
