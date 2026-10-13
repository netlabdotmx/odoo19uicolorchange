# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    brand_color = fields.Char(
        string="Color de la interfaz",
        config_parameter="odoo19uicolorchange.brand_color",
        default="#b51f23",
        help="Código de color hexadecimal (ej. #b51f23) que se aplica a la barra "
             "superior, botones principales, facetas del buscador y menú de apps.",
    )

    def action_save_and_reload(self):
        """Guarda el color y recarga la página para que el nuevo valor,
        que viaja en session_info, se aplique de inmediato."""
        self.execute()
        return {
            "type": "ir.actions.client",
            "tag": "reload",
        }
