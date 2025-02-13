def readdetailes(file_name):
    employe_details = ["ID,In,Out\n"]
    i=0
    with open(file_name, "r") as file:
        for line in file:
            while(i>=1):
                data = line.strip().split(",")
                name = data[0] 
                name_split = name.strip().split(" ") 
                user_info = name_split[1]
                user = user_info[1:-1]
                In_date = data[3]
                In_time = data[5]
                In = In_date + " " + In_time
                out_date = data[3]
                out_time = data[6]
                out = out_date + " " + out_time
                #employe_details[user]= In,out
                employe_details.append(f"{user}, {In}, {out} \n")
                break
            i = i+1
        return employe_details

def print_details(file_name):
    employee = readdetailes(file_name)
    with open("new_details.txt","w") as file:
        for i in employee:
            file.writelines(i) 
        file.writelines("\n")

print_details("time-cards - Sheet1.csv")