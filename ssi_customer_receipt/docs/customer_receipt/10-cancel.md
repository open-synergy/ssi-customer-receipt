# Cancel Customer Receipt

> **Module:** `ssi_customer_receipt`\
> **Model:** `customer_receipt`\
> **Menu:** Financial Accounting > Account Receivable > Customer Receipts\
> **Actor:** user in group `Customer Payment / Validator`\
> **State:** `draft` → `cancel`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for this model grants `cancel_ok` to the
  actor's group while the record is in **Draft** status.
- **Access:** User is in group `Customer Payment / Validator`.

## Flow

1. Open the **Financial Accounting > Account Receivable > Customer Receipts** menu.
2. Open the record to cancel.
3. Click the **Cancel** button.

## Post-Condition

- Status changes to **Cancelled**.
