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
- Minimal dependencies (`pyserial <https://pypi.python.org/pypi/pyserial>`_, `IntelHex <https://pypi.python.org/pypi/IntelHex>`_)


Quick Start
-----------

.. code-block:: console

    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install --requirement requirements.txt
    $ python -m unittest discover -s tests
    $ python -m telos.bsl -h    
    $ python -m telos.bsl /dev/ttyUSB0 --erase --program examples/blink/blink.hex


Resources
---------

#. `Crossbow TelosB Datasheet <http://www.willow.co.uk/TelosB_Datasheet.pdf>`_
#. `Memsic TelosB Datasheet <http://www.memsic.com/userfiles/files/Datasheets/WSN/telosb_datasheet.pdf>`_
#. `Telos Mote [detailed description and schematics] <http://www2.ece.ohio-state.edu/~bibyk/ee582/telosMote.pdf>`_
#. `Texas Instruments MSP430F1611 [product page] <http://www.ti.com/product/MSP430F1611/description>`_
#. `MSP430F161x Data Sheet <http://www.ti.com/lit/ds/symlink/msp430f1611.pdf>`_
#. `CC2420 [product page] <http://www.ti.com/product/CC2420>`_
#. `CC2420 Data Sheet <http://www.ti.com/lit/ds/symlink/cc2420.pdf>`_
#. `Analog Devices ADG715 [product page] <http://www.analog.com/en/products/switches-multiplexers/analog-switches-multiplexers/adg715.html>`_
#. `ADG715 Data Sheet <http://www.analog.com/media/en/technical-documentation/data-sheets/ADG714_715.pdf>`_
#. `MSP430x1xx Family User`s Guide <http://www.ti.com/lit/ug/slau049f/slau049f.pdf>`_
#. `MSP430 Assembly Language Tools v17.9.0.STS <http://www.ti.com/lit/ug/slau131q/slau131q.pdf>`_
#. `MSP430 GCC User's Guide <http://www.ti.com/lit/ug/slau646b/slau646b.pdf>`_
#. `MSP430 Embedded Application Binary Interface <http://www.ti.com/lit/an/slaa534/slaa534.pdf>`_
#. `Creating a Second-Level Bootloader for FLASH Bootloading on TMS320C6000 Platform With Code Composer Studio <http://www.ti.com/lit/an/spra999a/spra999a.pdf>`_
#. `IEEE 802.15.4 ™ and Zig Bee ™ Hardware Platform using MSP430F1612 <http://www.ti.com/lit/an/slaa264/slaa264.pdf>`_
#. `IEEE 802.15.4/ZigBee Security Research Toolkit <https://github.com/riverloopsec/killerbee>`_
#. `GoodFET by Travis Goodspeed <http://goodfet.sourceforge.net/>`_
#. `GoodFET on the TelosB, TMote Sky <http://travisgoodspeed.blogspot.com/2011/03/goodfet-on-telosb-tmote-sky.html>`_
#. `RIOT - The friendly OS for IoT <https://github.com/RIOT-OS/RIOT>`_
#. `TinyOS (an OS for embedded, wireless devices) <https://github.com/tinyos/tinyos-main>`_
#. `Intel Hex <https://en.wikipedia.org/wiki/Intel_HEX>`_


Contributing
------------

Contributions are welcome!