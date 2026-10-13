/** @odoo-module **/
import { session } from "@web/session";

/**
 * Aplica el color configurado en Ajustes como variable CSS global.
 * El valor llega en session_info (ver models/ir_http.py). Si no es un
 * color hexadecimal válido no se toca nada y el CSS usa su color por
 * defecto (#b51f23).
 */
const HEX = /^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$/;
const color = (session.navbar_brand_color || "").trim();

if (HEX.test(color)) {
    document.documentElement.style.setProperty("--brand-navbar-color", color);
}
