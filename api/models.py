from django.contrib.auth.models import AbstractUser
from django.db import models

Filled = "filled"
Partial = "partial"
Assigned = "assigned"
Cancelled = "cancelled"
Rescheduled = "re-scheduled"

Pending = "pending"
Confirmed = "confirmed"
Denied = "denied"

Patrol = "Pat"
Sgt = "Sgt"
Lt = "Lt"
Command_Staff = "Cmd"

Text = "text"
Email = "email"
Both = "both"
No_contact = "none"

Voluntary = "voluntary"
Forced = "forced"

DAY = "day"
MID = "mid"
NIGHT = "night"

signup_status = {
    Pending: "Pending",
    Confirmed: "Confirmed",
    Denied: "Denied"
}

post_status = {
    Filled: "filled",
    Partial: "partial",
    Assigned: "assigned",
    Cancelled: "cancelled",
    Rescheduled: "rescheduled"
}

Assignment_type = {
    Voluntary: "Voluntary",
    Forced: "Forced"
}

Role_Status = {
    Patrol: "Patrol",
    Sgt: "Sergeant",
    Lt: "Lieutenant",
    Command_Staff: "Command Staff"
}

Contact_status = {
    Text: "text",
    Email: "email",
    Both: "both",
    No_contact: "none"
}

# Shift_choices = {
#     DAY: "Day",
#     MID: "Midshift",
#     NIGHT: "Night"
# }


class Users(AbstractUser):
    badge_num = models.IntegerField(unique=True, null=True)
    hours = models.FloatField(default=0.0)
    pin = models.CharField(max_length=10)
    phone = models.CharField(max_length=15, blank=True, default="")
    contact_method = models.CharField(
        max_length=10,
        choices=Contact_status,
        default=No_contact
    )
    role = models.CharField(
        max_length=3,
        choices=Role_Status,
        default=Patrol
    )
    # shift = models.CharField(max_length=5, choices=Shift_choices, default=DAY)
    # is_eligible = models.BooleanField(default=True)
    # hire_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.badge_num})"


class OvertimePost(models.Model):
    overtime_id = models.AutoField(primary_key=True)
    work_order = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField()
    shift = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    hours = models.FloatField()
    location = models.CharField(max_length=50)
    personnel = models.IntegerField()
    notes = models.CharField(max_length=200, blank=True, default="")
    status = models.CharField(max_length=15, choices=post_status, default=Partial)
    had_forced = models.BooleanField(default=False)


class Signup(models.Model):
    overtime = models.ForeignKey(OvertimePost, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='assignments_made')
    status = models.CharField(max_length=15, choices=signup_status, default=Pending)
    assigned_at = models.DateTimeField(auto_now_add=True)
    assignment_type = models.CharField(max_length=10, choices=Assignment_type, default=Voluntary)
    notification_sent = models.BooleanField(default=False)
    notification_sent_at = models.DateTimeField(null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    confirmed_at = models.DateTimeField(null=True, blank=True)