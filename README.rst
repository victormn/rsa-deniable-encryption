RSA Deniable Encryption
=======================

.. image:: https://travis-ci.org/victormn/rsa-deniable-encryption.svg?branch=master
    :target: https://travis-ci.org/victormn/rsa-deniable-encryption
.. image:: https://coveralls.io/repos/github/victormn/rsa-deniable-encryption/badge.svg
    :target: https://coveralls.io/github/victormn/rsa-deniable-encryption

This project create a RSA cryptosystem with deniability. Three scripts was created:

- Generates RSA key pair
- Encrypt/Decrypt a message
- Find a new secret key that can decrypt a given message from a given cipher generated using a given secret key

**Example:**

.. code-block:: bash

    m1 = message 1                     
    m2 = message 2                     
    c = cipher                         
    pk = public key                    
    sk1 = secret key 1                 
    sk2 = secret key 2                 
    E() = encryption algorithm         
    D() = decryption algorithm         
    NSK() = new secret key algorithm  

.. code-block:: bash

   c = E(m1, pk)                                    
   m1 = D(c, sk1)                       
   sk2 = NSK(c, sk1, m2)              
   m2 = D(c, sk2)                   	


.. contents::

.. section-numbering::

Quickstart
----------

``make init`` to install all Python dependencies

``make build`` to build the project

(or just use ``make`` to install all Python dependencies and build the project)

How to use
----------

``deniablekeys [-p KEY_PATH]`` to generate a RSA key pair in PEM format, saving in **publickey.pem** and **secretkey.pem**.

``deniablersa  [-e | -d] key_path`` to encrypt ``-e`` or decrypt ``-d`` a given stdin input. To encrypt use a public key and to decrypt use a secret key.

``deniablecollision cipher_path message_path secretkey_path`` to get a collision secret key of given message, using a given cipher and secret key.

Dependencies
------------

``python3`` use the official `website <https://www.python.org/download/releases/3.0/>`_ to download python3

``python3-pip`` use the official `website <https://pypi.python.org/pypi/pip>`_ or the command:``apt-get install python3-pip``

Contact
-------

To contact the author, create a `issue <https://github.com/victormn/rsa-deniable-encryption/issues>`_ or see the `setup.py <https://github.com/victormn/rsa-deniable-encryption/blob/master/setup.py>`_ file.

ReadTheDocs
-----------

*Coming soon...*