# Reload Template Policy — Customer Receipt

> **Module:** `ssi_customer_receipt`\
> **Model:** `customer_receipt`\
> **Menu:** Financial Accounting > Account Receivable > Customer Receipts\
> **Actor:** user in group `Settings / Technical Settings`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** None — usable regardless of status.
- **Config:** At least one active `policy.template` exists for this model, so a matching
  template can be found.
- **Access:** User is in group `Settings / Technical Settings` (`base.group_system`).
  The **Policies** tab that contains this button is only visible to this group.

## Flow

1. Open the **Financial Accounting > Account Receivable > Customer Receipts** menu.
2. Open the record whose assigned policy template should be re-evaluated.
3. On the **Policies** tab, click **Reload Template Policy**.

## Post-Condition

- **Policy Template** is recomputed and re-assigned to the highest-sequence
  `policy.template` for this model whose condition currently matches the record. This
  may change which action buttons and policy fields (`confirm_ok`, `cancel_ok`,
  `restart_ok`) are granted, without changing the record's status.
