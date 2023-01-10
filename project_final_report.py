''' Zoe Garbus, Vivian Chen, Julia Luo
    DS2001 Final Project
    
    Report:
    a. Problem Statement and Background:
    i. The problem we are addressing is how the invasion of Ukraine by Russia 
    has affected the stock market of the companies that have pulled out of the 
    Russian economy. Specifically, determining which industry is the most 
    impacted by this conflict. This problem is important because it shows how
    a war affects not only the countries directly involved but it can affect 
    the economy of other nations which one might not initially expect - 
    because the world is so globalized today, war in another continent can 
    even affect the lives of regular citizens. For example, we see this in 
    rising gas prices all around the world. In addition, from a stockholder’s 
    perspective, these statistics would influence their decisions to either 
    buy or hold stocks from certain companies or industries.
    
    b. Introduction & Description of the Data:
    i. We collected our data from public stock market records for each company 
    we were going to be observing. More specifically, we found the stock 
    information from the beginning of 2022 up until Apr 12, 2022. We wanted to 
    analyze the data far back enough so we could compare the unaffected stock 
    prices with prices after the war started. 
    ii. The primary dataset that we used was Yahoo Finance. This constitutes 
    a record because it is a documentation of all public companies and 
    institutions stock market Information. It is accurate and verified 
    information that is utilized and is a primary source for businesses. 
    
    c. Methods
    i. The main techniques that we used throughout our project are related to
    our data visualization. These techniques allowed us to create clear and 
    concise graphs (plot & bar graphs) that portrayed the data in as effective 
    and understandable ways as possible. In addition, our graph included 
    various calculations using arithmetic operations to calculate averages 
    and differences and using built in functions like max() and min(). The 
    first half of our code works to visualize line graphs of each closing 
    price on each day since January 2022, for each individual company. In the 
    second part of our code, we found the difference between the price on the 
    day the company pulled out from Russia’s economy and the lowest price 
    after that date (in the find_diff function). Then in main, we plotted a 
    bar chart to compare those differences. Additionally, it finds and shows 
    the average difference for each industry. 
    
    d. Results, Conclusion, & Future Work
    i. Our analysis of the graphs concluded that the retail industry was most 
    affected by pulling out of Russia. One reason could be their earlier pull 
    out data compared to the companies from the other industries (almost a 
    week earlier than the companies we chose to look at). Another reason is 
    due to the disruptions in delivery since FedEX and UPS suspended their 
    shipments. Not to mention, brands such as Nike, Adidas, and Canada have 
    more luxury items that aren’t typically sought out as a daily necessity.
    For the gas sector, it was relatively surprising to see that their stock 
    prices did not decrease by that much. The companies had to increase their 
    prices for gas due to the lost resource of Russian oil. This may have 
    benefited the companies but negatively impacted the public because of the 
    extreme rise of gas prices. The food industry was also not greatly 
    affected. This is most likely due to the fact that the companies are not 
    extremely dependent on the business they conduct in the Russian economy. 
    They also pulled out of Russia much later than companies in other 
    industries. 

    ii. Our biggest strength throughout this project were our numerous data 
    visualizations. Our graphs are all very clear and organized in a way in 
    which the results can be understood clearly, even if someone was not 
    completely familiar with the content we focused on. Our limitations 
    included having to change the companies we originally had in mind because 
    there wasn’t relevant or accessible stock price data for those companies. 
    We wanted to look at a few companies that did not pull out of Russia, 
    for comparison, but most of them have their stock market information 
    private. Additionally, we felt that our main function could have been more 
    concise, given more time, by including more functions for our repeated 
    tasks.  

'''
import matplotlib.pyplot as plt

SHELL_FILE = "SHEL.csv"
BP_FILE = "BP.csv"
EXXON_FILE = "XOM.csv"

NIKE_FILE = "NKE.csv"
ADIDAS_FILE = "ADDYY.csv"
GOOSE_FILE = "GOOS.csv"

MCD_FILE = "MCD.csv"
PEPSI_FILE = "PEP.csv"
SBUCKS_FILE = "SBUX.csv"

#closing prices on the day the company pulled out

SHELL_PLP = 52.939999
BP_PLP = 29.209999
EXXON_PLP = 79.169998

ADIDAS_PLP = 113.489998
NIKE_PLP = 133.970001
GOOSE_PLP = 26.190001

MCD_PLP = 222.789993
PEPSI_PLP = 157.869995
SBUCKS_PLP = 84.000000

def read_file(filename):
    ''' Filename: read_file
        Parameter: filename, a string
        Returns: the dates (a list) and the closing prices (a list)
    '''
    dates = []
    close_price = []
    with open(filename, "r") as infile:
        header = infile.readline()
        while True:
            stocks = infile.readline()
            if stocks == "":
                break
            stocks = stocks.split(",")
            dates.append(stocks[0])
            close_price.append(float(stocks[4]))
            

    return dates, close_price

def get_max_price(dates, close_price):
    ''' Filename: get_max_price
        Parameters: dates (a list), close_price (a list)
        Returns: the max price (a float), the max date (a string)
    '''
    max_price = 0
    max_date = ''
    for i in range(len(close_price)):
        if close_price[i] > max_price:
            max_price = close_price[i]
            max_date = dates[i]

    return max_price, max_date 

def get_min_price(dates, close_prices):
    ''' Function: get_min_price
        Parameters: dates (a list), close_prices (a list)
        Returns: the min price (a float), the min date (a string)
    '''
    min_price = 1000
    min_date = ''
    
    for i in range(len(close_prices)):
        if close_prices[i] < min_price:
            min_price = close_prices[i]
            min_date = dates[i]
            
    return min_price, min_date

def make_plot(dates, close_price):
    ''' Function: make_plot
        Parameters: dates (a list), closing prices (a list)
        Returns: nothing just plots
    '''
    jan = []
    jan_price = []
    feb = []
    feb_price = []
    mar = []
    mar_price = []
    apr = []
    apr_price = []
    
    for i in range(len(dates)):
        if dates[i][5] == "0" and dates[i][6] == "1":
            jan.append(dates[i])
            jan_price.append(close_price[i])
            plt.plot(jan, jan_price, label = "Jan", color = "brown")
            
        elif dates[i][5] == "0" and dates[i][6] =="2":
            feb.append(dates[i])
            feb_price.append(close_price[i])
            plt.plot(feb, feb_price, label = "Feb", color = "red")
            
        elif dates[i][5] == "0" and dates[i][6] == "3":
            mar.append(dates[i])
            mar_price.append(close_price[i])
            plt.plot(mar, mar_price, label = "Mar", color = "green")
            
        elif dates[i][5] == "0" and dates[i][6] == "4":
            apr.append(dates[i])
            apr_price.append(close_price[i])
            plt.plot(apr, apr_price, label = "Apr", color = "blue")
            
    plt.xlabel("Jan 2022 to present")
    plt.ylabel("Closing Prices")
    plt.setp(plt.gcf().get_axes(), xticks=[])
    
def find_min_price_after_PLP(dates, closing_pr, company_plp):
    '''
    function: find_min_price_after_PLP
    parameters: dates(list of strings), closing_pr (list of floats, the prices
                associated with dates after the company's pull out date),
                company_plp (a float, the company's pull out date price)
    returns: min_price (the min price after the company pul out date (float))
    '''  
    min_price = 1000
   
    for i in range(len(closing_pr)):
        PLP_index = closing_pr.index(company_plp)
        after_PLP = closing_pr[PLP_index:]
        for i in range(len(after_PLP)):
            if after_PLP[i] < min_price:
                min_price = after_PLP[i]

    return min_price

def find_diff(company_plp, min_price):
    '''
    function: find_diff
    parameters: company_plp(float), min_price (float)
    returns: price_diff, the difference between the company's pull out date 
            price and the lowest price after that date
    '''
    price_diff = company_plp - min_price
    return price_diff


            
def main():
    
    # Execute the functions for the first industry to look at -- Food
    # Call first file (McDonalds) and read in the dates and the closing prices
    mcd_file = read_file(MCD_FILE)
    mcd_dates = mcd_file[0]
    mcd_close_price = mcd_file[1]

    # Get the max closing MCD price and the date it occured on
    mcd_max_price = get_max_price(mcd_dates, mcd_close_price)[0]
    mcd_max_date = get_max_price(mcd_dates, mcd_close_price)[1]
    
    # Get the min closing MCD price and the date it occured on 
    mcd_min_price = get_min_price(mcd_dates, mcd_close_price)[0]
    mcd_min_date = get_min_price(mcd_dates, mcd_close_price)[1]

    # Plot the MCD file with title, max & min prices, legend
    plt.show()
    mcd_plot = make_plot(mcd_dates, mcd_close_price)
    plt.plot(mcd_max_date, mcd_max_price, "*", label = mcd_max_price, 
             markersize = 12, color = "orange")
    plt.plot(mcd_min_date, mcd_min_price, "*", label = mcd_min_price, 
             markersize = 12, color = "black")
    plt.title("McDonalds Stock Prices", fontweight = "bold")
    handles, names = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(names, handles))
    plt.legend(by_label.values(), by_label.keys(),frameon=False,
                  loc='lower center', ncol=3)
    
    # Call the second file for the food industry (Starbucks) and read in 
    # the dates and closing prices
    sbux_file = read_file(SBUCKS_FILE)
    sbux_dates = sbux_file[0]
    sbux_close_prices = sbux_file[1]
    
    # Get the max prices for the SBUX data and the date it occured on
    sbux_max_price = get_max_price(sbux_dates, sbux_close_prices)[0]
    sbux_max_date = get_max_price(sbux_dates, sbux_close_prices)[1]
    
    # Get the min price for the SBUX data and the date it occured on 
    sbux_min_price = get_min_price(sbux_dates, sbux_close_prices)[0]
    sbux_min_date = get_min_price(sbux_dates, sbux_close_prices)[1]
    
    
    # Plot the SBUX file with title, max & min prices, legend
    plt.show()
    sbux_plot = make_plot(sbux_dates, sbux_close_prices)
    plt.plot(sbux_max_date, sbux_max_price, "*", label = sbux_max_price, 
             markersize = 12, color = "orange")
    plt.plot(sbux_min_date, sbux_min_price, "*", label = sbux_min_price, 
             markersize = 12, color = "black")
    plt.title("Starbucks Stock Prices", fontweight = "bold")
    handles, names = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(names, handles))
    plt.legend(by_label.values(), by_label.keys(),frameon=False,
                 loc='lower center', ncol=3)
   
    # Call the third file for the food industry (Pepsi) and read in the dates
    # and the closing prices
    pep_file = read_file(PEPSI_FILE)
    pep_dates = pep_file[0]
    pep_close_prices = pep_file[1]

    # Get the max price for PEP and the date it occured on 
    pep_max_price = get_max_price(pep_dates, pep_close_prices)[0]
    pep_max_date = get_max_price(pep_dates, pep_close_prices)[1]
    
    # Get the min price for the PEP data and the date it occured on
    pep_min_price = get_min_price(pep_dates, pep_close_prices)[0]
    pep_min_date = get_min_price(pep_dates, pep_close_prices)[1]
    
    # Plot the PEP data with title, legend, and max & min prices
    plt.show()
    pep_plot = make_plot(pep_dates, pep_close_prices)
    plt.plot(pep_max_date, pep_max_price, "*", label = pep_max_price, 
             markersize = 12, color = "orange")
    plt.plot(pep_min_date, pep_min_price, "*", label = pep_min_price, 
             markersize = 12, color = "black")
    plt.title("Pepsi Co. Stock Prices", fontweight = "bold")
    handles, names = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(names, handles))
    plt.legend(by_label.values(), by_label.keys(),frameon=False,
                 loc='lower center', ncol=3)
    
    # Execute the functions for the second industry to look at -- Oil
    # Read in teh first file (BP) and get the closing prices and dates
    bp_file = read_file(BP_FILE)
    bp_dates = bp_file[0]
    bp_close_prices = bp_file[1]
    
    # Get the max closing price for BP and the date it occured on
    bp_max_price = get_max_price(bp_dates, bp_close_prices)[0]
    bp_max_date = get_max_price(bp_dates, bp_close_prices)[1]
    
    # Get the min closing price for BP and the date it occured on
    bp_min_price = get_min_price(bp_dates, bp_close_prices)[0]
    bp_min_date = get_min_price(bp_dates, bp_close_prices)[1]
    
    # Plot the BP data with title, legend, and max & min prices
    plt.show()
    bp_plot = make_plot(bp_dates, bp_close_prices)
    plt.plot(bp_max_date, bp_max_price, "*", label = bp_max_price, 
             markersize = 12, color = "orange")
    plt.plot(bp_min_date, bp_min_price, "*", label = bp_min_price, 
             markersize = 12, color = "black")
    plt.title("BP Stock Prices", fontweight = "bold")
    handles, names = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(names, handles))
    plt.legend(by_label.values(), by_label.keys(),frameon=False,
                 loc='lower center', ncol=3)
    
    # Read in the second file (Shell) with dates and closing prices 
    shel_file = read_file(SHELL_FILE)
    shel_dates = shel_file[0]
    shel_close_prices = shel_file[1]
    
    # Get the max closing price for BP and the date it occured on
    shel_max_price = get_max_price(shel_dates, shel_close_prices)[0]
    shel_max_date = get_max_price(shel_dates, shel_close_prices)[1]

    # Get the min closing price for BP and the date it occured on
    shel_min_price = get_min_price(shel_dates, shel_close_prices)[0]
    shel_min_date = get_min_price(shel_dates, shel_close_prices)[1]
    
    # Plot the SHEL data with title, legend and min & max prices
    plt.show()
    shel_plot = make_plot(shel_dates, shel_close_prices)
    plt.plot(shel_max_date, shel_max_price, "*", label = shel_max_price,
             markersize = 12, color = "orange")
    plt.plot(shel_min_date, shel_min_price, "*", label = shel_min_price,
             markersize = 12, color = "black")
    plt.title("Shell Stock Prices", fontweight = "bold")
    handles, names = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(names, handles))
    plt.legend(by_label.values(), by_label.keys(),frameon=False,
                 loc='lower center', ncol=3)
    
    # Read in the third file in the oil industry (Exxon) and get dates 
    # and prices
    xom_file = read_file(EXXON_FILE)
    xom_dates = xom_file[0]
    xom_close_prices = xom_file[1]
    
    # Get the max price for XOM and the date it occured on
    xom_max_price = get_max_price(xom_dates, xom_close_prices)[0]
    xom_max_date = get_max_price(xom_dates, xom_close_prices)[1]
    
    # Get the min price for XOM and the date it occured on
    xom_min_price = get_min_price(xom_dates, xom_close_prices)[0]
    xom_min_date = get_min_price(xom_dates, xom_close_prices)[1]
    
    # Plot the XOM data with title, legend, and min & max prices
    plt.show()
    xom_plot = make_plot(xom_dates, xom_close_prices)
    plt.plot(xom_max_date, xom_max_price, "*", label = xom_max_price, 
             markersize = 12, color = "orange")
    plt.plot(xom_min_date, xom_min_price, "*", label = xom_min_price, 
             markersize = 12, color = "black")
    plt.title("Exxon Stock Prices", fontweight = "bold")
    handles, names = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(names, handles))
    plt.legend(by_label.values(), by_label.keys(),frameon=False,
                  loc='lower center', ncol=3)
    
    # Execute the functions for the third industry to look at -- Retail
    # Read in the first file for retail (Nike) and get the closing prices and
    # the dates 
    nke_file = read_file(NIKE_FILE)
    nke_dates = nke_file[0]
    nke_close_prices = nke_file[1]
    
    # Get the max closing NKE price and the date it occured on
    nke_max_price = get_max_price(nke_dates, nke_close_prices)[0]
    nke_max_date = get_max_price(nke_dates, nke_close_prices)[1]
    
    # Get the min closing NKE price and the date it occured on
    nke_min_price = get_min_price(nke_dates, nke_close_prices)[0]
    nke_min_date = get_min_price(nke_dates, nke_close_prices)[1]    
    
    # Plot the NKE data with title, legend, and min & max prices
    plt.show()
    nke_plot = make_plot(nke_dates, nke_close_prices)
    plt.plot(nke_max_date, nke_max_price, "*", label = nke_max_price, 
             markersize = 12, color = "orange")
    plt.plot(nke_min_date, nke_min_price, "*", label = nke_min_price, 
             markersize = 12, color = "black")
    plt.title("Nike Stock Prices", fontweight = "bold")
    handles, names = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(names, handles))
    plt.legend(by_label.values(), by_label.keys(),frameon=False,
                 loc='lower center', ncol=3)
    
    # Read in the second file from the retail industry (Adidas) and get the 
    # dates and closing prices
    ady_file = read_file(ADIDAS_FILE)
    ady_dates = ady_file[0]
    ady_close_prices = ady_file[1]
    
    # Get the max closing ADY price and the date it occured on
    ady_max_price = get_max_price(ady_dates, ady_close_prices)[0]
    ady_max_date = get_max_price(ady_dates, ady_close_prices)[1]
    
    # Get the min closing ADY price and the date it occured on
    ady_min_price = get_min_price(ady_dates, ady_close_prices)[0]
    ady_min_date = get_min_price(ady_dates, ady_close_prices)[1]
    
    # Plot the ADY data with title, legend, and min & max prices
    plt.show()
    ady_plot = make_plot(ady_dates, ady_close_prices)
    plt.plot(ady_max_date, ady_max_price, "*", label = ady_max_price, 
             markersize = 12, color = "orange")
    plt.plot(ady_min_date, ady_min_price, "*", label = ady_min_price, 
             markersize = 12, color = "black")
    plt.title("Adidas Stock Prices", fontweight = "bold")
    handles, names = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(names, handles))
    plt.legend(by_label.values(), by_label.keys(),frameon=False,
                  loc='lower center', ncol=3)
    
    # Read in the last file from the retail industry (Canada Goose) and get
    # the closing prices and dates
    goos_file = read_file(GOOSE_FILE)
    goos_dates = goos_file[0]
    goos_close_prices = goos_file[1]
    
    # Get the max closing GOOS price and the date it occured on
    goos_max_price = get_max_price(goos_dates, goos_close_prices)[0]
    goos_max_date = get_max_price(goos_dates, goos_close_prices)[1]
    
    # Get the min closing GOOS price and the date it occured on
    goos_min_price = get_min_price(goos_dates, goos_close_prices)[0]
    goos_min_date = get_min_price(goos_dates, goos_close_prices)[1]
    
    # Plot the GOOS data with title, legend, and min & max prices
    plt.show()
    goos_plot = make_plot(goos_dates, goos_close_prices)
    plt.plot(goos_max_date, goos_max_price, "*", label = goos_max_price, 
             markersize = 12, color = "orange")
    plt.plot(goos_min_date, goos_min_price, "*", label = goos_min_price, 
             markersize = 12, color = "black")
    plt.title("Canada Goose Stock Prices", fontweight = "bold")
    handles, names = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(names, handles))
    plt.legend(by_label.values(), by_label.keys(),frameon=False,
                  loc='lower center', ncol=3)
    
    # shell
    # read in the data
    dates, closing_pr = read_file(SHELL_FILE)
   
    # find the lowest price reached after the day the company pulled business
    # out of Russia
    min_price = find_min_price_after_PLP(dates, closing_pr, SHELL_PLP)
   
    # find the difference between the price on the day the company pulled out
    # and the lowest price from before
    shell_diff = find_diff(SHELL_PLP, min_price)

    # plot the difference in a bar chart
    plt.show()
    plt.bar("Shell", shell_diff, color = "yellow")
   
# now we repeat the process for the rest of the companies:
   
#BP
    dates, closing_pr = read_file(BP_FILE)
    min_price = find_min_price_after_PLP(dates, closing_pr, BP_PLP)
    bp_diff = find_diff(BP_PLP, min_price)
    plt.bar("BP", bp_diff, color = "goldenrod")

#exxon
    dates, closing_pr = read_file(EXXON_FILE)
    min_price = find_min_price_after_PLP(dates, closing_pr, EXXON_PLP)
    ex_diff = find_diff(EXXON_PLP, min_price)
    plt.bar("exxon", ex_diff, color = "gold")
   
#adidas
    dates, closing_pr = read_file(ADIDAS_FILE)
    min_price = find_min_price_after_PLP(dates, closing_pr, ADIDAS_PLP)
    ad_diff = find_diff(ADIDAS_PLP, min_price)
    plt.bar("Adidas", ad_diff, color = "skyblue")
   
#nike
    dates, closing_pr = read_file(NIKE_FILE)  
    min_price = find_min_price_after_PLP(dates, closing_pr, NIKE_PLP)
    nike_diff = find_diff(NIKE_PLP, min_price)
    plt.bar("nike", nike_diff, color = "dodgerblue")
   
#canada goose
   
    dates, closing_pr = read_file(GOOSE_FILE)    
    min_price = find_min_price_after_PLP(dates, closing_pr, GOOSE_PLP)
    goo_diff = find_diff(GOOSE_PLP, min_price)
    plt.bar("Canada Goose", goo_diff, color = "royalblue")

#mcdonalds

    dates, closing_pr = read_file(MCD_FILE)    
    min_price = find_min_price_after_PLP(dates, closing_pr, MCD_PLP)
    mcd_diff = find_diff(MCD_PLP, min_price)
    plt.bar("McDonalds", mcd_diff, color = "firebrick")

#pepsi

    dates, closing_pr = read_file(PEPSI_FILE)    
    min_price = find_min_price_after_PLP(dates, closing_pr, PEPSI_PLP)
    pep_diff = find_diff(PEPSI_PLP, min_price)
    plt.bar("Pepsi", pep_diff, color = "orangered")

#starbucks

    dates, closing_pr = read_file(SBUCKS_FILE)  
    min_price = find_min_price_after_PLP(dates, closing_pr, SBUCKS_PLP)
    sbx_diff = find_diff(SBUCKS_PLP, min_price)
    plt.bar("Starbucks", sbx_diff, color = "salmon")

    # customize graph
   
    plt.xticks(rotation = 60)
    plt.xlabel("Company name")
    plt.ylabel("Price drop")
    plt.title("Difference in stock price after companies pulled out")
   
    # find the average difference per sector - one for gas, retail, and food
   
    gas_avg = (shell_diff + bp_diff + ex_diff) / 3
    retail_avg = (ad_diff + nike_diff + goo_diff) / 3
    food_avg = (mcd_diff + pep_diff + sbx_diff) / 3
   
    # plot them
    plt.show()
    plt.bar("Gas", gas_avg, color = "khaki")
    plt.bar("Retail", retail_avg, color = "cornflowerblue")
    plt.bar("Food", food_avg, color = "tomato")
   
    plt.xlabel("Sector")
    plt.ylabel("Average price drop")
    plt.title("Average difference in stock price for each sector")
    
    
main()
