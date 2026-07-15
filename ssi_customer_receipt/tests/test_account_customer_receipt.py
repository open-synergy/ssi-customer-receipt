# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestAccountCustomerReceipt(YamlTransactionCase):
    def test_account_customer_receipt(self):
        self.run_yaml_scenario("test_data_account_customer_receipt.yaml")
