# PyDynamic
Python package for the analysis of dynamic measurements

The goal of this package is to provide a starting point for users in metrology and related areas who deal with time-dependent, i.e. *dynamic*, measurements.
The software is part of a joint research project of the national metrology institutes from Germany and the UK, i.e. [Physikalisch-Technische Bundesanstalt](http://www.ptb.de/cms/en.html)
and the [National Physical Laboratory](http://www.npl.co.uk).

Note that currently this software is written in Python 2.7. The next release will be written in Python 3.5 to ensure future compatibility.

### Installation
Since this software is still under active development, we highly recommend to not download the zip-file of the current version only. Instead, we recommend using [Github Desktop](https://desktop.github.com) or any other git-compatible version control software and cloning the repository (https://github.com/eichstaedtPTB/PyDynamic.git). In this way, any updates to the software will be highlighted in the version control software and can be applied very easily.

If you have downloaded this software, we would be very thankful for letting us know. You may, for instance, drop an email to one of the authors (e.g. [Sascha Eichstädt](mailto:sascha.eichstaedt@ptb.de) or [Ian Smith](mailto:ian.smith@npl.co.uk) )

### Roadmap - next steps

1. Transfer the current code basis to Python 3.5 for future compatibility.
2. Extend the exisiting examples using improved signals and systems.
3. Merge [GUM2DFT](https://www.ptb.de/cms/en/ptb/fachabteilungen/abt8/fb-84/ag-842/dynamischemessungen-842/download-gum2dft.html) into PyDynamic.
4. Extend the code to more advanced noise processes and uncertainty evaluation.
5. Add IPython notebooks as a way of documentation.
6. Provide graphical user interfaces for specific use cases (Any suggestions? Let us know!)

##### Acknowledgement
This work is part of the Joint Support for Impact project [14SIP08](http://mathmet.org/projects/14SIP08) of the European Metrology Programme for Innovation and Research (EMPIR). 
The [EMPIR](http://msu.euramet.org) is jointly funded by the EMPIR participating countries within EURAMET and the European Union.

##### Disclaimer
This software was developed at Physikalisch-Technische Bundesanstalt (PTB) and National Physical Laboratory (NPL). 
The software is made available "as is" free of cost. PTB and NPL assume no responsibility whatsoever for its use by other parties, 
and makes no guarantees, expressed or implied, about its quality, reliability, safety, suitability or any other characteristic. 
In no event will PTB and NPL be liable for any direct, indirect or consequential damage arising in connection with the use of this software.
