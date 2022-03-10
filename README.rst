======
Stytra
======

A modular package to control stimulation and track behavior.
---------------

.. image:: https://cdn.rawgit.com/portugueslab/stytra/644a23d5/stytra/icons/stytra_logo.svg
    :scale: 50%
    :alt: Logo

.. image:: https://badge.fury.io/py/stytra.svg
    :target: https://pypi.org/project/stytra/

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3238310.svg
   :target: https://doi.org/10.5281/zenodo.3238310

.. image:: https://img.shields.io/badge/docs-0.8-yellow.svg
    :target: http://www.portugueslab.com/stytra/
    
.. image:: https://travis-ci.com/portugueslab/stytra.svg?branch=master
    :target: https://travis-ci.com/portugueslab/stytra


If you are using Stytra for your own research, please `cite us <https://doi.org/10.1371/journal.pcbi.1006699>`_!
    
Stytra is divided into independent modules which can be assembled
depending on the experimental requirements. For a complete description, look at the `full documentation <http://www.portugueslab.com/stytra>`_.

Instructions to create your first experiment in Stytra and usage examples can be found in the `example gallery <http://www.portugueslab.com/stytra/userguide/1_examples_gallery.html>`_.


Quick installation guide for FELSENBERG LAB stytra version
------------------------

1) use github desktop to download the repo

2) Open the anaconda prompt

3) create the anaconda environment with the command conda env create -f C:\Users\drosophila\Documents\GitHub\stytra_FelsenbergLab\environment.yml  (use your specific path to the file)

4) activate the environment with the command: conda activate stytra_env

5) pip install pyfirmata

6) pip install nidaqmx

7) install OUR VERSION of stytra from github, with the command: pip install git+https://github.com/BZattera/stytra_FelsenbergLab



Ths installation is done!! Now, let's test the intallation by running an example:

1) Open PyCharm

2) Go to stytra_FelsenbergLab\stytra\examples and open most_basic_example

3) Click on File>Settings>Project>Project interpreter(or, more easily, on Python 3.8 on the bottom left of the interface)

4) Click on the the setting icon

5) Click on VirtualEnvironment > Existing environment

6) Click on the ... icon with the 3 dots and navigate to .conda > envs > Stytra_env and click on python.exe

7) Select "Make available for all projects" and then click OK. The update of the environment can take some time.

8) Right click on the protocol > Run


If you run stytra while logged with your username rather than with the lab account, you will have an error message.
If this is the case, please, go to ...\stytra_FelsenbergLab\stytra\experiments and open the __init__ file. At line 96, change the dir_save.

PLEASE, DO NOT PUSH THIS CHANGE!!


For further details on the installation please consult the relative `documentation  page <http://www.portugueslab.com/stytra/userguide/0_install_guide.html>`_.
