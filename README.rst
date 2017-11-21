Telos
=====

What?
-----

Telos is a Python 3 tool box for the MSP430 based Crossbow Telos (Rev. B). Telos includes utilities like a lightweight Bootstrap Loader (BSL) for easily programming target boards without expensive hardware.

Why?
----


Features
--------
- Written for Python 3.6
- Minimal dependencies (`pyserial <https://pypi.python.org/pypi/pyserial>`_)


Quick Start
-----------

.. code-block:: console

    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python -m unittest discover -s tests
    $ python -i -m telos.bsl

Resources
---------

#. `Crossbow TelosB Datasheet <http://www.willow.co.uk/TelosB_Datasheet.pdf>`_
#. `Memsic TelosB Datasheet <http://www.memsic.com/userfiles/files/Datasheets/WSN/telosb_datasheet.pdf>`_
#. `Telos Mote [detailed description and schematics] <http://www2.ece.ohio-state.edu/~bibyk/ee582/telosMote.pdf>`_
#. `Texas Instruments MSP430F1611 [product page] <http://www.ti.com/product/MSP430F1611/description>`_
#. `MSP430 Embedded Application Binary Interface <http://www.ti.com/lit/an/slaa534/slaa534.pdf>`_
#. `Analog Devices ADG715 [product page] <http://www.analog.com/en/products/switches-multiplexers/analog-switches-multiplexers/adg715.html>`_
#. `ADG715 Data Sheet <http://www.analog.com/media/en/technical-documentation/data-sheets/ADG714_715.pdf>`_
#. `MSP430F161x Data Sheet <http://www.ti.com/lit/ds/symlink/msp430f1611.pdf>`_
#. `MSP430x1xx Family User`s Guide <http://www.ti.com/lit/ug/slau049f/slau049f.pdf>`_
#. `IEEE 802.15.4 ™ and Zig B ee ™ Hardware Platform using MSP430F1612 <http://www.ti.com/lit/an/slaa264/slaa264.pdf>`_
#. `MSP430 Assembly Language Tools v17.9.0.STS <http://www.ti.com/lit/ug/slau131q/slau131q.pdf>`_
#. `GoodFET on the TelosB, TMote Sky <http://travisgoodspeed.blogspot.com/2011/03/goodfet-on-telosb-tmote-sky.html>`_
#. `GoodFET by Travis Goodspeed <http://goodfet.sourceforge.net/>`_
#. `IEEE 802.15.4/ZigBee Security Research Toolkit <https://github.com/riverloopsec/killerbee>`_


Contributing
------------

Contributions are welcome!