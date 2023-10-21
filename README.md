# tkinter-used-port-scanning-tool

Table of Contents:
- [Introduction](#Introduction)
- [Features](#Features)
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Usage](#Usage)
- [Screenshots](#Screenshots)
- [Lisence](#Lisence)



Introduction
> This is a Python-based Port Scanner tool with a graphical user interface (GUI) created using Tkinter. It allows users to quickly and easily scan for open ports on a target host. Port scanning is a crucial step in assessing the security of a network, and this tool makes the process more user-friendly.
The tool utilizes Python's built-in socket library to establish connections with the specified ports on the target host and determine their status (open or closed).


Features
> User-friendly GUI with Tkinter for easy navigation and interaction.
> Scan a range of ports on a target host.
> Display scan results with clear indications of open and closed ports.
> Save scan results to a text file for future reference.
> Fast and efficient port scanning.


Requirements
To run this Port Scanner, you will need:
> Python 3.x (https://www.python.org/)
> Tkinter (usually included with Python)
> Internet connection (for scanning external hosts)


Installation
> Clone or download this repository to your local machine.
> Install the required dependencies by running the following command:
   pip install -r requirements.txt
> Run the tool using the following command:
   python port_scanner.py
> Use the graphical interface to enter the target IP address or host name and specify the ports to scan.
> Click the "Scan" button to start the scan.
> Review the results on the interface or export them to a text file.


Usage
> Target IP/Host: Enter the IP address or host name of the target you want to scan.
> Port Range: Specify the range of ports you want to scan (e.g., 1-1024).
> Select Scan Type: Choose between "Quick Scan" and "Full Scan."
> Scan: Click the "Scan" button to start the scan.


Scan Results
> The tool will display the scan results in the graphical interface, showing which ports are open and closed. You can also export the results to a text file for further analysis.

Contribution
> We welcome contributions from the community. If you'd like to enhance the functionality, fix issues, or add new features to this Port Scanning Tool, please feel free to fork the repository, make your changes, and submit a pull request.

License
> This Port Scanning Tool is open-source and released under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.

Support
> If you encounter any issues or have questions, please open an issue in this repository, and our community or maintainers will assist you.

Happy scanning!
