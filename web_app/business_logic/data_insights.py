'''
data_insights

This file supports data calculation and processing operations.

'''

# Module Importations
import copy
import datetime
import pandas as pd

def return_min(generation_type, df_original):
    """Return Min
    ======================================
    Returns the minimum generation of a particular generation type, calculated from a supplied dataframe.
    
    Args:
        generation_type (string) - Type of generation to determine minimum for.
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        min_generation (float64) - Minimum value determined for generation type.
    """

    # Copy dataframe
    df_min = df_original.copy()

    # Filter dataframe for generation type
    df_min = df_min[(df_min['powType'] == generation_type)]

    # Calculate minimum generation for type
    min_generation = df_min['quantity'].min()

    # Return minimum
    return min_generation

def return_max(generation_type, df_original):
    """Return Max
    ======================================
    Returns the maximum generation of a particular generation type, calculated from a supplied dataframe.
    
    Args:
        generation_type (string) - Type of generation to determine maximum for.
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        max_generation (float64) - Maximum value determined for generation type.
    """

    # Copy dataframe
    df_max = df_original.copy()

    # Filter dataframe for generation type
    df_max = df_max[(df_max['powType'] == generation_type)]

    # Calculate maximum generation for type
    max_generation = df_max['quantity'].max()

    # Return maximum
    return max_generation

def return_mean(generation_type, df_original):
    """Return Mean
    ======================================
    Returns the mean of a particular generation type, calculated from a supplied dataframe.
    
    Args:
        generation_type (string) - Type of generation to determine mean for.
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        mean (float64) - Arithmetic mean determined for generation type.
    """

    # Copy dataframe
    df_mean = df_original.copy()

    # Filter dataframe for generation type
    df_mean = df_mean[(df_mean['powType'] == generation_type)]

    # Calculate mean generation for type
    mean = df_mean['quantity'].mean()

    # Return mean
    return mean

def return_sum_GWh(generation_type, df_original):
    """Return Sum GWh
    ======================================
    Returns the generation sum of a particular generation type, calculated from a supplied dataframe.
    
    Args:
        generation_type (string) - Type of generation to be summed.
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        sum_generation_GWh (float64) - Summed output determined for generation type.
    """

    # Copy dataframe
    df_sum = df_original.copy()

    # Filter dataframe for generation type
    df_sum = df_sum[(df_sum['powType'] == generation_type)]

    # Calculate summed generation for type
    sum_generation_GWh = (df_sum['quantity'].sum()) * 0.5 # Df is summarised in 30 min segments

    # Convert to GWh
    sum_generation_GWh = sum_generation_GWh * 0.001

    # Return sum
    return sum_generation_GWh

def return_total_sum_GWh(df_original):
    """Return Total Sum GWh
    ======================================
    Returns the total sum of generation from a supplied dataframe in GWh.
    
    Args:
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        total_sum_generation_GWh (float64) - Total summed output determined for dataframe.
    """

    # Copy dataframe
    df_total_sum = df_original.copy()

    # Calculate summed generation
    total_sum_generation_GWh = (df_total_sum['quantity'].sum()) * 0.5 # Df summarised in 30 min segments

    # Convert to GWh
    total_sum_generation_GWh = total_sum_generation_GWh * 0.001

    # Return sum
    return total_sum_generation_GWh

def rename_dataframe_powertypes(df_original):
    """Rename Dataframe Powertypes
    ======================================
    Renames some of the powertypes in the dataframe, for table presentation.
    
    Args:
        df_original (df) - Original dataframe.
        
    Returns:
        df_final (df) - Revised dataframe with renamed power types.
    """

    # Copy original dataframe
    df_final = df_original.copy()

    # Replace each of the powertypes in turn
    df_final['powType'] = df_final['powType'].replace({'Hydro Run-of-river and poundage': 'Hydro'})
    df_final['powType'] = df_final['powType'].replace({'Hydro Pumped Storage': 'Hydro Storage'})
    df_final['powType'] = df_final['powType'].replace({'Fossil Oil': 'Oil'})
    df_final['powType'] = df_final['powType'].replace({'Fossil Gas': 'Gas'})
    df_final['powType'] = df_final['powType'].replace({'Fossil Hard coal': 'Coal'})

    # Return the new dataframe
    return df_final

def rename_dict_keys(dict_original):
    """Rename Dict Keys
    ======================================
    Renames some of the keys in the dict, for table presentation.
    
    Args:
        dict_original (dict) - Dictionary with original key names.
        
    Returns:
        dict_final (dict) - Dictionary with final key names.
    """

    # Copy original dict
    dict_final = copy.deepcopy(dict_original)

    # Replacement keys
    key_old_1 = "Hydro Run-of-river and poundage"
    key_new_1 = "Hydro"
    key_old_2 = "Hydro Pumped Storage"
    key_new_2 = "Hydro Storage"
    key_old_3 = "Fossil Oil"
    key_new_3 = "Oil"
    key_old_4 = "Fossil Gas"
    key_new_4 = "Gas"
    key_old_5 = "Fossil Hard coal"
    key_new_5 = "Coal"

    # Replace keys using pop method
    for key in dict_final:
        
        if key == key_old_1:
            dict_final[key_new_1] = dict_final.pop(key_old_1)

        if key == key_old_2:
            dict_final[key_new_2] = dict_final.pop(key_old_2)

        if key == key_old_3:
            dict_final[key_new_3] = dict_final.pop(key_old_3)

        if key == key_old_4:
            dict_final[key_new_4] = dict_final.pop(key_old_4)

        if key == key_old_5:
            dict_final[key_new_5] = dict_final.pop(key_old_5)

    # Return dictionary
    return dict_final

def return_summary_df(df_original, 
                      start_date = datetime.datetime(2020,1,1, 0, 0, 0), 
                      end_date = datetime.datetime(2021,1,1, 0, 0, 0),
                      is_renewable = False):
    """Return Stats Summary Dataframe
    ======================================
    Returns a new dataframe summarising generation data stats. Can be set to only return renwable summary.
    
    Args:
        df_original (DataFrame) - Dataframe with time-series generation data.
        start_date (Datetime) - Earliest date for inclusion in stats calculations.
        end_date (Datetime) - Latest date for inclusion in stats calculations.
        is_renewable (False) -  Indicates whether to return a summary for renewable generation only.
        
    Returns:
        df_summary_stats (DataFrame) - New dataframe containing aggregated data.
    """
    
    # Copy dataframe
    df_timeseries = df_original.copy()
    df_timeseries.sort_values(by = ['setDatetime'], inplace = True)
    
    # Mask dataframe between start and end dates
    start_date = datetime.datetime(2020,3,1, 0, 0, 0)
    end_date = datetime.datetime(2021,1,1, 0, 0, 0)
    
    df_timeseries = df_timeseries[(df_timeseries['setDatetime'] > start_date)]
    df_timeseries = df_timeseries[(df_timeseries['setDatetime'] < end_date)]
    
    # Calculate total generation across whole time series
    total_generation_GWh = return_total_sum_GWh(df_timeseries)

    # Create dict for new dataframe, containing each parameter of interest
    if is_renewable == False:
         data_summary = {
            "Solar": [0, 0, 0, 0, 0],
            "Wind Offshore": [0, 0, 0, 0, 0],
            "Wind Onshore": [0, 0, 0, 0, 0],
            "Hydro": [0, 0, 0, 0, 0],
            "Hydro Storage": [0, 0, 0, 0, 0],
            "Other": [0, 0, 0, 0, 0], 
            "Nuclear": [0, 0, 0, 0, 0], 
            "Oil": [0, 0, 0, 0, 0], 
            "Gas": [0, 0, 0, 0, 0], 
            "Coal": [0, 0, 0, 0, 0], 
            "Biomass": [0, 0, 0, 0, 0]
            }
    else:
        data_summary = {
            "Solar": [0, 0, 0, 0, 0],
            "Wind Offshore": [0, 0, 0, 0, 0],
            "Wind Onshore": [0, 0, 0, 0, 0],
            "Hydro": [0, 0, 0, 0, 0],
            "Hydro Storage": [0, 0, 0, 0, 0],
            "Biomass": [0, 0, 0, 0, 0]
            }


    # Iterate over dict keys and populate stats
    for key in data_summary:

        # Determine statistics for each generation type
        generation_min = return_min(key, df_timeseries)
        generation_mean = return_mean(key, df_timeseries)
        generation_max = return_max(key, df_timeseries)
        generation_sum_GWh = return_sum_GWh(key, df_timeseries)
        generation_percent = (generation_sum_GWh / total_generation_GWh) * 100

        # Update dict with generation statistics
        data_summary[key][0] = generation_min
        data_summary[key][1] = generation_mean
        data_summary[key][2] = generation_max
        data_summary[key][3] = generation_sum_GWh
        data_summary[key][4] = generation_percent

    # Create and return df from dict
    df_summary = pd.DataFrame.from_dict(data_summary, orient='index')

    # Update column labels
    df_summary.rename(columns = {0: "Min", 1:"Mean", 2:"Max", 3:"Sum", 4:"% Total"}, inplace=True)
    
    return df_summary