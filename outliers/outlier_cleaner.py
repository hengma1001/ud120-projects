#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errors = abs(net_worths - predictions)  
    n_count = 0 
    for error, age, net_worth in sorted(zip(errors, ages, net_worths)): 
        if n_count < 0.9 * len(ages): 
            cleaned_data.append((age, net_worth, error)) 
        n_count += 1 
    
    return cleaned_data

