# Create Customer Receipt

> **Module:** `ssi_customer_receipt`\
> **Model:** `customer_receipt`\
> **Menu:** Financial Accounting > Account Receivable > Customer Receipts\
> **Actor:** user in group `Customer Payment / User`\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** At least one bank or cash **Journal** is configured for the company.
- **Config:** An active `policy.template` for this model exists (installed by the
  module), so `confirm_ok`/`cancel_ok`/`restart_ok` can later be granted to the actor's
  group.
- **Access:** User is in group `Customer Payment / User`.

## Flow

1. Open the **Financial Accounting > Account Receivable > Customer Receipts** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the fields:
   - **Customer**: Select the customer the receipt is registered for.
   - **Journal**: Select the bank or cash journal used to receive the payment.
   - **Payment Method**: Automatically filled from **Journal**. Change if needed. Hidden
     when the journal only has one available method.
   - **Recipient Bank Account**: Automatically filled if the selected payment method
     requires a bank account. Hidden otherwise.
   - **Destination Account**: Automatically filled from **Journal**. Change if needed.
   - **Receipt Date**: Defaults to today. Change if needed.
   - **Amount**: Enter the amount received.
   - **Currency**: Automatically filled from the company currency (only shown when
     multi-currency is enabled). Change if needed.
   - **Memo**: Optional free-text reference.
4. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
