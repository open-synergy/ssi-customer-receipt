# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from lxml import etree
from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestCustomerReceipt(YamlTransactionCase):
    def test_customer_receipt(self):
        self.run_yaml_scenario("test_data_customer_receipt.yaml")

    def test_form_view_policy_page_once_and_field_order(self):
        """Assert the rendered form view has no duplicated Policies page.

        Pure Python — trigger P1 (L-01/L-02: ``fields_view_get``'s return
        value is not a record, so YAML cannot inspect the rendered arch).
        Also asserts ``journal_id`` precedes ``destination_account_id`` in
        ``header_left`` (issue #12: the manual account must not be
        overwritten by the core compute once the journal is filled first).
        """
        result = self.env["customer_receipt"].fields_view_get(view_type="form")
        arch = etree.fromstring(result["arch"])

        policy_pages = arch.findall(".//page[@name='policy']")
        self.assertEqual(len(policy_pages), 1)

        policy_fields = arch.findall(".//field[@name='policy_template_id']")
        self.assertEqual(len(policy_fields), 1)

        header_left = arch.find(".//group[@name='header_left']")
        self.assertIsNotNone(header_left)
        child_names = [child.get("name") for child in header_left.findall("field")]
        self.assertIn("journal_id", child_names)
        self.assertIn("destination_account_id", child_names)
        self.assertLess(
            child_names.index("journal_id"),
            child_names.index("destination_account_id"),
        )

    def test_tree_and_search_views_keep_operating_unit_anchor(self):
        """Assert tree/search views still expose the OU anchor fields.

        Pure Python — trigger P1 (L-01/L-02: ``fields_view_get``'s return
        value is not a record, so YAML cannot inspect the rendered arch).
        ``ssi_customer_receipt_operating_unit`` inherits these views by
        xpathing ``field[@name='company_id']`` and ``filter[@name=
        'company']`` (issue #12 anchor contract).
        """
        tree_arch = etree.fromstring(
            self.env["customer_receipt"].fields_view_get(view_type="tree")["arch"]
        )
        self.assertTrue(tree_arch.findall(".//field[@name='company_id']"))

        search_arch = etree.fromstring(
            self.env["customer_receipt"].fields_view_get(view_type="search")["arch"]
        )
        self.assertTrue(search_arch.findall(".//field[@name='company_id']"))
        self.assertTrue(search_arch.findall(".//filter[@name='company']"))
