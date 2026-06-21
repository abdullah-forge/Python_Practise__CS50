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


#Day2 covered, loops, _, list, dictionary, range funtion, len, none,dictionary inside the list and for loop inside the for loop

def main():
    raw_signals = [45, 115, 60, 130, 25,25]
    f_signal = {}
    signal_classification(raw_signals,f_signal)
    print_signals(f_signal)


def signal_classification(raw_signals,f_signal):
    for i in range(len(raw_signals)):
        signal_val = raw_signals[i]
        keyname = f"Signal_{i+1}"
        if signal_val > 100:
            f_signal[keyname] = f"Noisy {signal_val} Hz"
        elif raw_signals[i] < 100:
            f_signal[keyname] = f"clean {signal_val} Hz"
    

def print_signals(f_signal):
    print("[LOG] Batch Processing Complete:") 
    for key,value in f_signal.items():
        print(f"{key} : {value}")
main()

# dictionary inside the list and for loop inside the for loop
sensor_network = [
    {"node_id" : "Alpha_1", "signals" : [45,115,60]},
    {"node_id": "Beta_2", "signals": [130, 25, 90]} 
]

for key in sensor_network:
    print(f"Analyzing node : {key["node_id"]}" )
    current_signal = key["signals"]
    for signal_val in current_signal:

        if signal_val > 100:
            print(f" - Signal {signal_val} Hz: NOISY")
        else: 
            print(f" - Signal {signal_val} Hz: CLEAN")
 
#try, except, else and pass

def main():
    incoming_signals = ["45", "115", "ERROR_NOCONNECTION", "60", "130"]
    clean_data = []
    checking_signals(incoming_signals,clean_data)
    print_signal(clean_data)


def checking_signals(incoming_signals,clean_data):
    for signal in incoming_signals:
        try:
            x = int(signal)
        except ValueError:
            pass
        else:
            clean_data.append(x)

def print_signal(clean_data):
    for value in clean_data:
        print(value)

main()
    


