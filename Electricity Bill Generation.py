# ELECTRICITY BILL GENERATION
import logging
try:
    logging.basicConfig(filename="EBill_logging.txt", level=logging.INFO,format='%(asctime)s %(message)s %(levelname)s %(name)s')

    logging.info("User are  going to enter Tarrif Detais")
    Tariff_details = input("Enter the Tariff unit value ('LT1','LT2A','LT2B','LT3'): ")
    logging.info(f"User Entered the tariif details {Tariff_details}")

    logging.info("The entered user details is converting into Alphanumeric")
    alphanumeric_input = ''.join(i for i in Tariff_details if i.isalnum())
    logging.info(f"The entered details is converted into alphanumeric {alphanumeric_input}")

    logging.info("Alphanumeric value will be converted to Uppercase")
    uppercase_input = alphanumeric_input.upper()
    logging.info(f"The upper case value is {uppercase_input}")

    logging.info("Now the uppercase value will be used as Tariff Details")
    Tariff = uppercase_input
    logging.info(f"The output tariff details will be{Tariff}")

    KW = float(input("Enter the KW used :", ))
    logging.info(f"The Kw entered by user is {KW}")

    units = float(input("Enter the units used  : "))
    logging.info(f"The Units entered by user is {units} ")

    # FIXED CHARGES for KW
    # Energy Consumed in Units

    if Tariff == "LT1":
        logging.info("Entering into the Tariff LT21")
        print("70INR is fixedcharges and for every 1 unit 8.75 INR and if it goes above 40 units it will converted into 2LT")
        if units>=1:
            a=70
            b=units*8.75
            print("The bill charge is :",units,"*","8.75","=",b)
        elif units > 40:
            print("it will be converted into LT2A")


    elif Tariff == "LT2A":
        logging.info("We Entered into Tariff LT2A")

        if KW < 1:
            logging.info("The KW range is below 1")
            a = KW * 100
            print("Fixed charges of rupess 100INR")
            print("The Fixed charged price is :", KW, "*", 100, "=", a)
            logging.info(f"Fixed charge rupees of Tariff Connectivity is : {a} ")


        elif KW >= 1 and KW < 50:
            logging.info("The KW range is above  1 and below 50")
            a = KW * 110
            print("Fixed charge of rupess 110INR")
            print("The Fixed charged price is :", KW, "*", 110, "=", a)
            logging.info(f"Fixed charge rupees of Tariff Connectivity is : {a} ")


        elif KW > 50:
            logging.info("The KW range is above 50 ")
            a = KW * 175
            print("Fixed charge of rupess 175INR")
            print("The Fixed charged price is :", KW, "*", 175, "=", a)
            logging.info(f"Fixed charge rupees of Tariff Connectivity is : {a} ")

        if Tariff == "LT2A":
            logging.info("We entered into  details for LT2A for units consumption")

            if units >= 0 and units <= 50:
                logging.info("The Units range is >0 and <50 ")
                b = round(units * 4.15, 3)
                print("single unit charge is 4.15INR")
                print("The energy charges for used electircity is : ", units, "*", 4.15, "=", b)
                logging.info(f"The charges for consumption of units is {b} ")

            elif units > 51 and units <= 100:
                logging.info("The Units range is >51 and <100 ")
                b = round(units * 5.60, 3)
                print('single unit charge is  5.60INR')
                print("The energy charges for used electircity is : ", units, "*", 5.60, "=", b)
                logging.info(f"The charges for consumption of units is {b} ")

            elif units > 101 and units <= 200:
                logging.info("The Units range is >101 and <200 ")
                b = round(units * 7.15, 3)
                print("units charge is 7.15INR")
                print("The energy charges for used electircity is : ", units, "*", 7.15, "=", b)
                logging.info(f"The charges for consumption of units is {b} ")

            elif units > 200:
                logging.info("The Units range is >200 ")
                b = round(units * 8.20, 3)
                print("units charge is 8.20INR")
                print("The energy charges for used electircity is : ", units, "*", 8.20, "=", b)
                logging.info(f"The charges for consumption of units is {b} ")



    elif Tariff == "LT2B":
        logging.info("Entering into the Tariff LT2B")
        print("Fixed charges of 150INR ")
        logging.info("Fixwd charge is 150INR")

        if KW > 0 and KW <=1:
            logging.info("The KW range is >0 and <1 ")
            a = (KW * 120)+150
            print("Fixed charges of rupess 120INR")
            print("The Fixed charged price is : ", KW, "*", 120,"+","150", "=", a)
            logging.info(f"Here we got fixed charge rupees:{a}")

        elif KW > 1:
            logging.info("The KW range is above 1")
            a = (KW * 175)+150
            print("and along with it should pay 175INR")
            print("The Fixed charged price is : ", KW, "*", 175,"+","150", "=", a)
            logging.info(f"Here we got fixed charge rupees:{a}")

        else:
            print("something wrong")
            logging.error(f"User inputed wrong Taifff name {Tariff}")

        if Tariff == "LT2B":
            logging.info("We  are enetering details for LT2B for units consumption")
            if units >= 0 and units <= 200:
                logging.info("The Units range is >0 and <200 ")
                b = round(units * 7.35, 3)
                print("single unit charge is 7.35 INR")
                print("The energy charges for used electircity is : ", units, "*", 7.35, "=", b)
                logging.info(f"The Units consumed is: {b}")

            elif units > 200:
                logging.info("The Units range is >200 ")
                b = round(units * 8.60, 3)
                print('single unit charge is 8.60 INR')
                print("The energy charges for used electircity is : ", units, "*", 8.60, "=", b)
                logging.info(f"The Units consumed is: {b}")
            else:
                print("something wrong")
                logging.info("Something wrong input: ")


    elif Tariff == "LT3":
        logging.info("Entering into the Tariff LT3")

        if KW >= 1 and KW <=50:
            logging.info("The KW range is > 1 and <50")
            a = KW * 125
            print("Fixed charges of rupess 125INR")
            print("The Fixed charged price is : ", KW, "*", 125, "=", a)
            logging.info(f"Here we got fixed charge rupees:{a}")

        elif KW > 50:
            a = KW * 230
            logging.info("The KW range is > 230")
            print("and along with it should pay 230INR")
            print("The Fixed charged price is : ", KW, "*", 230, "=", a)
            logging.info(f"Here we got fixed charge rupees:{a}")
        else:
            print("something wrong")
            logging.info("Some error in tariif details Entered")

        if Tariff == "LT3":
            logging.info("We  are enetering details for LT3 for units consumption")
            if units >= 0 and units <= 50:
                b = round(units * 8.40, 3)
                print("single unit charge is  8.40 INR")
                print("The energy charges for used electircity is : ", units, "*", 8.40, "=", b)
                logging.info(f"The Units consumed is: {b}")
            elif units > 50:
                b = round(units * 9.40, 3)
                print('single unit charge is 9.40 INR')
                print("The energy charges for used electircity is : ", units, "*", 9.40, "=", b)
                logging.info(f"The Units consumed is: {b}")
            else:
                print("something wrong")


    else:
        print("something wrong in user input on Tariff please refer note of text file (TariffDetails.txt) for details ")
        logging.info("something wrong in user input on Tariff please refer note of text file (TariffDetails.txt) for details ")

    Total = a + b
    Total_bill_amount = round(Total, 3)
    logging.info(f"The total bill amount is :{Total_bill_amount}")
    print("Total electicicty bill is", a, "+", b, "=", Total_bill_amount)

except ValueError:
    print("Please enter float number or int numbers and also check the Tariff details entered",KW)
    logging.info("Please enter float number or int numbers and also check the Tariff details entered")
except ValueError:
    print("please enter proper units value")
    logging.info("please enter proper units value")
except:
    pass



