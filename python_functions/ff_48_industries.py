def fama_french_industry_classification(df):
    """
    This function takes a Compustat Pandas Dataframe (with at least GVKEY and SIC) as input and returns a
    Compustat Pandas Dataframe with the names and abbreviation of the 48 Fama & French Industries appended
    (Industry classification from Kenneth French’ website).

    :param df:	Pandas Dataframe. Compustat data with GVKEY and SIC.
    :return:	Pandas Dataframe. Compustat data, with the industry name and abbreviation appended.

    Example:
    compustat_ind_dataframe = fama_french_industry_classification(compustat_dataframe)
    """
    # Packages
    import pandas as pd

    # Functions
    def make_sic_list(sic_list_of_lists):
        # Empty final list to fill
        sic_list = []

        # Loop over all sub-lists in the list of lists
        for sic_begin_end_sub_list in sic_begin_end_list:

            # Empty sub-list to fill
            sic_sub_list = []

            # Loop over all lists in the top list
            for sic_begin_end in sic_begin_end_sub_list:
                # SIC begin
                sic_begin = sic_begin_end[0]

                # SIC end
                sic_end = sic_begin_end[1]

                # Get all SICs between begin and end
                sic_sub_comb_list = [str(sic).zfill(4) for sic in range(sic_begin, sic_end)]

                # Append to sub-list
                sic_sub_list.append(sic_sub_comb_list)

            # Flatten the list
            sic_sub_list = [item for sub_list in sic_sub_list for item in sub_list]

            # Append to final list
            sic_list.append(sic_sub_list)

        # Return
        return sic_list

    # Error handling
    if not isinstance(df, pd.DataFrame):
        print("Error: 'df' is not a dataframe!")
        return
    if "gvkey" not in df.columns:
        print("Error: required column 'gvkey' is not in the provided dataframe 'df'!")
        return
    if "sic" not in df.columns:
        print("Error: required column 'sic' is not in the provided dataframe 'df'!")
        return

    # Combine industry names in string list
    industries_list = ["Agriculture", "Food Products", "Candy & Soda", "Beer & Liquor", "Tobacco Products",
                       "Recreation", "Entertainment", "Printing and Publishing", "Consumer Goods", "Apparel",
                       "Healthcare", "Medical Equipment", "Pharmaceutical Products", "Chemicals",
                       "Rubber and Plastic Products", "Textiles", "Construction Materials", "Construction",
                       "Steel Works Etc", "Fabricated Products", "Machinery", "Electrical Equipment",
                       "Automobiles and Trucks", "Aircraft", "Shipbuilding, Railroad Equipment", "Defense",
                       "Precious Metals", "Non-Metallic and Industrial Metal Mining", "Coal",
                       "Petroleum and Natural Gas", "Utilities", "Communication", "Personal Services",
                       "Business Services", "Computers", "Electronic Equipment", "Measuring and Control Equipment",
                       "Business Supplies", "Shipping Containers", "Transportation", "Wholesale", "Retail",
                       "Restaurants, Hotels, Motels", "Banking", "Insurance", "Real Estate", "Trading",
                       "Almost Nothing"]

    # Combine industry abbreviations in string list
    industries_abbrev_list = ["AGRIC", "FOOD", "SODA", "BEER", "SMOKE", "TOYS", "FUN", "BOOKS", "HSHLD", "CLTHS",
                              "HLTH", "MEDEQ", "DRUGS", "CHEMS", "RUBBR", "TXTLS", "BLDMT", "CNSTR", "STEEL", "FABPR",
                              "MACH", "ELCEQ", "AUTOS", "AERO", "SHIPS", "GUNS", "GOLD", "MINES", "COAL", "OIL", "UTIL",
                              "TELCM", "PERSV", "BUSSV", "COMPS", "CHIPS", "LABEQ", "PAPER", "BOXES", "TRANS", "WHLSL",
                              "RTAIL", "MEALS", "BANKS", "INSUR", "RLEST", "FIN", "OTHER"]

    # Combine all beginning and ending SIC codes for each industry in a list of lists
    sic_begin_end_list = [
        [[100, 200], [200, 300], [700, 800], [910, 920], [2048, 2049]],
        [[2000, 2047], [2050, 2064], [2070, 2080], [2090, 2093], [2095, 2096], [2098, 2100]],
        [[2064, 2069], [2086, 2087], [2096, 2098]],
        [[2080, 2086]],
        [[2100, 2200]],
        [[920, 1000], [3650, 3653], [3732, 3733], [3930, 3932], [3940, 3950]],
        [[7800, 7834], [7840, 7842], [7900, 7901], [7910, 7912], [7920, 7934], [7940, 7950], [7980, 7981], [7990, 8000]
         ],
        [[2700, 2750], [2770, 2772], [2780, 2800]],
        [[2047, 2048], [2391, 2393], [2510, 2520], [2590, 2600], [2840, 2845], [3160, 3162], [3170, 3173], [3190, 3200],
         [3229, 3230], [3260, 3261], [3262, 3264], [3269, 3270], [3230, 3232], [3630, 3640], [3750, 3752], [3800, 3801],
         [3860, 3862], [3870, 3874], [3910, 3912], [3914, 3916], [3960, 3963], [3991, 3992], [3995, 3996]],
        [[2300, 2391], [3020, 3022], [3100, 3111], [3130, 3132], [3140, 3152], [3963, 3966]],
        [[8000, 8100]],
        [[3693, 3694], [3840, 3852]],
        [[2830, 2832], [2833, 2837]],
        [[2800, 2830], [2850, 2880], [2890, 2900]],
        [[3031, 3032], [3041, 3042], [3050, 3054], [3060, 3100]],
        [[2200, 2285], [2290, 2296], [2297, 2300], [2393, 2396], [2397, 2400]],
        [[800, 900], [2400, 2440], [2450, 2460], [2490, 2500], [2660, 2662], [2950, 2953], [3200, 3201], [3210, 3212],
         [3240, 3242], [3250, 3260], [3264, 3265], [3270, 3276], [3280, 3282], [3290, 3294], [3295, 3300], [3420, 3434],
         [3440, 3443], [3446, 3447], [3448, 3453], [3490, 3500], [3996, 3997]],
        [[1500, 1512], [1520, 1550], [1600, 1800]],
        [[3300, 3301], [3310, 3318], [3320, 3326], [3330, 3342], [3350, 3358], [3360, 3380], [3390, 3400]],
        [[3400, 3401], [3443, 3445], [3460, 3480]],
        [[3510, 3537], [3538, 3570], [3580, 3583], [3585, 3587], [3589, 3599]],
        [[3600, 3601], [3610, 3614], [3620, 3622], [3623, 3630], [3640, 3647], [3648, 3650], [3660, 3661], [3690, 3693],
         [3699, 3700]],
        [[2296, 2297], [2396, 2397], [3010, 3012], [3537, 3538], [3647, 3648], [3694, 3695], [3700, 3701], [3710, 3712],
         [3713, 3717], [3790, 3793], [3799, 3800]],
        [[3720, 3722], [3723, 3726], [3728, 3730]],
        [[3730, 3732], [3740, 3744]],
        [[3760, 3770], [3795, 3796], [3480, 3490]],
        [[1040, 1050]],
        [[1000, 1040], [1050, 1120], [1400, 1500]],
        [[1200, 1300]],
        [[1300, 1301], [1310, 1340], [1370, 1383], [1389, 1390], [2900, 2913], [2990, 3000]],
        [[4900, 4901], [4910, 4912], [4920, 4926], [4930, 4933], [4939, 4943]],
        [[4800, 4801], [4810, 4814], [4820, 4823], [4830, 4842], [4880, 4893], [4899, 4900]],
        [[7020, 7022], [7030, 7034], [7200, 7201], [7210, 7213], [7214, 7218], [7219, 7222], [7230, 7232], [7240, 7242],
         [7250, 7252], [7260, 7300], [7395, 7396], [7500, 7501], [7520, 7550], [7600, 7601], [7620, 7621], [7622, 7624],
         [7629, 7632], [7640, 7642], [7690, 7700], [8100, 8500], [8600, 8700], [8800, 8900], [7510, 7516]],
        [[2750, 2760], [3993, 3994], [7218, 7219], [7300, 7301], [7310, 7343], [7349, 7354], [7359, 7373], [7374, 7386],
         [7389, 7395], [7396, 7398], [7399, 7400], [7519, 7520], [8700, 8701], [8710, 8714], [8720, 8722], [8730, 8735],
         [8740, 8749], [8900, 8912], [8920, 9000], [4220, 4230]],
        [[3570, 3580], [3680, 3690], [3695, 3696], [7373, 7374]],
        [[3622, 3623], [3661, 3667], [3669, 3680], [3810, 3811], [3812, 3813]],
        [[3811, 3812], [3820, 3828], [3829, 3840]],
        [[2520, 2550], [2600, 2640], [2670, 2700], [2760, 2762], [3950, 3956]],
        [[2440, 2450], [2640, 2660], [3220, 3222], [3410, 3413]],
        [[4000, 4014], [4040, 4050], [4100, 4101], [4110, 4122], [4130, 4132], [4140, 4143], [4150, 4152], [4170, 4174],
         [4190, 4201], [4210, 4220], [4230, 4232], [4240, 4250], [4400, 4701], [4710, 4713], [4720, 4750], [4780, 4781],
         [4782, 4786], [4789, 4790]],
        [[5000, 5001], [5010, 5016], [5020, 5024], [5030, 5061], [5063, 5066], [5070, 5079], [5080, 5095], [5099, 5101],
         [5110, 5114], [5120, 5123], [5130, 5173], [5180, 5183], [5190, 5200]],
        [[5200, 5201], [5210, 5232], [5250, 5252], [5260, 5262], [5270, 5272], [5300, 5301], [5310, 5312], [5320, 5321],
         [5330, 5332], [5334, 5335], [5340, 5350], [5390, 5401], [5410, 5413], [5420, 5470], [5490, 5501], [5510, 5580],
         [5590, 5701], [5710, 5723], [5730, 5737], [5750, 5800], [5900, 5901], [5910, 5913], [5920, 5933], [5940, 5991],
         [5992, 5996], [5999, 6000]],
        [[5800, 5830], [5890, 5900], [7000, 7001], [7010, 7020], [7040, 7050], [7213, 7214]],
        [[6000, 6001], [6010, 6037], [6040, 6063], [6080, 6083], [6090, 6100], [6110, 6114], [6120, 6180], [6190, 6200]
         ],
        [[6300, 6301], [6310, 6332], [6350, 6352], [6360, 6362], [6370, 6380], [6390, 6412]],
        [[6500, 6501], [6510, 6511], [6512, 6516], [6517, 6533], [6540, 6542], [6550, 6554], [6590, 6600], [6610, 6612]
         ],
        [[6200, 6300], [6700, 6701], [6710, 6727], [6730, 6734], [6740, 6780], [6790, 6796], [6798, 6800]],
        [[4950, 4962], [4970, 4972], [4990, 4992]]
    ]

    # Using the starting and ending SIC codes, make a list of SIC codes for each industry
    sic_list = make_sic_list(sic_begin_end_list)

    # Combine industry abbreviations and SICs in dictionary
    industry_dict = dict(zip(industries_abbrev_list, sic_list))

    # Make dataframe from dictionary
    industry_df = pd.DataFrame.from_dict(industry_dict, orient='index'). \
        rename_axis("ind"). \
        reset_index().melt(id_vars=["ind"], value_name="sic"). \
        drop("variable", axis=1). \
        dropna(). \
        sort_values(["ind", "sic"]). \
        drop_duplicates(). \
        reset_index(drop=True)

    # Combine industry names and industry abbreviations in dataframe
    industry_name_df = pd.DataFrame({"ind_name": industries_list, "ind": industries_abbrev_list}).drop_duplicates()

    # Merge industry names into sics/industry abbreviations dataframe
    industry_df = industry_df.merge(industry_name_df, on="ind", how="left")[["sic", "ind", "ind_name"]]. \
        drop_duplicates(["sic", "ind"])

    # Merge industry dataframe with Compustat dataframe
    return_df = df.merge(industry_df, on="sic", how="left"). \
        drop_duplicates(). \
        sort_values(["gvkey", "datadate"]). \
        reset_index(drop=True)

    # Return dataframe
    return return_df
