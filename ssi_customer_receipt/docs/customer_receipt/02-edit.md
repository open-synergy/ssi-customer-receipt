# Edit Customer Receipt

> **Module:** `ssi_customer_receipt`\
> **Model:** `customer_receipt`\
> **Menu:** Financial Accounting > Account Receivable > Customer Receipts\
> **Actor:** user in group `Customer Payment / User`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Access:** User is in group `Customer Payment / User`.

## Flow

1. Open the **Financial Accounting > Account Receivable > Customer Receipts** menu.
2. Find and open the record to edit.
3. Change the required fields (**Customer**, **Journal**, **Payment Method**,
   **Recipient Bank Account**, **Destination Account**, **Receipt Date**, **Amount**,
   **Currency**, **Memo**) as needed.
4. Click **Save**.

## Post-Condition

- The record is updated with the new values.
