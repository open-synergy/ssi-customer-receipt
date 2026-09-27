# Reset to Draft Customer Receipt

> **Module:** `ssi_customer_receipt`\
> **Model:** `customer_receipt`\
> **Menu:** Financial Accounting > Account Receivable > Customer Receipts\
> **Actor:** user in group `Customer Payment / Validator`\
> **State:** `posted` | `cancel` → `draft`\
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Posted** or **Cancelled**.
- **Config:** An active `policy.template` for this model grants `restart_ok` to the
  actor's group whenever the record is not in **Draft** status.
- **Access:** User is in group `Customer Payment / Validator`.

## Flow

1. Open the **Financial Accounting > Account Receivable > Customer Receipts** menu.
2. Open the record to reset.
3. Click the **Reset To Draft** button.

## Post-Condition

- Status returns to **Draft**.
