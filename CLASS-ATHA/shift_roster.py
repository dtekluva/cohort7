import datetime

start_year, start_month, start_day = 2015, 1, 1
end_year, end_month, end_day = 2015, 2, 1

start_date = datetime.date(start_year, start_month, start_day)
end_date = datetime.date(end_year, end_month, end_day)

days = [start_date + datetime.timedelta(days=x) for x in range((end_date-start_date).days + 1)]

days_string = []
available_teams = ["Team A", "Team B", "Team C", "Team D"]

teams_arranged_in_patterns = []

for index, day in enumerate(days):

    days_string.append(day.strftime('%Y-%m-%d'))
    # print(day.strftime('%Y-%m-%d'))

    team_due_index = index%4
    team_due = available_teams[team_due_index]

    teams_arranged_in_patterns.append(team_due)

shift_roster_dict = dict(zip(days_string, teams_arranged_in_patterns))
