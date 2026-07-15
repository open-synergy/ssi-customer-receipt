.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================================
Customer Receipt + Operating Unit
=================================

This is a glue module that adds Operating Unit support to the
``customer_receipt`` model. Users can pick an operating unit on the customer
receipt tree, search, and form views. The operating unit set on the receipt is
shared with its delegated ``account.move`` and is automatically propagated to
every ``account.move.line`` generated when the receipt is posted, keeping the
resulting journal entries scoped to the same operating unit.


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/open-synergy/ssi-customer-receipt/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.


Credits
=======

Contributors
------------

* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by the PT. Simetri Sinergi Indonesia.
