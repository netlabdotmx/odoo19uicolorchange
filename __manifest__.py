{
    "name": "Navbar Color Tinto Premium",
    "version": "1.1",
    "summary": "Tema tinto premium para barra superior, botones y switcher MURR en Odoo 19",
    "category": "Web",
    "depends": ["web"],
    "data": [
        "security/navbar_color_security.xml",
        "views/res_users_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "navbar_color/static/src/css/navbar_color.css",
            "navbar_color/static/src/js/switch_company_menu.js",
            "navbar_color/static/src/xml/switch_company_menu.xml",
        ]
    },
    "installable": True,
    "application": False,
    "author": "Custom",
    "license": "LGPL-3",
}
