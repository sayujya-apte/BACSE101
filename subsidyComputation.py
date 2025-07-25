"""
1. Subsidy Computation

Agricultural subsidies are offered by the Indian government to farmers for improving
crop yields and benefiting them. To facilitate the farmers in finding the subsidy
amount, develop a Python code to calculate the subsidy based on the crop the farmer
grows. The farmers can grow one of these three types of crops: Rice, Wheat, or
Maize. The program calculates and displays the type of crop, total subsidy based on
the type of crop selected, along with the yield and market rate. Use menu driven
approach to implement the same. Each crop has a different formula for calculating
the subsidy:
Rice: Subsidy= (Yield × Market Rate) +100
Wheat: Subsidy= (Yield × Market Rate) +200
Maize: Subsidy= (Yield × Market Rate) +300

Input Format :
Press 1/2/3 to compute the Subsidy of Rice/Wheat/Maize
Next Line to enter the Market Rate
Next Line to enter the Yield
Enter either Yes/No

Output Format :
Display “Press 1/2/3 to compute the Subsidy of Rice/Wheat/Maize”
Display the Type of Crop, Subsidy, Yield and Market Rate
Do you want to continue (Yes/No). If Yes
Press 1/2/3 to compute the Subsidy of Rice/Wheat/Maize
Display the Type of Crop, Subsidy, Yield and MarketRate
Do you want to continue (Yes/No). If No, display ‘Thank you’

"""

cropNames = ["Rice", "Wheat", "Maize"]

while True:
    cropType = int(input("Press 1/2/3 to compute the subsidy of Rice/Wheat/Maize : "))

    if cropType in [1, 2, 3]:
        yieldValue = float(input("Enter yield : "))
        mktRate = float(input("Enter market rate : "))

        if cropType == 1:
            subsidy = (yieldValue * mktRate) + 100
        elif cropType == 2:
            subsidy = (yieldValue * mktRate) + 200
        elif cropType == 3:
            subsidy = (yieldValue * mktRate) + 300

        print(f'Subsidy for {cropNames[cropType - 1]} at yield {yieldValue} and market value {mktRate} is {subsidy}')

        cont = str(input("Continue? [Yes/No] : "))
        if cont.upper() == "YES":
            continue
        else:
            print("Thank you!")
            break

    else:
        print("Please enter valid crop type!")
