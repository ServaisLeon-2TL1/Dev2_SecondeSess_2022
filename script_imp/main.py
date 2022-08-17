from script_importation_tlca import *
import sys

if __name__=='__main__':

    if len(sys.argv) < 5:
        print("Error! Not enough arguments. Exiting.")
        sys.exit()


    name_csv = sys.argv[1]
    xlsx_tlca_vide = sys.argv[2]
    xlsx_tlca_rempli = sys.argv[3]

    columns = list()

    for i in range(4, len(sys.argv)):
        columns.append(sys.argv[i])


    ScriptImportation(name_csv, xlsx_tlca_vide, xlsx_tlca_rempli, columns)
    #import_vers_tlca('moodle.csv')
