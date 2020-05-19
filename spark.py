# %%
import pandas as pd
import os
import glob
import xlwt

MEETING_POINTS = 20
SOCIAL_POINTS = 10
LUNCH_BUDDY_POINTS = 5

# %%
def parse_csv():
    """
    Parse the csv files in their respective directories and
    return as lists of DataFrames.
    """
    parsed_dues = pd.read_csv('data/Dues.csv')

    # Get the full system path. Windows seems to really care about this.
    meetings_path = os.path.join(os.getcwd(), "data/meetings")
    # Create a list of all the csv files in the directory
    meetings = glob.glob(os.path.join(meetings_path, '*.csv'))
    # Finally, parse all the csv files and place in a list
    parsed_meetings = [pd.read_csv(meeting) for meeting in meetings]

    # The same for socials in the data/socials directory
    socials_path = os.path.join(os.getcwd(), "data/socials")
    socials = glob.glob(os.path.join(socials_path, '*.csv'))
    parsed_socials = [pd.read_csv(social) for social in socials]

    return parsed_dues, parsed_meetings, parsed_socials

def construct_roster(dues):
    """
    Constructs a roster DataFrame from the dues form.
    """

    roster = pd.DataFrame()
    # Just take the columns from the dues form
    roster["Name"] = dues["Name"]
    roster["EID"] = dues["EID"]
    # Add a column for spark points with default 0
    roster["Spark Points"] = 0

    return roster

def check_attendance(eid, meeting):
    """
    Checks the attendance of an EID for a given meeting.
    """
    
    # Iterate through list of EIDs
    for index, attendee in meeting.iterrows():
        if attendee["What's your EID?"].lower() == eid.lower():
            return True
    return False    

# %%
DUES, MEETINGS, SOCIALS = parse_csv()
ROSTER = construct_roster(DUES)
# %%

for index, member in ROSTER.iterrows():
    for meeting in MEETINGS:
        if check_attendance(member["EID"], meeting):
            ROSTER.at[index, "Spark Points"] += MEETING_POINTS
    for social in SOCIALS:
        if check_attendance(member["EID"], social):
            ROSTER.at[index, "Spark Points"] += SOCIAL_POINTS

# %%
print(ROSTER)