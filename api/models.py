from django.db import models


Filled = "filled"
Partial = "partial"
Assigned = "assigned"
Cancelled = "cancelled"
Rescheduled = "re-scheduled"

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

Pending = "pending"
Confirmed = "confirmed"
Denied = "denied"
 
signup_status = {
    Pending: "Pending",
    Confirmed: "Confirmed",
    Denied: "Denied"
}

post_status = {
    Filled: "filled",
    Partial:"partial",
    Assigned:"assigned",
    Cancelled:"cancelled",
    Rescheduled:"rescheduled"
}

Assignment_type = {
    Voluntary: "Voluntary",
    Forced: "Forced"
}

Role_Status = {
    Patrol: "Patrol",
    Sgt: "Seargent",
    Lt: "Lieutenant",
    Command_Staff: "Command Staff"
}

Contact_status = {
    Text: "text", 
    Email:"email",
    Both:"both",
    No_contact:"none"
}

# Create your models here.
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
    status = models.CharField(max_length=15,choices=post_status, default=Partial)
    had_forced = models.BooleanField(default=False)



class Users(models.Model):
    badge_num = models.IntegerField(unique=True) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hours = models.FloatField(default=0.0)
    pin = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    contact_method = models.CharField(
        max_length= 10, 
        choices= Contact_status,
        default=No_contact
    )
    role = models.CharField(
        max_length=3,
        choices= Role_Status,
        default=Patrol                                  
    )

    #TODO: maybe put in a shift option and an eligibitly option 

class Signup(models.Model):
    #TODO - have a status for the assignemnet so that people know whats available 
    overtime = models.ForeignKey(OvertimePost, on_delete=models.CASCADE)       
    user = models.ForeignKey(Users, on_delete=models.CASCADE)                 
    assigned_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name='assignments_made')

    status = models.CharField(max_length=15, choices=signup_status, default=Pending)
    assigned_at = models.DateTimeField(auto_now_add=True)
    assignment_type = models.CharField(max_length=10,choices=Assignment_type, default=Voluntary)
    notification_sent = models.BooleanField(default=False)
    notification_sent_at = models.DateTimeField(null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    confirmed_at = models.DateTimeField(null=True, blank=True)