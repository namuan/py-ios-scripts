import os

import reminders
from datetime import datetime, timedelta

outdir = os.path.expanduser("~/Documents/Reminders")
try:
    os.mkdir(outdir)
except FileExistsError:
    pass

def get_and_save_recent_reminders(calendar_id, days=7, filename='recent_reminders.md'):
    # Get the specific calendar
    calendar = reminders.get_calendar(calendar_id)

    if not calendar:
        print(f"No calendar found with ID: {calendar_id}")
        return

    print(f"Retrieving reminders in '{calendar.title}' calendar for the last {days} days...")

    # Get all reminders from this calendar
    calendar_reminders = reminders.get_reminders(calendar=calendar)

    if not calendar_reminders:
        print("No reminders found in this calendar.")
        return

    # Calculate the date 7 days ago
    seven_days_ago = datetime.now() - timedelta(days=days)

    recent_reminders = []
    for reminder in calendar_reminders:
        if reminder.completed and reminder.completion_date:
            if reminder.completion_date >= seven_days_ago:
                recent_reminders.append(reminder)
        elif not reminder.due_date or reminder.due_date >= seven_days_ago:
            recent_reminders.append(reminder)

    if not recent_reminders:
        print(f"No reminders found in the last {days} days.")
        return

    # Create Markdown content
    markdown_content = f"# Recent Reminders in '{calendar.title}' Calendar\n\n"
    markdown_content += f"*Last {days} days (as of {datetime.now().strftime('%Y-%m-%d %H:%M')})*\n\n"

    for reminder in recent_reminders:
        markdown_content += f"- **{reminder.title}**\n"
        markdown_content += "\n"

    # Generate filename with current date
    filename = f"reminders_{datetime.now().strftime('%Y%m%d')}.md"
    filepath = os.path.join(outdir, filename)

    # Save to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Reminders list saved to {filepath}")

    # Also print to console
    print("\nRecent Reminders:")
    print(markdown_content)


# Calendar ID for the "Bookmarks" calendar
bookmarks_calendar_id = "9F7D5A87-C671-41A6-BE0B-C6038AC7E9B8"

# Run the function
get_and_save_recent_reminders(bookmarks_calendar_id)
