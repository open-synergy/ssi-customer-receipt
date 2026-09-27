odoo.define("ssi_customer_receipt.customer_receipt_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Flow step 1 of every IK: "Open the Financial Accounting > Account
    // Receivable > Customer Receipts menu." Shared by all tours in this file.
    function openCustomerReceiptMenuSteps() {
        return [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Financial Accounting app",
                trigger:
                    '.o_app[data-menu-xmlid="ssi_financial_accounting.menu_root_financial_accounting"]',
            },
            {
                content: "Open the Account Receivable menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_financial_accounting.menu_account_receivable"]',
            },
            {
                content: "Open the Customer Receipts menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_customer_receipt.customer_receipt_menu"]',
            },
            {
                // Gerbang: tunggu action TUJUAN benar-benar terpasang, bukan
                // sekadar "ada list di layar" (landing action is "Invoices").
                content: "Customer Receipts list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Customer Receipts)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    // IK: docs/customer_receipt/01-create.md
    tour.register(
        "ssi_customer_receipt_customer_receipt_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(openCustomerReceiptMenuSteps(), [
            // Flow step 2 — Click the New button. (14.0: "Create")
            {
                content: "Click Create",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only.
                },
            },
            // Flow step 3 — Fill in Customer and Journal, then Amount.
            {
                content: "Select the customer",
                trigger: ".o_field_many2one[name='partner_id'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Customer Receipt Partner Create",
            },
            {
                content: "Pick the customer from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(TOUR Customer Receipt Partner Create)",
                in_modal: false,
            },
            {
                content: "Select the Journal",
                trigger: "select.o_field_widget[name='journal_id']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text TOUR Customer Receipt Journal",
            },
            {
                content: "Fill in Amount",
                trigger: ".o_field_widget[name='amount'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text 150000",
            },
            // Flow step 4 — Click Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only.
                },
            },
            // Post-Condition — A new record is created in Draft status.
            {
                content: "New receipt is created in Draft status",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='draft'].btn-primary",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );

    // IK: docs/customer_receipt/02-edit.md
    tour.register(
        "ssi_customer_receipt_customer_receipt_edit",
        {
            test: true,
            url: "/web",
        },
        [].concat(openCustomerReceiptMenuSteps(), [
            // Flow step 2 — Find and open the record to edit.
            {
                content: "Open the receipt",
                trigger:
                    ".o_data_row:contains(TOUR Customer Receipt Partner Edit) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            // 14.0 — an opened existing record is read-only; Edit first.
            {
                content: "Click the Edit button",
                trigger: ".o_form_button_edit",
            },
            {
                content: "Form is now editable",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only.
                },
            },
            // Flow step 3 — Change the required fields (Amount).
            {
                content: "Change Amount",
                trigger: ".o_field_widget[name='amount'] input",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text 999000",
            },
            // Flow step 4 — Click Save.
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },
            // Post-Condition — The record is updated with the new values.
            {
                content: "Record is saved",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );

    // IK: docs/customer_receipt/04-confirm.md
    tour.register(
        "ssi_customer_receipt_customer_receipt_confirm",
        {
            test: true,
            url: "/web",
        },
        [].concat(openCustomerReceiptMenuSteps(), [
            // Flow step 2 — Open the record to confirm.
            {
                content: "Open the receipt",
                trigger:
                    ".o_data_row:contains(TOUR Customer Receipt Partner Confirm) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            // Flow step 3 — Click the Confirm button.
            {
                content: "Click the Confirm button",
                trigger: ".o_statusbar_buttons button[name='action_post']",
                extra_trigger: ".o_form_view",
            },
            // Post-Condition — Status changes to Posted.
            {
                content: "Status is Posted",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='posted'].btn-primary",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );

    // IK: docs/customer_receipt/10-cancel.md
    tour.register(
        "ssi_customer_receipt_customer_receipt_cancel",
        {
            test: true,
            url: "/web",
        },
        [].concat(openCustomerReceiptMenuSteps(), [
            // Flow step 2 — Open the record to cancel.
            {
                content: "Open the receipt",
                trigger:
                    ".o_data_row:contains(TOUR Customer Receipt Partner Cancel) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            // Flow step 3 — Click the Cancel button.
            {
                content: "Click the Cancel button",
                trigger: ".o_statusbar_buttons button[name='action_cancel']",
                extra_trigger: ".o_form_view",
            },
            // Post-Condition — Status changes to Cancelled.
            {
                content: "Status is Cancelled",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='cancel'].btn-primary",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );

    // IK: docs/customer_receipt/12-restart.md
    tour.register(
        "ssi_customer_receipt_customer_receipt_restart",
        {
            test: true,
            url: "/web",
        },
        [].concat(openCustomerReceiptMenuSteps(), [
            // Flow step 2 — Open the record to reset (already Posted).
            {
                content: "Open the receipt",
                trigger:
                    ".o_data_row:contains(TOUR Customer Receipt Partner Restart) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            // Flow step 3 — Click the Reset To Draft button.
            {
                content: "Click the Reset To Draft button",
                trigger: ".o_statusbar_buttons button[name='action_draft']",
                extra_trigger: ".o_form_view",
            },
            // Post-Condition — Status returns to Draft.
            {
                content: "Status is back to Draft",
                trigger:
                    ".o_statusbar_status .o_arrow_button[data-value='draft'].btn-primary",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );

    // IK: docs/customer_receipt/14-print.md
    //
    // The Print button opens the generic "Select Report To Print" wizard
    // (ssi_print_mixin). No print_document_type/report is configured for
    // the `customer_receipt` model in this repo yet, so the wizard offers
    // no report to pick (see the IK's Pre-Condition note). Per the tour
    // skill's rule on actions with no reachable completion signal, this
    // tour only proves the button opens the wizard, then discards it —
    // it does NOT select a report or click the wizard's own Print button.
    tour.register(
        "ssi_customer_receipt_customer_receipt_print",
        {
            test: true,
            url: "/web",
        },
        [].concat(openCustomerReceiptMenuSteps(), [
            // Flow step 2 — Open the receipt to print.
            {
                content: "Open the receipt",
                trigger:
                    ".o_data_row:contains(TOUR Customer Receipt Partner Print) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            // Flow step 3 — Click the Print button.
            {
                content: "Click the Print button",
                trigger: ".o_statusbar_buttons button:enabled:contains(Print)",
                extra_trigger: ".o_form_view",
            },
            {
                // Waiting for the modal to appear: `in_modal: false` keeps the
                // search global instead of scoped to a (not-yet-existing)
                // modal — see patterns-dialogs-and-wizards.md "Perkecualian
                // ambang-masuk".
                content: "The Select Report To Print wizard is displayed",
                trigger: ".modal-title:contains(Select Report To Print)",
                in_modal: false,
                run: function () {
                    // Assertion only.
                },
            },
            // Deliberately stop here — see the comment above the register()
            // call. Discard the wizard instead of completing it.
            {
                content: "Discard the wizard",
                trigger: ".modal-footer button:contains(Cancel)",
            },
            {
                content: "Wizard is closed",
                trigger: "body:not(:has(.modal))",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );

    // IK: docs/customer_receipt/15-reload-template-policy.md
    tour.register(
        "ssi_customer_receipt_customer_receipt_reload_template_policy",
        {
            test: true,
            url: "/web",
        },
        [].concat(openCustomerReceiptMenuSteps(), [
            // Flow step 2 — Open the record whose policy should be re-evaluated.
            {
                content: "Open the receipt",
                trigger:
                    ".o_data_row:contains(TOUR Customer Receipt Partner Reload) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
            // Flow step 3 — On the Policies tab, click Reload Template Policy.
            {
                content: "Open the Policies tab",
                trigger: ".o_notebook .nav-link:contains(Policies)",
                extra_trigger: ".o_form_view",
            },
            {
                content: "Click Reload Template Policy",
                trigger: ".o_form_view button[name='action_reload_policy_template']",
            },
            // Post-Condition — Policy Template is recomputed and reassigned.
            // The fixture clears policy_template_id beforehand (setUpClass),
            // so this text is guaranteed absent before the click.
            {
                content: "Policy Template is reassigned",
                trigger:
                    ".o_field_widget[name='policy_template_id']:contains(Customer Receipt: Standard)",
                run: function () {
                    // Assertion only.
                },
            },
        ])
    );
});
