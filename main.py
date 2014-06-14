


ACTIVITY_THRESHOLD = .5
LAST_YEARS = 3


def get_facebook_group_members():
    return [ {"name":"Victor J Wang"} ]

def calculate_active_score(member):
    # Has attended FB event.
    # Has attended eventbrite event.
    return 0


if __name__ == "__main__":
    # Get all Facebook Group members.
    members = get_facebook_group_members()
    
    # Calculate active "score" for each member.
    # Print out name if score is below threshold.
    for member in members:
        score = calculate_active_score(member)
        if score < ACTIVITY_THRESHOLD:
            print member["name"]
