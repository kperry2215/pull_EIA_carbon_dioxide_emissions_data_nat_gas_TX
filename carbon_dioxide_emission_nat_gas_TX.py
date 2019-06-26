import eia
import pandas as pd

def retrieve_time_series(api, series_ID):
    """
    Return the time series dataframe, based on API and unique Series ID
    """
    #Retrieve Data By Series ID 
    series_search = api.data_by_series(series=series_ID)
    ##Create a pandas dataframe from the retrieved time series
    df = pd.DataFrame(series_search)
    return df

def main():
    """
    Run main script
    """
    #Create EIA API using your specific API key
    api_key = "YOUR API KEY HERE"
    api = eia.API(api_key)
    #Declare desired series ID
    series_ID='EMISS.CO2-TOTV-TT-NG-TX.A'
    df=retrieve_time_series(api, series_ID)
    #Print the returned dataframe df
    print(df)

if __name__== "__main__":
    main()

"""
        Total carbon dioxide emissions from all sectors, natural gas, Texas (million metric tons CO2)
1980                                           214.237163                                            
1981                                           205.069396                                            
1982                                           177.723591                                            
1983                                           169.059890                                            
1984                                           180.060660                                            
1985                                           178.186725                                            
1986                                           167.965480                                            
1987                                           173.925345                                            
1988                                           185.375988                                            
1989                                           195.629601                                            
1990                                           195.024469                                            
1991                                           191.806929                                            
1992                                           188.455361                                            
1993                                           196.532143                                            
1994                                           193.195241                                            
1995                                           200.739390                                            
1996                                           212.532702                                            
1997                                           210.401856                                            
1998                                           217.578472                                            
1999                                           205.526470                                            
2000                                           227.249651                                            
2001                                           219.856674                                            
2002                                           223.234514                                            
2003                                           209.561714                                            
2004                                           202.191500                                            
2005                                           181.055064                                            
2006                                           180.434067                                            
2007                                           184.506801                                            
2008                                           185.778455                                            
2009                                           177.408633                                            
2010                                           186.222804                                            
2011                                           191.900939                                            
2012                                           200.310049                                            
2013                                           208.881640                                            
2014                                           204.718832                                            
2015                                           215.814051                                            
2016                                           209.689272                                            


"""