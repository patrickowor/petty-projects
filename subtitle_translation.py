try:
    file = input('enter a file link: ')
    new = input('convert to which format :\n1) .srt\n==> ')
    
    try:
        f_name, f_type = file.split('.')
    except:
        print('not a file')
    with open(file, 'r') as vtt:
        if new == '1':
            with open(f_name+'.srt', 'w') as result:
                t = 0
                for line in vtt:
                    if len(line) == 1:
                        t += 1
                        result.write(f'\n{t}\n')
                    else:
                        if t >= 1:
                            line =  line.replace('.', ',').replace('.&lt;/i&gt;','').replace('&lt;/i&gt;','').replace('&lt;i&gt;','')
                            try:
                                if int(line.split(',')[-1]):
                                    line = line
                            except:
                                l = line.replace('\n', '')
                                line = f"<i> { l } </i>"  + " \n"
                            result.write(line)
        print('task complete')        
       
                  
                             
                                        
except:
    print('error occured check your input values')           