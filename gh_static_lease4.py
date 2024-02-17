# Initial Input gh_pfsense_isc_dhcp_data.xml
# Final Output gh_static_lease3_converted_to_opnsense.xml
# Module  are provided by python use pip to install 
import json
import uuid
import os
import xmltodict
 
# Convert pfsense xml to json array of ojects
# Input  gh_pfsense_isc_dhcp_data.xml
# Output gh_kea_dhcp_data.json
def pfsense_xml_to_json(path,input,output):

    # open the input xml file and read
    # data into a python dictionary 
    # using xmltodict module

    input_file = os.path.join(path,input)
    print("Convert xml ", input_file, "to json objects")
    print("Output needs to be a single json array containing json objects")
    print("Format: [{object1},{object2},{object3}]")

    isExist = os.path.exists(input_file)
    print ("The input file exists:", isExist)

    with open (input_file) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())	
    # Clean-up the nested array 
    # and get to the dhcpd value
    long_list = (list(data_dict.values()))
    # print(long_list)
    # print("\n")

    # get to staticmap
    short_list = long_list[0]
    # print(short_list)
    # print("\n\n")

    # get to staticmap(key): json objects (values) 
    inner_list = short_list['staticmap']
    print("\n")
    # print(inner_list)


    # Convert the dictionary to a json string with indentation 
    json_str = json.dumps(inner_list, indent=4)
    print (json_str)


    # Specify the path to the output file 
    #output_file = rf'C:\Users\patri\Documents\python\GitHub\gh_kea_dhcp_data.json'
    output_file = os.path.join(path,output)
    # Save the json representation of the structure 
    with open(output_file, 'w') as f: 
        # Write the JSON string to the file 
        f.write(json_str) 
    # Print a confirmation message with the output file path 
    print("\njson saved to", output_file,"\n")

# Convert json array of ojects to opnsense xml
# Input  gh_kea_dhcp_data.json
# Output gh_static_lease3_converted_to_opnsense.xml
def json_to_opnsense_xml(path,input,output):

    # when json null appears it is a None
    null = None
    # input_file = open(rf'C:\Users\patri\Documents\python\GitHub\gh_kea_dhcp_data.json', 'r')
    file = os.path.join(path,input)
    input_file = open(file, 'r')
    json_decode = json.load(input_file)
    
    # output_file = open(r'C:\Users\patri\Documents\python\GitHub\gh_static_lease3_converted_to_opnsense.xml', 'w')
    output_file = os.path.join(path,output)
    output_file = open(output_file, 'w')
    result = []
    for item in json_decode:
        my_dict={}
        my_dict['mac']=item.get('mac')
        my_dict['ipaddr']=item.get('ipaddr')
        my_dict['hostname']=item.get('hostname')
        my_dict['descr']=item.get('descr')
    
        u = str(uuid.uuid4())
        #print (u)
    
        str1 =          "<reservations>\n"
    
        str2 =          "<reservation uuid=\""
        str2a =         "\">\n"
    
        #Identify subnet use static uuid
        str3 =          "<subnet>7046c7cb-a9fb-4a50-8a49-3b6e77d42809</subnet>\n"
    
        str4 =          "<ip_address>"
        str4a =         "</ip_address>\n"
    
        str5 =          "<hw_address>" 
        str5a =         "</hw_address>\n"
    
        str6 =          "<hostname>"
        str6a =         "</hostname>\n"
    
        str7 =          "<description>" 
        str7a =         "</description>\n"
    
        str8 =          "</reservation>\n"
        str9 =          "</reservations>\n"
    
        # write to file by looping
    
        #output_file.writelines(f"{'':>7}{str1}")

        output_file.writelines(f"{'':>10}{str2}{u}{str2a}")
        output_file.writelines(f"{'':>12}{str3}")
        output_file.writelines(f"{'':>12}{str4}{my_dict['ipaddr']}{str4a}")
        output_file.writelines(f"{'':>12}{str5}{my_dict['mac']}{str5a}")
    
        if (my_dict['hostname']== null):
            output_file.writelines(f"{'':>12}{str6}{str6a}")
        else:
            output_file.writelines(f"{'':>12}{str6}{my_dict['hostname']}{str6a}")
    
        if (my_dict['descr']== null):  
            output_file.writelines(f"{'':>12}{str7}{'EMPTY'}{str7a}")  
        else:
            output_file.writelines(f"{'':>12}{str7}{my_dict['descr']}{str7a}")
        
        output_file.writelines(f"{'':>10}{str8}")
    
        #output_file.writelines(f"{'':>7}{str9}")

    # Close file
    output_file.close()

    # Checking if the data is written to file or not
    # display_output_file = rf'C:\Users\patri\Documents\python\GitHub\gh_static_lease3_converted_to_opnsense.xml'
    # output_file = open(r'C:\Users\patri\Documents\python\GitHub\gh_static_lease3_converted_to_opnsense.xml', 'r')
    display_output_file = os.path.join(path,output)
    output_file = open(display_output_file, 'r')
    
    print(output_file.read())
    output_file.close() 

    # Print a confirmation message with the output file path 
    print("Opnsense kea-dhcp xml saved to",display_output_file)



# Change working path
os.chdir(rf'C:\\Users\\patri\\Documents\\python\\GitHub')
entry_path = (os.getcwd())

# Read pfsense config xml
input_file  = "gh_pfsense_isc_dhcp_data.xml"
output_file = "gh_kea_dhcp_data.json"
print("pfsense_xml_to_json\n[Path]                             Input File                  Output file")
print(entry_path,input_file,output_file,"\n")
pfsense_xml_to_json(entry_path,input_file,output_file)

# Output opnsense config xml
input_file  = "gh_kea_dhcp_data.json"
output_file = "gh_static_lease3_converted_to_opnsense.xml"
print("json_to_opnsense_xml\n[Path]                              Input File                  Output file")
print(entry_path,input_file,output_file,"\n")
json_to_opnsense_xml(entry_path,input_file,output_file)