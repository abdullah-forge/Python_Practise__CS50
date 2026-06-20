#Day1 --- variable, function, scope, data type,  round, retun,split,title,capatilize, strip, end,sep, f string , input

#Raw data
def main():
    data = input("Name, Height :")
    final_output = Format_profile(data)
    print(final_output)
def Format_profile(data):
    parts = data.split(",")
    Name = parts[0].strip().title()
    height = parts[1].strip()
    clean_height = round(float(height),2)
    return f"Name : {Name}, height : {clean_height}"

main()

# cover topics are _, match, conditionals (if,elif,else, or and not )

def main():
    data = input("Enter Core ID and Temperature: ")
    output = check_Reactor(data)
    print(output)
def check_Reactor(data):
    parts = data.split(",")
    core_id = parts[0]
    temp = parts[1]
    core_id = core_id.strip().upper()
    temp = temp.strip()
    temp = round(float(temp), 1)
    ...
    if temp <= 50.0:
        status = 'safe'
        state = "Safe"
    elif temp > 50.0 and temp <= 90.0:
        status = "Fans turn ON"
        state = "Warning"
    else:
        status = "Shut down"
        state = "Critical"
    ...    
    match temp:
        case temp if temp <=  50.0:
            status = 'safe'
            state = "Safe"
        case temp if temp >50.0 and temp <= 90.00:
            status = "Fans turn ON"
            state = "Warning"
        case _:
            status = "Shut down"
            state = "Critical"
    return f"{state}, {core_id} Temp: {temp}C -> {status}"


main()
