{
    "name": "custom_module_training",
    "summary": "Short (1 phrase/line) summary of the module's purpose",
    "author": "Daya Motor",
    "website": "https://github.com/fizzuddin-daya/odoo17-train",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Customizations",
    "version": "17.0.1.0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/purchase_order_attachment_requirement_view.xml",
    ],
    "license": "LGPL-3",
    # only loaded in demonstration mode
    # "demo": [
    #     "demo/demo.xml",
    # ],
    "application": False,
    "installable": True,
}
