def Celcius_to_Fahrenhite(temperature):
    fahrenhite = (temperature * 1.8)+32
    return fahrenhite

def Fahrenhite_to_Celcius(temperature):
    celcius = (temperature-32)/1.8
    return celcius

def operation():

    try:
        temperature = float(input('Enter temperature: '))
    except ValueError:
        print('enter valid temperature value.')
        return
    
    print('Where do you want to convert the temperature ? ')
    print('----------------------------------------------')
    print('1. Celcius to Fahrenhite')
    print('2. Fahrenhite to Celcius')
    print('----------------------------------------------')

    choice = int(input('Enter your choice: '))
    match choice:
        case 1 : 
            fharenhite = Celcius_to_Fahrenhite(temperature)
            print(fharenhite,"\u00B0F")
        case 2:
            celcius = Fahrenhite_to_Celcius(temperature)
            print(celcius,"\u00B0C")
        case default:
            print('choose correctly')

while(True):
    operation()
    choice = int(input('Do you want to continue ? (1 for Yes / 2 for No): '))
    if(choice == 1):
        operation()
    elif(choice == 2):
        exit(1)
    else:
        print('Choose correct option.')