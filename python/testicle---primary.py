# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"PC5..00","system":"readv2"},{"code":"10965.0","system":"med"},{"code":"12695.0","system":"med"},{"code":"19026.0","system":"med"},{"code":"28215.0","system":"med"},{"code":"33424.0","system":"med"},{"code":"44918.0","system":"med"},{"code":"46552.0","system":"med"},{"code":"47565.0","system":"med"},{"code":"5241.0","system":"med"},{"code":"634.0","system":"med"},{"code":"6451.0","system":"med"},{"code":"6794.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('undescended-testicle-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["testicle---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["testicle---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["testicle---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
