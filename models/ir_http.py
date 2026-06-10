# -*- coding: utf-8 -*-
from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super().session_info()
        try:
            result['murr_can_switch_route'] = request.env.user.has_group(
                'navbar_color.group_murr_multi_route_switch'
            )
        except Exception:
            result['murr_can_switch_route'] = False
        return result
