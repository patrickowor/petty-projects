df1= [{'country_code':'+234',
            'country_name':'Nigeria'}]
df2 = [{'name':'Patrick',
            'dept':'computer',
            'country_code':'+234'
}]

# looping through 
for df1_dic in df1:
    if df2[0]['country_code']== df1_dic['country_code']:
        print('your country name is ', end='')
        print(df1_dic['country_name'])