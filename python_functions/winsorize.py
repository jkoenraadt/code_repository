def winsorize(df, percentiles=None, trim=True, include=None, exclude=None):
    """
    This function winsorizes the columns of a pandas dataframe. The user can select the percentiles, whether the
    observations are set to "NaN" (missing, and therefore trimmed) or to the winsorized value, and which columns to
    include/exclude. It returns a pandas dataframe of the same dimensions.

    :param df:				A pandas dataframe with the variables to winsorize.
    :param percentiles:		Specified winsorization percentiles. Default is 1% and 99%.
    :param trim:			Trim the variables by setting them to 'NaN', if 'False' replace values to 1% and 99%.
                            Default is 'True'
    :param include:			List of variables to include in the winsorization. Default is all columns.
    :param exclude:			List of variables to exclude from the winsorization, all other will be winsorized. Default
                            is none of the columns.
    :return:				A pandas dataframe of the same dimensions, in which the variables are winsorized.
    """
    # Import packages
    import numpy as np
    import pandas as pd

    # Set defaults
    if percentiles is None:
        percentiles = [0.01, 0.99]
    if include is None:
        include = list(df.columns)
    if exclude is None:
        exclude = list()

    # Error handling
    if not pd.Series(include).isin(df.columns).all():
        print("Some columns in 'include' are not in the dataframe!")
        return
    if len(exclude) != 0:
        if not pd.Series(exclude).isin(df.columns).all():
            print("Some columns in 'exclude' are not in the dataframe!")
            return
    if len(percentiles) > 2:
        print("Percentiles list is too long, maximum is 2!")
        return
    if percentiles[0] > percentiles[1]:
        percentiles[0], percentiles[1] = percentiles[1], percentiles[0]
    if not isinstance(include, list):
        include = [include]
    if not isinstance(exclude, list):
        exclude = [exclude]
    if len(include) != 0 & len(exclude) != 0:
        print("Select either columns to include or exclude, not both!")
        return
    if not isinstance(trim, bool):
        print("'Trim' should be boolean!")
        return

    # Save current column order
    column_order = df.columns

    # List of columns to winsorize
    if len(exclude) != 0:
        df_to_winsorize = df.drop(exclude, axis=1)
        df_not_winsorize = df[exclude]
    else:
        exclude = [col for col in df.columns if col not in include]
        df_to_winsorize = df.drop(exclude, axis=1)
        df_not_winsorize = df[exclude]

    # Winsorize columns
    for col in df_to_winsorize.columns:
        # Use quantile function to get cut off values
        cutoff_value_low = df[col].quantile(percentiles[0])
        cutoff_value_high = df[col].quantile(percentiles[1])

        # Winsorize variables
        if trim is True:
            df_to_winsorize.loc[df_to_winsorize[col] < cutoff_value_low, col] = np.nan
            df_to_winsorize.loc[df_to_winsorize[col] > cutoff_value_high, col] = np.nan
        else:
            df_to_winsorize.loc[df_to_winsorize[col] < cutoff_value_low, col] = cutoff_value_low
            df_to_winsorize.loc[df_to_winsorize[col] > cutoff_value_high, col] = cutoff_value_high

    # Combine dataframes
    df_list = [df_to_winsorize, df_not_winsorize]
    df_winsorized = pd.concat(df_list, axis=1)

    # Restore original order
    df_winsorized = df_winsorized[[col for col in column_order]]

    # Return
    return df_winsorized