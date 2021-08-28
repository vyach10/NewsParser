from datetime import datetime

def date_format(posted_at):
    
    posted_at = posted_at.split(" ")
    
    if int(posted_at[0]) < 10: posted_at[0] = '0' + posted_at[0]
    
    if posted_at[1].lower() == 'января': posted_at[1] = '01'
    if posted_at[1].lower() == 'февраля': posted_at[1] = '02'
    if posted_at[1].lower() == 'марта': posted_at[1] = '03'
    if posted_at[1].lower() == 'апреля': posted_at[1] = '04'
    if posted_at[1].lower() == 'мая': posted_at[1] = '05'
    if posted_at[1].lower() == 'июня': posted_at[1] = '06'
    if posted_at[1].lower() == 'июля': posted_at[1] = '07'
    if posted_at[1].lower() == 'августа': posted_at[1] = '08'
    if posted_at[1].lower() == 'сентября': posted_at[1] = '09'
    if posted_at[1].lower() == 'октября': posted_at[1] = '10'
    if posted_at[1].lower() == 'ноября': posted_at[1] = '11'
    if posted_at[1].lower() == 'декабря': posted_at[1] = '12'
    date = ""
    for i in posted_at:
        date += i
        date += "."
    return(datetime.strptime(date[0:len(date)-1], "%d.%m.%Y")) 

#print(date_format('3 Февраля 2021'))