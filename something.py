def check_status(status, gvar):
    from datetime import date
    now = date.today()
    Date = int(now.strftime("%Y"))

    if status == 'COMPLETE':
        goal_status = 'achieved'
    elif status == "CANCELLED":
        goal_status = 'cancelled'
    elif Date >= 2021:
        goal_status = 'out of frame'
    elif status == 'ACTIVE':
        if gvar <= -30:
            goal_status = "ahead of plan"
        elif gvar >= -30 and gvar <= 0:
            goal_status = "on track"
        elif gvar >= 1 and gvar <= 30:
            goal_status = 'at risk'
        elif gvar >= 30:
            goal_status = 'delayed'
        else:
            goal_status = 'other'
    return goal_status
    



def state(status, gvar):
    if status == True and gvar is not None:
        try:
            Gvar = int(gvar)
        except:
            print('gvar is not an integer')
        goal_status = check_status(status, Gvar)
        print(goal_status)


