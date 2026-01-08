from flask import Flask, render_template, request
from datetime import datetime, timedelta
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def reading_calculator():
    if request.method == 'POST':
        try:
            # Get form data
            total_pages = int(request.form['total_pages'])
            pages_per_session = int(request.form['pages_per_session'])
            session_duration = int(request.form['session_duration'])
            time_unit = request.form['time_unit']
            sessions_per_week = int(request.form['sessions_per_week'])
            start_date = request.form['start_date']
            
            print(f"Received: pages={total_pages}, pages/session={pages_per_session}, duration={session_duration} {time_unit}, sessions/week={sessions_per_week}")
            
            # Calculate total sessions needed
            total_sessions_needed = math.ceil(total_pages / pages_per_session)
            
            # Calculate total weeks needed
            weeks_needed = total_sessions_needed / sessions_per_week
            
            # Calculate total days (weeks * 7)
            total_days = weeks_needed * 7
            
            # Convert to other time units
            hours = (session_duration * total_sessions_needed) / 60 if time_unit == 'minutes' else session_duration * total_sessions_needed
            days = total_days
            months = weeks_needed / 4.345  # Average weeks per month
            years = weeks_needed / 52
            
            # Calculate finish date
            start = datetime.strptime(start_date, '%Y-%m-%d')
            finish = start + timedelta(days=total_days)
            
            print(f"Calculations: sessions={total_sessions_needed}, weeks={weeks_needed}, finish={finish}")
            
            return render_template('result.html', 
                                 total_pages=total_pages,
                                 total_sessions=total_sessions_needed,
                                 hours=round(hours, 2),
                                 days=round(days, 2),
                                 weeks=round(weeks_needed, 2),
                                 months=round(months, 2),
                                 years=round(years, 2),
                                 start_date=start.strftime('%B %d, %Y'),
                                 finish_date=finish.strftime('%B %d, %Y'),
                                 sessions_per_week=sessions_per_week)
            
        except Exception as e:
            print(f"ERROR: {e}")
            import traceback
            traceback.print_exc()
            return f"Error: {e}"
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)