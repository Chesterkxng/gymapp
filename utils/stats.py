from subscription.models import Subscription
from session.models import Session, Package
from django.db.models.functions import TruncMonth, TruncHour
from django.db.models import Count, Sum, TimeField
from datetime import datetime, date
from collections import defaultdict

# class for Subscription app

class SubscriptionStats:
    today = datetime.now().date()

    # function that get the total amount of pending subs
    def get_pending_subs():
        today = datetime.now().date()
        return Subscription.objects.filter(endDate__gte=today).count()

    # function that return a dict of subs by type
    def get_pending_subs_by_type():
        today = datetime.now().date()
        result = defaultdict(int)   # init a dict of int 
        pending_subs = Subscription.objects.filter(endDate__gte=today) # get 
        for pending_sub in pending_subs:
            package_name = pending_sub.package.name
            result[package_name] += 1
        return dict(result)

    def get_monthly_subs():
            current_year = datetime.now().year
            month_names = [
                'January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December'
            ]
            
            # Get subscription counts by month
            subscriptions_by_month = Subscription.objects.annotate(
                month=TruncMonth('startDate')
            ).filter(
                startDate__year=current_year
            ).values(
                'month'
            ).annotate(
                count=Count('id')
            ).order_by('month')

            # Create a dictionary to store counts for each month
            monthly_counts = {month: 0 for month in month_names}

            # Update dictionary with actual counts from query
            for subscription in subscriptions_by_month:
                month_name = subscription['month'].strftime('%B')
                monthly_counts[month_name] = subscription['count']

            # Convert dictionary to a list of dicts
            result = [{'month': month, 'count': monthly_counts[month]} for month in month_names]

            return result
                    
class SessionStats:

    # function that get the total amount of pending subs
    def get_sessions_in_current_month():
        today = date.today()
        # Get the first and last day of the current month
        first_day_of_month = date(today.year, today.month, 1)
        if today.month == 12:
            last_day_of_month = date(today.year + 1, 1, 1)
        else:
            last_day_of_month = date(today.year, today.month + 1, 1)

        # Filter the sessions based on the date
        return Session.objects.filter(
            date__gte=first_day_of_month,
            date__lt=last_day_of_month
        ).count()


    # function that return a dict of subs by type
    def get_sessions_in_current_month_by_type():
        today = date.today()
        # Get the first and last day of the current month
        first_day_of_month = date(today.year, today.month, 1)
        if today.month == 12:
            last_day_of_month = date(today.year + 1, 1, 1)
        else:
            last_day_of_month = date(today.year, today.month + 1, 1)

        # Filter the sessions based on the date
        sessions = Session.objects.filter(
            date__gte=first_day_of_month,
            date__lt=last_day_of_month)

        result = defaultdict(int)   # init a dict of int 
        for session in sessions:
            package_name = session.package.name
            result[package_name] += 1
        return dict(result)

    def get_monthly_sessions():
            current_year = datetime.now().year
            month_names = [
                'January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December'
            ]
            
            # Get subscription counts by month
            sessions_by_month = Session.objects.annotate(
                month=TruncMonth('date')
            ).filter(
                date__year=current_year
            ).values(
                'month'
            ).annotate(
                count=Count('id')
            ).order_by('month')

            # Create a dictionary to store counts for each month
            monthly_counts = {month: 0 for month in month_names}

            # Update dictionary with actual counts from query
            for session in sessions_by_month:
                month_name = session['month'].strftime('%B')
                monthly_counts[month_name] = session['count']

            # Convert dictionary to a list of dicts
            result = [{'month': month, 'count': monthly_counts[month]} for month in month_names]

            return result
    
    # Function that get finance of current month
    def get_current_month_sessions_amount():
        today = date.today()
        # Get the first and last day of the current month
        first_day_of_month = date(today.year, today.month, 1)
        if today.month == 12:
            last_day_of_month = date(today.year + 1, 1, 1)
        else:
            last_day_of_month = date(today.year, today.month + 1, 1)

        # Filter the sessions based on the date
        sessions = Session.objects.filter(
            date__gte=first_day_of_month,
            date__lt=last_day_of_month
        )
        amount = 0
        for session in sessions:
            amount += session.package.amount
        return amount

    # function that get finance of current month by type
    def get_current_month_sessions_amount_by_type():
        today = date.today()
        # Get the first and last day of the current month
        first_day_of_month = date(today.year, today.month, 1)
        if today.month == 12:
            last_day_of_month = date(today.year + 1, 1, 1)
        else:
            last_day_of_month = date(today.year, today.month + 1, 1)

        # Filter the sessions based on the date
        sessions = Session.objects.filter(
            date__gte=first_day_of_month,
            date__lt=last_day_of_month)

        result = defaultdict(int)   # init a dict of int 
        for session in sessions:
            package_name = session.package.name
            result[package_name] += session.package.amount
        return dict(result)

    def get_monthly_sessions_count_per_type():
        current_year = datetime.now().year

        # Get all packages
        packages = Package.objects.values_list('name', flat=True)

        # Initialize the result dictionary
        result = {package: [0] * 12 for package in packages}

        # Annotate sessions by month and package, then count them
        session_counts = Session.objects.filter(date__year=current_year).annotate(
            month=TruncMonth('date')
        ).values(
            'month', 'package__name'
        ).annotate(
            count=Count('id')
        ).order_by('month')

        # Populate the result with the actual counts
        for session in session_counts:
            month_index = session['month'].month - 1
            package_name = session['package__name']
            result[package_name][month_index] = session['count']

        # Convert the result dictionary to a list of dictionaries
        result_list = [{'name': package, 'data': counts} for package, counts in result.items()]

        return result_list

    def get_monthly_amounts_per_type():
        current_year = datetime.now().year

        # Initialize a dictionary to hold the data for each package
        data = {}

        # Get the list of all packages
        packages = Session.objects.values_list('package__name', flat=True).distinct()

        # Iterate over each package and initialize the data list for each month
        for package in packages:
            data[package] = [0] * 12

        # Aggregate the amounts per package per month
        amounts_by_month = Session.objects.filter(
            date__year=current_year
        ).annotate(
            month=TruncMonth('date')
        ).values(
            'month', 'package__name'
        ).annotate(
            total_amount=Sum('package__amount')
        ).order_by('month')

        # Fill the data dictionary with the actual amounts
        for entry in amounts_by_month:
            month_index = entry['month'].month - 1  # 0-indexed month
            package_name = entry['package__name']
            data[package_name][month_index] = entry['total_amount']

        # Convert the dictionary into the desired list of dicts format
        result = [{'name': package, 'data': amounts} for package, amounts in data.items()]

        return result

    def get_sessions_by_hour():
        sessions_by_hour = (
        Session.objects.annotate(hour_truncated=TruncHour('hour', output_field=TimeField()))
        .values('hour_truncated')
        .annotate(count=Count('id'))
        .order_by('hour_truncated')
        )   
        hours = []
        counts = []
        for session in sessions_by_hour:
            hours.append(session['hour_truncated'].strftime('%H:00'))  # Format the hour
            counts.append(session['count'])
        
        return {'hours': hours, 'counts': counts}