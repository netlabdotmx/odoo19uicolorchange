# Navbar Color — Odoo 19 Community

Módulo para aplicar un color personalizado a la barra superior, todos los botones primarios y las facetas del buscador en Odoo 19 Community. Incluye también un badge de empresa de solo lectura en el navbar.

---

## Estructura de archivos

```
navbar_color/
├── __manifest__.py
└── static/src/
    ├── css/navbar_color.css
    ├── js/switch_company_menu.js
    └── xml/switch_company_menu.xml
```

---

## `__manifest__.py`

```python
{
    "name": "Navbar Color Tinto Premium",
    "version": "1.1",
    "summary": "Tema tinto premium para barra superior, botones y switcher en Odoo 19",
    "category": "Web",
    "depends": ["web"],
    "assets": {
        "web.assets_backend": [
            "navbar_color/static/src/css/navbar_color.css",
            "navbar_color/static/src/js/switch_company_menu.js",
            "navbar_color/static/src/xml/switch_company_menu.xml",
        ]
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
```

> No depende de ningún otro módulo personalizado. Solo requiere `web`.

---

## `static/src/css/navbar_color.css`

Estrategia: una **CSS variable central** en `:root`. Para cambiar el color solo se modifica esa línea.

```css
:root {
    --brand-navbar-color: #b51f23;  /* ← cambiar aquí */
}

/* ── Navbar completa ── */
.o_main_navbar,
.o_main_navbar > .o_menu_sections,
.o_main_navbar .o_menu_brand,
.o_main_navbar .o_menu_toggle,
.o_main_navbar .o_menu_systray,
.o_main_navbar .o_menu_systray .dropdown-toggle,
.o_main_navbar .o_menu_sections .dropdown-toggle,
.o_main_navbar .o_menu_sections .o_nav_entry {
    background-color: var(--brand-navbar-color) !important;
    color: #ffffff !important;
    border: none !important;
}

/* Hover y estado activo */
.o_main_navbar .o_nav_entry:hover,
.o_main_navbar .o_menu_brand:hover,
.o_main_navbar .o_menu_toggle:hover,
.o_main_navbar .o_menu_sections .dropdown-toggle:hover {
    filter: brightness(0.85) !important;
}
.o_main_navbar .o_menu_sections .show > .dropdown-toggle {
    filter: brightness(0.8) !important;
}

/* ── Todos los btn-primary en la app ── */
.btn-primary {
    background-color: var(--brand-navbar-color) !important;
    border-color: var(--brand-navbar-color) !important;
    color: #ffffff !important;
}
.btn-primary:hover,
.btn-primary:active,
.btn-primary:focus {
    filter: brightness(0.85) !important;
}

/* ── Facetas del buscador ── */
.o_searchview_facet .o_searchview_facet_label {
    background-color: var(--brand-navbar-color) !important;
    color: white !important;
}

/* ── Menú de apps nativo Community (sin app_menu_enterprise) ── */
.o_home_menu {
    background-color: var(--brand-navbar-color) !important;
    background-image: none !important;
}
.o_home_menu .o_app.o_focused {
    background-color: rgba(255, 255, 255, 0.2) !important;
}

/* ── Ocultar switcher nativo, mostrar badge personalizado ── */
.o_main_navbar .o_switch_company_menu,
.o_burger_menu_companies {
    display: none !important;
}

.o_main_navbar .o_murr_company_label {
    display: inline-flex !important;
    gap: 0.4rem;
    white-space: nowrap;
}
.o_main_navbar .o_murr_company_caption {
    font-size: 12px;
    letter-spacing: 0.08em;
    opacity: 0.8;
    text-transform: uppercase;
}
.o_main_navbar .o_murr_company_value {
    padding: 0.2rem 0.55rem;
    border: 1px solid rgba(255, 255, 255, 0.35);
    border-radius: 0.35rem;
    font-size: 14px;
    font-weight: 700;
    line-height: 1.2;
}

/* Dropdown de empresa: alineación interna */
.o_switch_company_menu_dropdown .o_switch_company_item {
    padding-left: 8px !important;
}
.o_switch_company_menu_dropdown .o_switch_company_item .log_into,
.o_switch_company_menu_dropdown .o_switch_company_item .company_label {
    padding-left: 0 !important;
}
```

**Puntos clave:**
- `!important` es necesario para sobreescribir los estilos inline y de Bootstrap que usa Odoo
- `filter: brightness(0.85)` para hover evita definir un segundo color manualmente
- Aplica a **todos** los `btn-primary` de la app, no solo al navbar

---

## `static/src/js/switch_company_menu.js`

Patch del componente `SwitchCompanyMenu` para mostrar solo la empresa activa en el dropdown (modo una sola empresa):

```js
/** @odoo-module **/
import { SwitchCompanyMenu } from "@web/webclient/switch_company_menu/switch_company_menu";
import { patch } from "@web/core/utils/patch";
import { user } from "@web/core/user";

patch(SwitchCompanyMenu.prototype, {
    computeVisibleCompanies() {
        const all = super.computeVisibleCompanies();
        if (!user.activeCompany) {
            return all;
        }
        return all.filter((entry) => entry.company.id === user.activeCompany.id);
    },
});
```

> Para entornos multi-empresa: eliminar este archivo y quitarlo del `__manifest__.py`.

---

## `static/src/xml/switch_company_menu.xml`

Dos patches con `t-inherit-mode="extension"`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<templates xml:space="preserve">

    <!-- Patch 1: nombre de empresa activa en topbar + badge de solo lectura -->
    <t t-name="web.SwitchCompanyMenu" t-inherit="web.SwitchCompanyMenu" t-inherit-mode="extension">
        <xpath expr="//span[hasclass('oe_topbar_name')]" position="replace">
            <span class="oe_topbar_name d-none d-lg-block text-truncate">
                <t t-esc="user.activeCompany.name"/>
            </span>
        </xpath>
        <xpath expr="//div[hasclass('o_switch_company_menu')]" position="after">
            <div class="o_murr_company_label d-none d-md-flex align-items-center ms-2 text-white"
                 style="pointer-events: none; user-select: none;">
                <span class="o_murr_company_caption me-2">Empresa</span>
                <span class="o_murr_company_value"
                      t-esc="user.defaultCompany ? user.defaultCompany.name : user.activeCompany.name"/>
            </div>
        </xpath>
    </t>

    <!-- Patch 2: rediseñar ítem del dropdown (sin checkbox, palomita a la derecha) -->
    <t t-name="web.SwitchCompanyItem" t-inherit="web.SwitchCompanyItem" t-inherit-mode="extension">
        <xpath expr="//div[@role='menuitemcheckbox']" position="replace"/>
        <xpath expr="//div[@role='button']" position="after">
            <div class="d-flex align-items-center pe-2" style="width:20px;">
                <i t-if="isCompanySelected" class="fa fa-check text-primary" style="font-size:11px;"/>
            </div>
        </xpath>
        <xpath expr="//span[hasclass('company_label')]" position="attributes">
            <attribute name="t-attf-style">padding-left:0px;</attribute>
        </xpath>
    </t>

</templates>
```

**Puntos clave:**
- `t-inherit="web.SwitchCompanyMenu"` — nombre exacto del template original
- `t-inherit-mode="extension"` — extiende, no reemplaza
- El badge usa `pointer-events: none` para que sea puramente decorativo (no abre el dropdown)
- `user.defaultCompany` tiene prioridad sobre `user.activeCompany` para mostrar el nombre

---

## Instalación

```bash
# 1. Copiar al directorio de addons
cp -r navbar_color/ /opt/odoo/extra-addons/

# 2. Verificar addons_path en /etc/odoo/odoo.conf
grep addons_path /etc/odoo/odoo.conf
# Debe incluir /opt/odoo/extra-addons

# 3. Reiniciar Odoo
systemctl restart odoo

# 4. En Odoo: Ajustes → Activar modo desarrollador → Apps → instalar "Navbar Color Tinto Premium"
```

---

## Cambiar el color

Editar una sola línea en `static/src/css/navbar_color.css`:

```css
:root {
    --brand-navbar-color: #b51f23;  /* ← poner el color deseado */
}
```

Ejemplos:
| Color | Hex |
|-------|-----|
| Rojo tinto (default) | `#b51f23` |
| Azul corporativo | `#1565C0` |
| Verde | `#2E7D32` |
| Naranja | `#E65100` |
| Morado | `#6A1B9A` |
| Negro | `#212121` |

Después reiniciar Odoo (no requiere reinstalar el módulo):

```bash
systemctl restart odoo
```
