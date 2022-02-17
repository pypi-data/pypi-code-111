# Copyright 2016-20 ForgeFlow S.L. (https://www.forgeflow.com)
# Copyright 2016 Aleph Objects, Inc. (https://www.alephobjects.com/)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "DDMRP",
    "summary": "Demand Driven Material Requirements Planning",
    "version": "15.0.1.2.0",
    "license": "LGPL-3",
    "development_status": "Beta",
    "author": "ForgeFlow, " "Odoo Community Association (OCA)",
    "maintainers": ["JordiBForgeFlow", "LoisRForgeFlow", "ChrisOForgeFlow"],
    "website": "https://github.com/OCA/ddmrp",
    "category": "Warehouse",
    "depends": [
        "purchase_stock",
        "mrp_bom_location",
        "stock_demand_estimate",
        "web_widget_bokeh_chart",
        "mrp_multi_level",
        "base_cron_exclusion",
        "stock_warehouse_calendar",
        "stock_helper",
    ],
    "data": [
        "data/product_adu_calculation_method_data.xml",
        "data/stock_buffer_profile_variability_data.xml",
        "data/stock_buffer_profile_lead_time_data.xml",
        "data/stock_buffer_profile_data.xml",
        "data/ir_sequence.xml",
        "data/decimal_precision_data.xml",
        "security/ir.model.access.csv",
        "security/stock_security.xml",
        "security/stock_buffer_manual_procurement_security.xml",
        "wizards/make_procurement_buffer_view.xml",
        "views/stock_buffer_profile_view.xml",
        "views/stock_buffer_profile_variability_view.xml",
        "views/stock_buffer_profile_lead_time_view.xml",
        "views/product_adu_calculation_method_view.xml",
        "views/stock_warehouse_views.xml",
        "views/mrp_production_view.xml",
        "views/purchase_order_view.xml",
        "views/purchase_order_line_view.xml",
        "views/mrp_bom_view.xml",
        "views/stock_move_views.xml",
        "views/stock_buffer_view.xml",
        "views/stock_picking.xml",
        "report/mrp_report_bom_structure.xml",
        "data/ir_cron.xml",
        "wizards/ddmrp_run_view.xml",
        "wizards/res_config_settings_views.xml",
    ],
    "demo": [
        "demo/res_partner_demo.xml",
        "demo/product_category_demo.xml",
        "demo/product_product_demo.xml",
        "demo/product_supplierinfo_demo.xml",
        "demo/mrp_bom_demo.xml",
        "demo/stock_buffer_demo.xml",
    ],
    "post_load": "post_load_hook",
    "installable": True,
    "application": True,
    "assets": {
        "web.assets_backend": [
            "ddmrp/static/src/js/list_renderer_buffer_info.js",
            "ddmrp/static/src/scss/list_view.scss",
        ],
    },
}
