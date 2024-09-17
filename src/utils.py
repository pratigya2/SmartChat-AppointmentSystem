# src/utils.py

import parsedatetime as pdt
import datetime

def parse_date(input_date: str) -> str:
    cal = pdt.Calendar()
    current_date = datetime.datetime.now()
    time_struct, parse_status = cal.parse(input_date, current_date)
    
    if parse_status:
        parsed_date = datetime.datetime(*time_struct[:6])
        formatted_date = parsed_date.strftime('%Y-%m-%d')
        return formatted_date
    else:
        raise ValueError("Could not parse the date.")
