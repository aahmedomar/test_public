import argparse
from modules.split_qvs import split_qvs_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    prog='qvs Splitter',
    description='''This program takes in a qliksense unbuilt script and generates folders based on the tabs
    as found in qliksense, sperate the script.qvs into respective subfolder, generate exposure.yml, a source summary,
    a catalog of split assets plus a rrecreation of the qliense application provided as html report''',
    epilog='ADEPT utilities')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument("-a", "--app-name", required=False, help="app name or Qliksense Application/script name", default="my_qliksense_script")
    parser.add_argument("-i", "--input-file", required=False, help="input file from Qliksense .qvs", default="in/script.qvs")
    parser.add_argument("-o", "--output-dir", required=False, help="output directory", default="out/")
    parser.add_argument("-c", "--conf-file", required=False, help="Profiling configuration file", default="profiling.yml")
    parser.add_argument("-s", "--split-delimiter", required=False, help="qvs file split delimiter", default="///$tab")
    split_qvs_file(parser)
