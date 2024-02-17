12:27PM
Problem Statement: 
Choosing the new kea-dhcp feature in opnsense 24.1 does not automatically migrate 
the isc-dhcp static leases information to kea-dhcp. The intent of the python script 
is to patch an existing opnsense config already Gui configured with one existing kea-dhcp
static lease device. Re-use of the identified <subnet> uuid is required 
in gh_static_lease4.py to create the reservations. 
Hopefully users will find it useful and prevent manual Gui data entry.

My Use Case:
Currently, I have not moved my pfsense isc-dhcp static leases information
to opnsense isc-dhcp. I have been dreading how I would manually enter all 
40+ devices: ip, mac address, hostname and description. Below is how I solved this
migration dilemma to opnsense.

Prerequisites:
Python Code developed on a Windons and tested on W11 directories. (Python 3.12)
Basic Python knowledge
Optional: Notepad ++


Overview of Processing:
This python script converts a small section of the pfsense config: isc-dhcp static lease(.xml)
into an opnsense kea-dhcp static lease(.xml)format. A sample gh_pfsense_isc_dhcp_data.xml 
is provided as a template and available to add your pfsense isc-dhcp clients. 
The input .xml will be converted into a json array of static release objects 
which is then further converted into a new updated section of opnsense: kea-dhcp 
static lease delimited by <reservations>. For every device in kea-dhcp, 
the python script will generate a new random uuid for every device and re-uses 
the user's <subnet> uuid.

See below:

      </reservations>
          <reservation uuid="6a688941-02f8-46aa-abc6-8121fa434809">
            <subnet>7046c7cb-a9fb-4a50-8a49-3b6e77d42809</subnet>
            <ip_address>192.168.1.100</ip_address>
            <hw_address>90:a1:b1:c1:d1:e11</hw_address>
            <hostname/>
            <description/>
       </reservations>
	   
	   
Sample pfsense xml Data Test Run:	   
Copy gh_static_lease4.py and gh_pfsense_isc_dhcp_data.xml into the same directory.

>>  python3 gh_static_lease4.py

creates 
gh_kea_dhcp_data.json
gh_static_lease3_converted_to_opnsense.xml


Adding the patch to the opnsense config file:
In opnsense GUI, create and add a client in the kea-dhcp reservation tab and apply save.
You have just created an uuid for the subnet. Save the config backup, open the config
and identify your <subnet> uuid  </subnet>. 
Edit the gh_static_lease4.py and add ur new subnet uuid. 
In the same directory  run gh_static_lease4.py with your gh_pfsense_isc_dhcp_data.xml present.
The *.py script will generates a new kea-dhcp format - see the newly created  .xml in
gh_static_lease3_converted_to_opnsense.xml.
