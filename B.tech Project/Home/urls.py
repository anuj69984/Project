from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.Welcome,name="Welcome"),
    url(r'^Home/',views.Home,name="Home"),
    url(r'^Reunion/',views.Reunion,name="Reunion"),
    url(r'^Gallery/',views.Gallery,name="Gallery"),
    url(r'^AlumniMeet/',views.AlumniMeet,name="AlumniMeet"),
    url(r'^ContactUs/',views.ContactUs,name="ContactUs"),
    url(r'^Register/',views.Register,name="Register"),
    url(r'^RegisterAlumni/',views.RAlumni,name='AlumniR'),
    url(r'^RegisterStaff/',views.RStaff,name='StaffR'),
    url(r'^RegisterStudent/',views.RStudent,name='StudentR'),
    url(r'^Login/',views.Login,name="Login"),
    url(r'^RegisteredAlumni/',views.RegisteredAlumni,name="RegisteredAlumni"),
    url(r'^News&Notifications/',views.Notifications,name="News&Notifications"),
    url(r'^Association/',views.Association,name="Association"),
    url(r'^UpcomingEvents/',views.UpcomingEvents,name="UpcomingEvents"),
    url(r'^MakeAGift/',views.MakeAGift,name="MakeAGift"),
    url(r'^OtherLinks/',views.OtherLinks,name="OtherLinks"),
    url(r'^Chat/',views.chat,name="Chat"),
    url(r'^delete_chat/',views.delete_chat,name="delete_chat"),
    url(r'^Profile/',views.AlumniProfile,name="AlumniProfile"),
    url(r'^Sendmail/',views.Sendmail,name="SendMail"),   
]