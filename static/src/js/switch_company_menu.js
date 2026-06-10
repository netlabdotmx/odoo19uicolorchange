/** @odoo-module **/
import { SwitchCompanyMenu } from "@web/webclient/switch_company_menu/switch_company_menu";
import { patch } from "@web/core/utils/patch";
import { user } from "@web/core/user";
import { session } from "@web/session";

/**
 * Si el usuario tiene el grupo 'Cambio de Ruta Multi-Empresa', se muestra
 * el listado completo de empresas permitidas (comportamiento estándar de Odoo).
 * Si no tiene el grupo, solo se muestra la empresa activa (modo lectura).
 */
patch(SwitchCompanyMenu.prototype, {
    computeVisibleCompanies() {
        if (session.murr_can_switch_route) {
            return super.computeVisibleCompanies();
        }
        const all = super.computeVisibleCompanies();
        if (!user.activeCompany) {
            return all;
        }
        return all.filter((entry) => entry.company.id === user.activeCompany.id);
    },
});
