# Code Repository

This repository contains all shared code

FAMA & FRENCH 48 INDUSTRY-CLASSIFICATION  
This function takes a Compustat Pandas Dataframe (required columns: GVKEY, SIC) as input and returns a Compustat Pandas Dataframe with the names and abbreviation 
of the 48 Fama & French Industries appended (Industry classification from Kenneth French’ website). 

WINSORIZE  
This function takes a Pandas Dataframe as input and winsorizes (or trims) all (or a subset) of variables. It returns a Pandas Dataframe with winsorized variables.
