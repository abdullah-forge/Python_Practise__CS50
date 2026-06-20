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
