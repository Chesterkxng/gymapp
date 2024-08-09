from django.shortcuts import render
from utils.stats import SubscriptionStats, SessionStats

# Create your views here.
def subscriptions(request):
    pending_subcriptions = SubscriptionStats.get_pending_subs()
    pending_subscriptions_by_type = SubscriptionStats.get_pending_subs_by_type()
    monthly_subs = SubscriptionStats.get_monthly_subs()

    # formating data for charts
    pending_subscriptions_donut_labels= list(pending_subscriptions_by_type.keys())
    pending_subscriptions_donut_series = list(pending_subscriptions_by_type.values())
    monthly_subs_count = [month['count'] for month in monthly_subs]
    context = {
        "pending_subcriptions": pending_subcriptions,
        "pending_subscriptions_by_type": pending_subscriptions_by_type,
        "pending_subscriptions_donut_labels": pending_subscriptions_donut_labels,
        "pending_subscriptions_donut_series": pending_subscriptions_donut_series,
        "monthly_subs_count": monthly_subs_count,
    }
    
    return render(request, 'dashboard/subscription.html', context)

def sessions(request):
    current_month_sessions = SessionStats.get_sessions_in_current_month()
    current_month_sessions_by_type = SessionStats.get_sessions_in_current_month_by_type()
    monthly_sessions = SessionStats.get_monthly_sessions()
    sessions_by_hour = SessionStats.get_sessions_by_hour()
    # Finances
    current_month_sessions_amount = SessionStats.get_current_month_sessions_amount()
    current_month_sessions_amount_by_type = SessionStats.get_current_month_sessions_amount_by_type()
    sessions_count_per_type = SessionStats.get_monthly_sessions_count_per_type()
    monthly_amounts_per_type = SessionStats.get_monthly_amounts_per_type()


    # formating data for charts
    current_month_sessions_donut_labels= list(current_month_sessions_by_type.keys())
    current_month_sessions_donut_series = list(current_month_sessions_by_type.values())
    monthly_sessions_count = [month['count'] for month in monthly_sessions]

    current_month_sessions_amount_donut_labels= list(current_month_sessions_amount_by_type.keys())
    current_month_sessions_amount_donut_series = list(current_month_sessions_amount_by_type.values())




    context = {
        "current_month_sessions": current_month_sessions,
        "current_month_sessions_by_type": current_month_sessions_by_type,
        "current_month_sessions_donut_labels":  current_month_sessions_donut_labels,
        "current_month_sessions_donut_series": current_month_sessions_donut_series,
        "monthly_sessions_count": monthly_sessions_count,
        "current_month_sessions_amount": current_month_sessions_amount,
        "current_month_sessions_amount_by_type": current_month_sessions_amount_by_type,
        "current_month_sessions_amount_donut_labels": current_month_sessions_amount_donut_labels,
        "current_month_sessions_amount_donut_series": current_month_sessions_amount_donut_series,
        "sessions_count_per_type": sessions_count_per_type,
        "monthly_amounts_per_type": monthly_amounts_per_type,
        "sessions_by_hour_hours": sessions_by_hour['hours'],
        "sessions_by_hour_count": sessions_by_hour['counts'],
    }
    return render(request, 'dashboard/session.html', context)