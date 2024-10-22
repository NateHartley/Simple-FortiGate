with open(r'email.txt', 'r', encoding="utf8") as email:
    text = email.readlines()
    alert_num = 1

    # Summarised alerts go to alerts.log, its contents get written over everytime this program is run
    f = open("alerts.log", "w")

    for line in text:

        if line.find("date") != -1:
            date = line[5:15]
            time = line[21:29]
            f.writelines(["Alert number: ", str(alert_num), "\n", "Date: ", date, "\n", "Time: ", time, "\n"])


        if line.find("action") != -1:
            word_list = line.split()
            for i in word_list:

                if i.find("srccountry") != -1:
                    f.write(i)

                    next_word = word_list.index(i)+1
                    if word_list[next_word].find("dstip") == -1: # if country has two words in its name
                        f.writelines([" ", word_list[next_word]])

                    f.write("\n")

                if i.find("attack") != -1:
                    if i[6] == "=": # removes attackid keyword from being displayed
                        f.writelines([i, "\n", "\n", "\n"])

                if i.find("action") != -1:
                    if i[0] != "c" and len(i) < 30: # removes craction keyword and url from being displayed
                        f.writelines([i, "\n"])

            alert_num += 1

    f.close()
