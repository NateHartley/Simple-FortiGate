# For now copy FortiGate alerts into email.txt

with open(r'email.txt', 'r') as email:
    text = email.readlines()
    alert_num = 1

    # Summarised alerts go to alerts.log, its contents get written over everytime this program is run
    f = open("alerts.log", "w")

    for line in text:

        if line.find("date") != -1:
            date = line[5:15]
            time = line[21:29]
            f.write("Alert number: ")
            f.write(str(alert_num))
            f.write("\n")
            f.write("Date: ")
            f.write(date)
            f.write("\n")
            f.write("Time: ")
            f.write(time)
            f.write("\n")


        if line.find("action") != -1:
            word_list = line.split()
            for i in word_list:

                if i.find("srccountry") != -1:
                    f.write(i)
                    f.write("\n")

                if i.find("attack") != -1:
                    if i[6] == "=": # removes attackid keyword from being displayed
                        f.write(i)
                        f.write("\n")
                        f.write("\n")

                if i.find("action") != -1:
                    if i[0] != "c": # removes craction keyword from being displayed
                        f.write(i)
                        f.write("\n")

            alert_num += 1

    f.close()
