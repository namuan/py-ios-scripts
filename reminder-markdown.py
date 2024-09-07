import reminders
from datetime import datetime, timedelta


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
        status = "x" if reminder.completed else " "
        due_date = reminder.due_date.strftime("%Y-%m-%d %H:%M") if reminder.due_date else "No due date"
        completion_date = reminder.completion_date.strftime(
            "%Y-%m-%d %H:%M") if reminder.completion_date else "Not completed"

        markdown_content += f"- [{status}] **{reminder.title}**\n"
        markdown_content += f"  - Due: {due_date}\n"
        markdown_content += f"  - Completed: {completion_date}\n"
        if reminder.notes:
            markdown_content += f"  - Notes: {reminder.notes}\n"
        markdown_content += "\n"

    # Save to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Reminders list saved to {filename}")

    # Also print to console
    print("\nRecent Reminders:")
    print(markdown_content)


# Calendar ID for the "Bookmarks" calendar
bookmarks_calendar_id = "9F7D5A87-C671-41A6-BE0B-C6038AC7E9B8"

# Run the function
get_and_save_recent_reminders(bookmarks_calendar_id)
