import 'font-awesome/css/font-awesome.css';
import '@pytsite/bootstrap/v3/css/bootstrap.css';
import '@pytsite/bootstrap/v3/css/add-ons.css';
import '@pytsite/bootstrap/v3/js/bootstrap.js';
import './AdminLTE/css/AdminLTE.css';
import './AdminLTE/css/skins/skin-blue.css';
import './css/custom.scss';
import './AdminLTE/js/app.js';

const $ = require('jquery');
const cookie = require('js-cookie');

$('.sidebar-toggle').click(function () {
    if ($('body').hasClass('sidebar-collapse'))
        cookie.remove('adminSidebarCollapsed');
    else
        cookie.set('adminSidebarCollapsed', '1', {expires: 3650});
});
