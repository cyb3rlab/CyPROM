# CyPROM: Scenario Progression Management for Cybersecurity Training

CyPROM is a scenario progression management system that was created with the goal of making possible advanced cybersecurity training activities that take place in dynamic environments in which all three training aspects can be put into practice, attack, forensics, and defense. CyPROM was developed initially by the Cyber Range Organization and Design (CROND) NEC-endowed chair at the Japan Advanced Institute of Science and Technology (JAIST), Ishikawa, Japan, and development currently continues at the Cybersecurity Lab at JAIST.

An overview of CyPROM is provided in the figure below. Based on training scenarios and target information provided by instructors, the management module of CyPROM will initiate a set of processes that drive the execution of those scenarios in the training environment. Each scenario driver uses a "Trigger-Action-Branching" mechanism that is executed independently for each participant, so that scenario progression takes place in accordance with their individual actions.

![CyPROM Overview](https://github.com/crond-jaist/cyprom/blob/master/cyprom_overview.png)

Next we provide brief information on how to setup and use CyPROM. For details, including training scenario representation, please refer to the User Guide made available on the [releases](https://github.com/crond-jaist/cyprom/releases) page.


## Setup

CyPROM has been developed mainly on the Ubuntu 18.04 LTS operating system; other OSes may work, but have not been thoroughly tested. Although CyPROM can interface with cyber ranges created in other manners, we recommend its use together with the [CyTrONE framework](https://github.com/crond-jaist/cytrone) and its components, which you may want to install in advance.

In order to setup CyPROM it is enough to uncompress the archive containing the latest release into your directory of choice (for instance, your home directory) on the host on which you intend to use it. In case CyPROM is used together with CyRIS, we suggest using the same host for both of them. The only requirement is that CyPROM can access the cyber range environments that will be used during the training activity.

CyPROM is implemented in Python, and it requires several packages to run. We provide the list of requirements in a file that can be used to install the included packages via the following command from the `cyprom/` directory:

`$ sudo pip3 install -r requirements.txt`

In addition, some of the CyPROM actions, such as `scan_open_ports`, require the command `nmap` to be available on the machine on which the action is run, typically a cyber range host. Therefore, you should make sure the `nmap` command is installed in the cyber range before attempting to use such actions.

Although the default settings should work fine in most case, before using CyPROM for the first time, we suggest that you check the content of the configuration file `config` that is located in the top directory of the CyPROM installation.

We have also created a sample web site that can be used to demonstrate the new functionality of CyPROM; the necessary files are provided as an additional asset in the GitHub release, named `cyweb.tgz`. Please refer to the README file in that archive for installation details.


## Quick Start

In order to run CyPROM with the default settings, use the following command:

`$ ./cyprom.py`

This will execute a basic training scenario that emulates a sample training activity with two scenarios using only harmless test actions.

To get used to the training scenario representation syntax, we suggest examining the examples provided in the directory `examples/`, and also consulting the user guide. In particular, a cyber range must be created, and the target information file needs to be modified accordingly, in order to run an actual training activity.


## References

For a research background regarding CyPROM, please refer to the following documents:

* R. Beuran, T. Inoue, Y. Tan, Y. Shinoda, "Realistic Cybersecurity Training via Scenario Progression Management", IEEE European Symposium on Security and Privacy Workshops (EuroS&PW 2019), Workshop on Cyber Range Applications and Technologies (CACOE'19), Stockholm, Sweden, June 20, 2019, pp. 67-76.

* Q. V. Ngo, "Hands-on Training for Mitigating Web Application Vulnerabilities", master’s thesis, Japan Advanced Institute of Science and Technology, September 2023. https://dspace.jaist.ac.jp/dspace/handle/10119/18734

For a list of contributors to this project, see the file CONTRIBUTORS included in the distribution.
