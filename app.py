from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def reading_calculator():
    if request.method == 'POST':
        print("Form submitted!")  # Debug line
        
        # Get form data
        total_pages = int(request.form['total_pages'])
        pages_read = int(request.form['pages_read'])
        time_value = int(request.form['time_value'])
        time_unit = request.form['time_unit']
        start_date = request.form['start_date']
        
        print(f"Total pages: {total_pages}")  # Debug line
        
        # Convert time to minutes for calculation
        time_in_minutes = {
            'minutes': time_value,
            'hours': time_value * 60,
            'days': time_value * 60 * 24
        }[time_unit]
        
        # Calculate reading rate (pages per minute)
        pages_per_minute = pages_read / time_in_minutes
        
        # Calculate total time needed in minutes
        total_minutes_needed = total_pages / pages_per_minute
        
        # Convert to different time units
        hours = total_minutes_needed / 60
        days = hours / 24
        weeks = days / 7
        months = days / 30.44
        years = days / 365.25
        
        # Calculate finish date
        start = datetime.strptime(start_date, '%Y-%m-%d')
        finish = start + timedelta(days=days)
        
        print("About to render result.html")  # Debug line
        
        return render_template('result.html', 
                             total_pages=total_pages,
                             hours=round(hours, 2),
                             days=round(days, 2),
                             weeks=round(weeks, 2),
                             months=round(months, 2),
                             years=round(years, 2),
                             start_date=start.strftime('%B %d, %Y'),
                             finish_date=finish.strftime('%B %d, %Y'),
                             finish_date_short=finish.strftime('%Y-%m-%d'))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)