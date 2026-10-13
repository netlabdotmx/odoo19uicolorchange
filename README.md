# Color de la Interfaz — Odoo 19 Community

Módulo para aplicar un **color de marca configurable** a la interfaz de Odoo 19
Community: barra superior, botones principales (`btn-primary`), facetas del
buscador y menú de aplicaciones.

El color **ya no está fijo en el código**: se define desde
**Ajustes → Color de la interfaz** escribiendo un código hexadecimal.

---

## Estructura

```
odoo19uicolorchange/
├── __manifest__.py
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── ir_http.py                 # expone el color en session_info
│   └── res_config_settings.py     # campo de color en Ajustes
├── views/
│   └── res_config_settings_views.xml   # página de Ajustes + menú
└── static/src/
    ├── css/navbar_color.css       # tema (usa la variable --brand-navbar-color)
    └── js/navbar_color.js         # aplica el color de la sesión como variable CSS
```

> ⚠️ **El nombre de la carpeta debe ser `odoo19uicolorchange`** (es el nombre
> técnico del módulo). Las rutas de los assets y los IDs dependen de él.

---

## Cómo funciona

1. El color se guarda en `ir.config_parameter` con la clave
   `odoo19uicolorchange.brand_color` (campo en `res.config.settings`).
2. `ir.http.session_info()` añade ese valor a la sesión como
   `navbar_brand_color`.
3. `navbar_color.js` lee el valor al cargar el bundle y, si es un hex válido,
   lo escribe en `--brand-navbar-color` sobre `:root`.
4. El CSS usa `var(--brand-navbar-color, #b51f23)`: si no hay valor o es
   inválido, cae al color por defecto `#b51f23`.

---

## Uso

1. Instalar el módulo (Apps → actualizar lista → "Color de la Interfaz").
2. Ir a **Ajustes → Color de la interfaz** (visible para administradores).
3. Escribir el color en hexadecimal, p. ej. `#1565C0`.
4. **Guardar**: la página se recarga y el color se aplica de inmediato.

Ejemplos:

| Color | Hex |
|-------|-----|
| Rojo tinto (default) | `#b51f23` |
| Azul corporativo | `#1565C0` |
| Verde | `#2E7D32` |
| Naranja | `#E65100` |
| Morado | `#6A1B9A` |
| Negro | `#212121` |

---

## Instalación

```bash
# 1. Clonar / copiar el módulo en el addons_path (carpeta = odoo19uicolorchange)
cp -r odoo19uicolorchange/ /opt/odoo/extra-addons/

# 2. Verificar addons_path
grep addons_path /etc/odoo/odoo.conf

# 3. Reiniciar Odoo y actualizar la lista de apps
systemctl restart odoo
```

No requiere editar archivos para cambiar el color; se hace desde Ajustes.

---

## Notas

- El tema aplica a **todos** los `.btn-primary` del backend (no solo al navbar).
- El color por defecto se puede cambiar en `DEFAULT_BRAND_COLOR`
  (`models/ir_http.py`) y en el `:root` de `navbar_color.css`.
- No incluye funcionalidad de empresas/switcher: es puramente de color.
