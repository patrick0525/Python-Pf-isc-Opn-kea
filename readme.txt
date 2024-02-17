Problem Statement: 
Choosing the new kea-dhcp feature in opnsense 24.1 does not automatically convert
the isc-dhcp static leases to kea-dhcp. The intetened output is used to patch an existing opnsense kea-dhcp 
with one static lease device.

Currently,I have not moved my pfsense isc-dhcp leases to opnsense isc-dhcp. I was dreading how
I would manually enter all 40+ devices: ip, mac address, hostname and desription.
Below is how I solved this migration dilemma to opnsense.

This python script converts a small section of the pfsense config: isc-dhcp static lease(.xml)
into an opnsense kea-dhcp static lease(.xml) format. A sample gh_pfsense_isc_dhcp_data.xml is provided as a template
to add your pfsense isc-dhcp clients. The input  xml  will be coverted into a json array of static release objects 
which is then further converted into a new updated section of opnsense: kea-dhcp 
static lease delimited by <reservations>. For every device in kea-dhcp, the python script will generates a
new radndom uuid for every device and re-use the subnet uuid.

See below:

      </reservations>
          <reservation uuid="6a688941-02f8-46aa-abc6-8121fa434809">
            <subnet>7046c7cb-a9fb-4a50-8a49-3b6e77d42809</subnet>
            <ip_address>192.168.1.100</ip_address>
            <hw_address>90:a1:b1:c1:d1:e11</hw_address>
            <hostname/>
            <description/>
       </reservations>
	   
	   
=====	   
Test Run with sample pfsense xml data
In the same directory run gh_static_lease4.py with your gh_pfsense_isc_dhcp_data.xml present.

>>  python3 gh_static_lease4.py

creates 
gh_kea_dhcp_data.json
gh_static_lease3_converted_to_opnsense.xml
=======


In opnsense GUI, create and add a client in the kea-dhcp reservations and apply save.
You have just created an uuid for the subnet. Save the config backup,open the config
and identify yout <subnet> uuid  </subnet>. 
Edit gh_static_lease4.py and add ur new subnet uuid. 
In the same directory  run gh_static_lease4.py with your gh_pfsense_isc_dhcp_data.xml present.
The *.py script will generates a new kea-dhcp format - see the newlly created  gh_static_lease3_converted_to_opnsense.xml

To complete the opnsense config file, cut and paste the entire section
into the targetd opnsense config file delimited by <reservations>.