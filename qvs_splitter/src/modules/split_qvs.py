import os
import argparse
import uuid
import re
import pandas
import csv

output_path=''

def generate_html_buttons(input_catalog):
    buttons = []
    with open(input_catalog, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tab_name = row['Tab_Name'].strip()
            button_html = f'<button class="tablinks" onclick="openCity(event, \'{tab_name}\')">{tab_name}</button>'
            buttons.append(button_html)
    return buttons

def generate_html_divs(input_catalog):
    divs = []
    divs.append('  <!-- Tab content -->')
    with open(input_catalog, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tab_name = row['Tab_Name'].strip()
            qvs_path = row['QVS_Path'].strip()
            try:
                with open(qvs_path, 'r') as qvs_file:
                    pre_content = qvs_file.read()
            except FileNotFoundError:
                pre_content = f"Error: File not found - {qvs_path}"
            except Exception as e:
                pre_content = f"Error reading file - {qvs_path}: {e}"
                
            div_html = f"""
<div id="{tab_name}" class="tabcontent">
    <h3>{tab_name}</h3>
    <pre>{pre_content}</pre>
</div>"""
            divs.append(div_html)
    return divs


def generate_report_html(input_catalog, output_html_path):
    # check if html report file exists
    script_html_exist = os.path.exists(output_html_path)
    if not script_html_exist:
        with open(output_html_path, 'a'):
            os.utime(output_html_path, None)
        print("html report file created ")
        with open(output_html_path, 'a') as html_output_file:
            html_header = '''<!DOCTYPE html>
<html>
<head>
<style>
/* Style the tab */
.tab {
  overflow: hidden;
  border: 1px solid #ccc;
  background-color: #f1f1f1;
}

/* Style the buttons that are used to open the tab content */
.tab button {
  background-color: inherit;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  transition: 0.3s;
}

/* Change background color of buttons on hover */
.tab button:hover {
  background-color: #ddd;
}

/* Create an active/current tablink class */
.tab button.active {
  background-color: #ccc;
}

/* Style the tab content */
.tabcontent {
  display: none;
  padding: 6px 12px;
  border: 1px solid #ccc;
  border-top: none;
  
}

/* Go from zero to full opacity */
@keyframes fadeEffect {
  from {opacity: 0;}
  to {opacity: 1;}
}
</style>
<h1>Referring Physician</h1>
</head>
<body>
'''
            html_output_file.write("{0}".format(html_header))
            html_output_file.write('   <div class="tab">\n')
            buttons = generate_html_buttons(input_catalog)
            html_output_file.write('\n    '.join(buttons))
            html_output_file.write('  </div>\n')
            divs = generate_html_divs(input_catalog)
            html_output_file.write('\n'.join(divs))
            report_tail = '''
  <script>
    function openCity(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}
  </script>
</body>
</html>'''
            html_output_file.write(report_tail)


def split_file_from_qliksense(script_name, input_file, split_delimiter, output_dir):
    counter = 1
    section = 'audit'
    my_tabs = {}

    """
    split_file_from_pg_dump - Split File From qliksense File
    
    """
    try:
        stats_output_dir = os.path.join(output_dir, script_name)
        stats_output_path = os.path.join(stats_output_dir, script_name+'_Catalog.csv')
        exposure_output_path = os.path.join(stats_output_dir, script_name+'_Exposure.yml')
        output_html_path = os.path.join(stats_output_dir, script_name+'_QlikSense.html')
        output_source_path = os.path.join(stats_output_dir, script_name+'_Sources.txt')
        ## check if file exists
        catalogFile_isExist = os.path.exists(stats_output_path)
        if not catalogFile_isExist:
            os.makedirs(stats_output_dir)
            print("The new directory is created for audit stats! ")
            with open(stats_output_path, 'a') as stats_output_file:
                stats_output_file.write("{0},{1},{2},{3}\n".format("Tab_Name", "QVS_Path", "SQL_Path", "Original_Tab_Name"))
        exposure_yml_exist = os.path.exists(exposure_output_path)
        if not exposure_yml_exist:
            with open(exposure_output_path, 'a'):
                os.utime(exposure_output_path, None)
            print("yaml file created ")
            with open(exposure_output_path, 'a') as exposure_output_file:
                yaml_header = '''version: 2

exposures:

  - name: {0}
    label: {0}
    type: dashboard
    maturity: high
    url: https://hea/{0}
    description: >
      {0} from QlikSense Refactor to HeA

    depends_on:\n'''.format(script_name)
                exposure_output_file.write("{0}".format(yaml_header))

        with open(input_file, 'r') as input_file:
            for line in input_file.read().split('\n'):
                if split_delimiter in line:
                    counter = counter+1

                    output_filename = line.removeprefix('///$tab ').replace(' ', '_').capitalize()
                    section = output_filename
                    output_qvs_path = os.path.join(stats_output_dir, section, 'script.qvs')
                    output_sql_path = os.path.join(stats_output_dir, section, output_filename+'.sql')
                    object_directory_isExist = os.path.exists(os.path.join(stats_output_dir, section))
                    if not object_directory_isExist:
                        # Create a new directory because if it does not exist
                        os.makedirs(os.path.join(stats_output_dir, section))
                        # create an empty sql file 
                        with open(output_sql_path, 'a') as output_sql_file:
                            sql_header = '''-- setting configurations for model
{{ 
    config( 
        enabled=true,
        materialized = 'view', 
        tags=['referring_provider', 'qvf', 'qlik_refactor', 'group1'],
        database='Cerner',
        schema='Cerner_Data',
        alias='{0}'

    ) 
}}\n'''.format(output_filename.lower())
                            output_sql_file.write("{0}".format(sql_header))

                        print("The new directory is created! "+ os.path.join(stats_output_dir, section))
                    with open(output_qvs_path, 'a') as output_file:
                        output_file.write("{0}\n".format(line))

                    with open(stats_output_path, 'a') as stats_output_file:
                        qvs_stats = output_filename+","+output_qvs_path+","+output_sql_path+","+line.removeprefix('///$tab ')
                        stats_output_file.write("{0}\n".format(qvs_stats))
                    # write to exposure.yml
                    with open(exposure_output_path, 'a') as exposure_output_file:
                        exposure_ref = "      - ref('{0}')\n".format(output_filename)
                        exposure_output_file.write("{0}".format(exposure_ref))
                    
                    my_tabs[output_filename] = "    <button class=\"tablinks\" onclick=\"openCity(event, 'Main')\">Main</button>\n"
                    print(section + ' Tab Order '+str(counter)+' started and write to file '+ output_filename)
                else:
                    #skips empty lines (change the condition if you want empty lines too)
                    if line.strip() :
                        output_qvs_path = os.path.join(stats_output_dir, section, 'script.qvs')
                        isExist = os.path.exists(os.path.join(stats_output_dir, section))
                        if not isExist:
                            # Create a new directory because it does not exist
                            os.makedirs(os.path.join(stats_output_dir, section))
                            print("The new directory is created! "+ os.path.join(stats_output_dir, section))
                        with open(output_qvs_path, 'a') as output_file:
                            output_file.write("{0}\n".format(line))
                        if 'lib:' in line: # check for lib references
                            with open(output_source_path, 'a'):
                                os.utime(output_source_path, None)
                            with open(output_source_path, 'a') as output_source_file:
                                output_source_file.write("{0},tab_sources_from ,{1}\n".format(output_filename, line.replace('[','').replace(']','').replace('FROM ','').replace('from ','')))
        generate_report_html(stats_output_path, output_html_path)        
    except Exception as e:
        print(f"something went wrong in split_file_from_qliksense: {e}")
        raise



def split_qvs_file(parser):
    """
    main - Driver program
    
    """
    try:
        args = parser.parse_args()
        app_name = args.app_name
        input_file = args.input_file
        output_directory = args.output_dir
        split_delimiter = args.split_delimiter
        split_file_from_qliksense(app_name, input_file, split_delimiter, output_directory)
        # profile_adept_results(args)
    except Exception as e:
        print(f"something went wrong in calling main driver for the program: {e}")
        raise