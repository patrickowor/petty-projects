""" here is the code for the date all you need to do is import the get_date function I created and pass in the value like '3 days ago', '3 years ago' etc and it would return a value  """

""" there is an example at the very end of this code please delete it later so you can call the get_date function from anywhere """


# this is the date gotten from your web scrapper
def get_date(date):
    date_list = date.split('') if '-' in date else date.split(' ')
    scraped_date = date
    
    
    
    months ={'january':{
        'index' : 1,
        'days' : 31 ,
        'month_before':'december',
    },
    'febuary':{
        'index' : 2,
        'days' : 24 ,
        'month_before':'january',
    },
    'march':{
        'index' : 3,
        'days' : 31 ,
        'month_before':'february',
    },
    'april':{
        'index' : 4,
        'days' : 30 ,
        'month_before':'march',
    },
    'may':{
        'index' : 5,
        'days' : 31 ,
        'month_before':'april',
    },
    'june':{
        'index' : 6,
        'days' : 30,
        'month_before':'may',
    },
    'july':{
        'index' : 7,
        'days' : 31 ,
        'month_before':'june',
    },
    'august':{
        'index' : 8,
        'days' : 31 ,
        'month_before':'july',
    },
    'september':{
        'index' : 9,
        'days' : 30 ,
        'month_before':'august',
    },
    'october':{
        'index' : 10,
        'days' : 31 ,
        'month_before':'september',
    },
    'november':{
        'index' : 11,
        'days' : 30 ,
        'month_before':'october',
    },
    'december':{
        'index' : 12,
        'days' : 31 ,
        'month_before':'november',
    }
    }
    
    
    
    from datetime import datetime
    
    
    _date =datetime.today()
    today_date = _date.strftime('%d-%B-%Y')
    last_year =str( int(_date.strftime('%Y')) - 1)
    today_date_list = today_date.split('-')
    
    
    
    
    
    if 'days' in scraped_date:
        try:
            calc = int(today_date_list[0]) -int(date_list[0]) 
            if calc < 0:
                raise error
            result = [calc, today_date_list[1], today_date_list[2]]
        except:
            month = months[today_date_list[1].lower()]['month_before']
            extra_days  = months[month]['days']
            calc = (extra_days +int(today_date_list[0])) - int(date_list[0])
            result = [calc, month, today_date_list[2]]
        
    elif 'year' in scraped_date:
        this_year = int(today_date_list[2])
        calc = this_year - int(date_list[0])
        result = [today_date_list[0],today_date_list[1],calc]
    elif 'month' in scraped_date or 'months' in scraped_date:
        today_index = months[today_date_list[1].lower()]['index']
        calc = int(today_index) - int(date_list[0])
        for month in months:
                if calc < 0:
                    new_calc = calc + 12
                    year = int(today_date_list[2])
                    if months[month]['index'] == new_calc:
                        year -= 1
                        result = [today_date_list[0], month,last_year]
                elif calc > 0:
                    if months[month]['index'] == calc:
                        result =[today_date_list[0],month, today_date_list[2]]
    final = datetime( int(result[2])   ,months[result[1]]['index'],  int(result[0])  )     
    return final 
        
print(get_date('19 days ago'))  