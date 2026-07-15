# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CustomerReceipt(models.Model):
    """Dedicated model for Customer Receipt on the shared account_payment table.

    ``account.payment`` is used for both customer receipts and vendor payments,
    distinguished only by ``payment_type``/``partner_type``. Because access
    rights and record rules are per-model, it is not possible to grant a user
    access to customer receipts only without also exposing vendor payments.

    This model exposes **only** customer receipts. It inherits every field and
    method of ``account.payment`` and reuses the very same physical table
    (``_table = "account_payment"``), so no new table nor column is created.
    A dedicated model lets ACL and record rules target customer receipts
    independently from vendor payments.

    Do NOT add stored fields here: a stored field would add a column to the
    real ``account_payment`` table. Only override existing field attributes,
    add methods, or add non-stored/related fields. Extra data belongs on
    ``account.payment`` in ``ssi_financial_accounting``.
    """

    _name = "customer_receipt"
    _inherit = "account.payment"
    _table = "account_payment"
    _description = "Customer Receipt"

    payment_type = fields.Selection(
        default="inbound",
    )
    partner_type = fields.Selection(
        default="customer",
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals["payment_type"] = "inbound"
            vals["partner_type"] = "customer"
        # account.payment is delegated (_inherits) to account.move, so ORM create
        # materializes account.move + account.move.line under the caller's rights.
        # Elevate so a user holding only `customer_receipt` ACL can create it.
        # sudo() in Odoo 14 keeps env.uid = triggering user -> create_uid stays correct.
        records = super(CustomerReceipt, self.sudo()).create(vals_list)
        return records.with_env(self.env)

    def write(self, vals):
        # write triggers _synchronize_to_moves, touching account.move/move.line.
        return super(CustomerReceipt, self.sudo()).write(vals)

    def action_post(self):
        # action_post calls move_id._post(), which needs account.move rights.
        return super(CustomerReceipt, self.sudo()).action_post()

    def action_draft(self):
        # action_draft calls move_id.button_draft(), which needs account.move rights.
        return super(CustomerReceipt, self.sudo()).action_draft()

    def action_cancel(self):
        # action_cancel calls move_id.button_cancel(), which needs account.move rights.
        return super(CustomerReceipt, self.sudo()).action_cancel()
