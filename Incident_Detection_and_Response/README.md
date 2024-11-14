🔍 Incident Detection and Response Report - Windows-Based System 🖥️

📄 Executive Summary

This report details the detection, investigation, and remediation of a suspected security incident involving unauthorised remote access on a Windows-based system. Through a meticulous investigation, the team leveraged Microsoft Sysinternals tools—such as TCPView, Process Explorer, and Autoruns—to uncover and neutralise a potentially malicious application, putty.exe, which had established an unauthorised remote connection.

🔍 Key Findings

1️⃣ Detection of Suspicious Process - putty.exe 🕵️

Anomalous activity was detected via TCPView, revealing an active connection by putty.exe to an unknown remote IP address. This indicated a potential compromise of the system and a threat to the larger network.

2️⃣ Persistence Mechanism 🔧

Using Process Explorer and Autoruns, the investigation traced putty.exe to explorer.exe, suggesting it was likely downloaded via Internet Explorer. A suspicious autorun entry labeled “secure” was discovered in the Windows registry, enabling automatic execution of the malicious application upon system startup.

3️⃣ Containment and Remediation 🚫

Once confirmed as malicious, immediate containment actions were taken:

📌Disconnected the network to prevent further spread.

📌Terminated the active connection and removed putty.exe along with related registry entries.

📌Hardened the system by activating firewall policies, applying system updates, and installing antivirus software.

🔐 Recommendations for Enhanced Security

The report concludes with a set of proactive security measures to mitigate future incidents:

1️⃣ Enhanced Network Monitoring and Alerts 📡

Improve visibility into network activity to identify anomalies quickly.

2️⃣ Restricted Administrative Privileges 🔒

Limit access to essential personnel only, reducing potential attack vectors.

3️⃣ Enabled Windows Defender and Firewall Policies 🛡️

Strengthen default protections and minimise the risk of unauthorised access.

4️⃣ Enhanced Email and Download Filtering ✉️

Filter potentially malicious content to reduce the likelihood of malware infiltration.
