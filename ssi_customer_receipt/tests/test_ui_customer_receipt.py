# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase - NOT HttpCase. In Odoo 14.0, plain HttpCase does not
# expose ``cls.env`` in ``setUpClass`` (its ``env`` is set per-test by
# TransactionCase.setUp instead), so the fixtures below would fail before
# any browser step ever runs.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiCustomerReceipt(HttpSavepointCase):
    """Tour tests for the ``customer_receipt`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the journal and per-tour partner/receipt fixtures.

        ``base.user_admin`` already holds every group these tours need
        (``customer_payment_user_group``/``_validator_group``/
        ``_all_group`` and ``base.group_system``) via core/module demo
        data, so no extra ``groups_id`` grant is required here.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")
        # Pre-Condition (all tours): at least one bank/cash Journal exists.
        cls.journal = cls.env["account.journal"].create(
            {
                "name": "TOUR Customer Receipt Journal",
                "type": "bank",
            }
        )

        # 01-create.md picks this partner from the many2one dropdown; no
        # receipt fixture is needed since the tour creates its own record.
        cls.env["res.partner"].create(
            {
                "name": "TOUR Customer Receipt Partner Create",
                "is_company": True,
            }
        )

        # 02-edit.md, 04-confirm.md, 10-cancel.md, 14-print.md and
        # 15-reload-template-policy.md each open an EXISTING draft record,
        # anchored in the list by its own uniquely-named partner (the
        # ``name``/document number column stays "/" for every draft
        # receipt, so it cannot anchor a row on its own).
        cls.receipt_edit = cls._create_receipt("Edit")
        cls.receipt_confirm = cls._create_receipt("Confirm")
        cls.receipt_cancel = cls._create_receipt("Cancel")
        cls.receipt_print = cls._create_receipt("Print")

        # 12-restart.md ("Reset To Draft") requires a record that is
        # already Posted or Cancelled. Reached via the ACTION METHOD
        # (not ``write({"state": ...})``) so every side effect of
        # ``action_post`` (accounting move, policy recompute) runs too.
        cls.receipt_restart = cls._create_receipt("Restart")
        cls.receipt_restart.action_post()
        cls.receipt_restart.invalidate_cache()

        # 15-reload-template-policy.md needs an observable delta: clear
        # the auto-assigned template first so the button's effect (the
        # template reappearing) cannot already be true before the click.
        cls.receipt_reload = cls._create_receipt("Reload")
        cls.receipt_reload.write({"policy_template_id": False})

    @classmethod
    def _create_receipt(cls, suffix):
        """Create one draft ``customer_receipt`` anchored by a unique partner.

        :param suffix: word appended to the fixture partner's name, used
            by the matching tour to anchor its list row via ``:contains``.
        """
        partner = cls.env["res.partner"].create(
            {
                "name": "TOUR Customer Receipt Partner %s" % suffix,
                "is_company": True,
            }
        )
        return cls.env["customer_receipt"].create(
            {
                "partner_id": partner.id,
                "journal_id": cls.journal.id,
                "amount": 100000.0,
            }
        )

    def test_create(self):
        """Run the create tour for ``customer_receipt``.

        IK: docs/customer_receipt/01-create.md
        """
        self.start_tour(
            "/web", "ssi_customer_receipt_customer_receipt_create", login="admin"
        )

    def test_edit(self):
        """Run the edit tour for ``customer_receipt``.

        IK: docs/customer_receipt/02-edit.md
        """
        self.start_tour(
            "/web", "ssi_customer_receipt_customer_receipt_edit", login="admin"
        )

    def test_confirm(self):
        """Run the confirm tour for ``customer_receipt``.

        IK: docs/customer_receipt/04-confirm.md
        """
        self.start_tour(
            "/web", "ssi_customer_receipt_customer_receipt_confirm", login="admin"
        )

    def test_cancel(self):
        """Run the cancel tour for ``customer_receipt``.

        IK: docs/customer_receipt/10-cancel.md
        """
        self.start_tour(
            "/web", "ssi_customer_receipt_customer_receipt_cancel", login="admin"
        )

    def test_restart(self):
        """Run the reset-to-draft tour for ``customer_receipt``.

        IK: docs/customer_receipt/12-restart.md
        """
        self.start_tour(
            "/web", "ssi_customer_receipt_customer_receipt_restart", login="admin"
        )

    def test_print(self):
        """Run the print tour for ``customer_receipt``.

        IK: docs/customer_receipt/14-print.md

        Stops at the wizard opening (no report is configured for this
        model yet); see the comment above the tour's registration.
        """
        self.start_tour(
            "/web", "ssi_customer_receipt_customer_receipt_print", login="admin"
        )

    def test_reload_template_policy(self):
        """Run the reload-template-policy tour for ``customer_receipt``.

        IK: docs/customer_receipt/15-reload-template-policy.md
        """
        self.start_tour(
            "/web",
            "ssi_customer_receipt_customer_receipt_reload_template_policy",
            login="admin",
        )
