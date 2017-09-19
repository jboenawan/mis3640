def calculate_bmi(weight, height):
    bmi = 703 * weight / (height * height)

    if bmi <= 18.5:
        print("your bmi is {:.1f}. You are underweighted.".format(bmi))
    elif bmi > 18.5 and bmi <= 25:
        print("your bmi is {:.1f}. You are normal-weighted.".format(bmi))
    elif 25 < bmi <= 29.9:
        print("your bmi is {:.1f}. You are overweighted.".format(bmi))
    else:
        print("your bmi is {:.1f}. You are obese.".format(bmi))

weight = input('Enter your weight (in lb):')
height = input('Enter your height (in in):')
weight = float(weight)
height = float(height)
calculate_bmi(weight, height)