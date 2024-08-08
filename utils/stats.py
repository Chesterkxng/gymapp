from subscription.models import Subscription
from session.models import Session
from django.db.models.functions import TruncMonth
from django.db.models import Count
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
                    


