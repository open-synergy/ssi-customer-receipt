# Confirm Customer Receipt

> **Module:** `ssi_customer_receipt`\
> **Model:** `customer_receipt`\
> **Menu:** Financial Accounting > Account Receivable > Customer Receipts\
> **Actor:** user in group `Customer Payment / Validator`\
> **State:** `draft` → `posted`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for this model grants `confirm_ok` to the
  actor's group while the record is in **Draft** status.
- **Access:** User is in group `Customer Payment / Validator`.

## Flow

1. Open the **Financial Accounting > Account Receivable > Customer Receipts** menu.
2. Open the record to confirm.
3. Click the **Confirm** button.

## Post-Condition

- Status changes to **Posted**.
- The related journal entry is posted.
