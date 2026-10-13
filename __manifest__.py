{
    "name": "Color de la Interfaz",
    "version": "19.0.1.0.0",
    "summary": "Cambia el color de la barra superior, botones y acentos de Odoo 19 desde Ajustes",
    "description": """
Tema de color configurable para Odoo 19 Community.

Aplica un color de marca a la barra superior, los botones principales,
las facetas del buscador y el menú de aplicaciones. El color se define
desde Ajustes (código hexadecimal), no está fijo en el código.
""",
    "category": "Web",
    "depends": ["web"],
    "data": [
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "odoo19uicolorchange/static/src/css/navbar_color.css",
            "odoo19uicolorchange/static/src/js/navbar_color.js",
        ]
    },
    "installable": True,
    "application": False,
    "author": "netlab",
    "license": "LGPL-3",
}
