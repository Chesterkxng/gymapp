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

    # formating data for charts
    current_month_sessions_donut_labels= list(current_month_sessions_by_type.keys())
    current_month_sessions_donut_series = list(current_month_sessions_by_type.values())
    monthly_sessions_count = [month['count'] for month in monthly_sessions]

    context = {
        "current_month_sessions": current_month_sessions,
        "current_month_sessions_by_type": current_month_sessions_by_type,
        "current_month_sessions_donut_labels":  current_month_sessions_donut_labels,
        "current_month_sessions_donut_series": current_month_sessions_donut_series,
        "monthly_sessions_count": monthly_sessions_count
    }
    return render(request, 'dashboard/session.html', context)