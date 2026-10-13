# -*- coding: utf-8 -*-
from odoo import models
from odoo.http import request

# Color por defecto si no se ha configurado nada en Ajustes.
DEFAULT_BRAND_COLOR = "#b51f23"


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        """Expone el color de marca al frontend dentro de la sesión.

        El JS lo lee en el arranque del bundle y lo aplica como variable CSS,
        por lo que el color deja de estar fijo en el archivo .css.
        """
        result = super().session_info()
        color = DEFAULT_BRAND_COLOR
        try:
            color = request.env["ir.config_parameter"].sudo().get_param(
                "odoo19uicolorchange.brand_color", DEFAULT_BRAND_COLOR
            )
        except Exception:
            color = DEFAULT_BRAND_COLOR
        result["navbar_brand_color"] = color or DEFAULT_BRAND_COLOR
        return result
