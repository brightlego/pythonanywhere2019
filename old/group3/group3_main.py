'''this main function inputs daily rainfall data from N Ghana,
calculates a set of statistics, generates a new set of data for 3 years
based on stats, calculates flood risk based on if amount of r > 20mm/day'''

def main():
    prob_rain, prob_norain, mean, stddev = analyse(file)
    amount = generate(mean, stddev, prob_rain, prob_norain)
    number_flood = risk(amount)

if __name__ == "__main__":
    main()