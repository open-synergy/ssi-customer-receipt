# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Customer Receipt",
    "version": "14.0.2.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "depends": [
        "ssi_financial_accounting",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/ir_rule/customer_receipt.xml",
        "views/customer_receipt_views.xml",
    ],
    "demo": [],
    "uninstall_hook": "uninstall_hook",
}
