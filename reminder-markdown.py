import os
import reminders
from datetime import datetime, timedelta

outdir = os.path.expanduser("~/Documents/Reminders")
try:
    os.mkdir(outdir)
except FileExistsError:
    pass

def get_and_save_recent_reminders(calendar_id):
    # Get the specific calendar
    calendar = reminders.get_calendar(calendar_id)

    if not calendar:
        print(f"No calendar found with ID: {calendar_id}")
        return

    print(f"Retrieving reminders in '{calendar.title}' calendar from yesterday and earlier...")

    # Get all reminders from this calendar
    calendar_reminders = reminders.get_reminders(calendar=calendar)

    if not calendar_reminders:
        print("No reminders found in this calendar.")
        return

    # Calculate yesterday's date (midnight)
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    filtered_reminders = []
    for reminder in calendar_reminders:
        if reminder.completed and reminder.completion_date:
            if reminder.completion_date < today:
                filtered_reminders.append(reminder)
        elif reminder.due_date and reminder.due_date < today:
            filtered_reminders.append(reminder)

    if not filtered_reminders:
        print("No reminders found from yesterday or earlier.")
        return

    # Create Markdown content
    markdown_content = f"# Reminders in '{calendar.title}' Calendar\n\n"
    markdown_content += f"*From yesterday and earlier (as of {datetime.now().strftime('%Y-%m-%d %H:%M')})*\n\n"

    for reminder in filtered_reminders:
        markdown_content += f"- **{reminder.title}**\n"
        markdown_content += "\n"

    # Generate filename with current date
    filename = f"reminders_{datetime.now().strftime('%Y%m%d')}.md"
    filepath = os.path.join(outdir, filename)

    # Save to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Reminders list saved to {filepath}")

    deleted_count = 0
    for reminder in filtered_reminders:
        reminders.delete_reminder(reminder)
        deleted_count += 1

    # Also print to console
    print("\nFiltered Reminders:")
    print(markdown_content)
    print(f"\nTotal reminders deleted: {deleted_count}")

# Calendar ID for the "Bookmarks" calendar
bookmarks_calendar_id = "9F7D5A87-C671-41A6-BE0B-C6038AC7E9B8"

# Run the function
get_and_save_recent_reminders(bookmarks_calendar_id)

