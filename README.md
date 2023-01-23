# TriHarmony

TriHarmony

Project Overview

TriHarmony is a site aimed at therapists and behavioral specialists working with families with young children. It is a way for the specialist to collect data for the child - the parent provides the child’s behavior data, and the child provides their own feeling data. 

The ideal goal would be daily check-ins for both parent and child, that record data that can then be shared with their specialist to inform their treatment plan. The site has three parts: specialist, parent, child. The user will choose which they are on the login page. 

On the parent/caregiver side, the app will allow the parent to log in and complete the data form themselves and send it directly to the specialist. The app also serves as a way for the parents to contact the specialist. 

The child’s side contains a feelings chart with different faces or emojis indicating a mood. The child will choose what mood they feel like. This will be time stamped and added to their data. There will also be a spot for the child to journal and video links to entertaining feelings-based videos and activities. There will also be a rewards system implemented on the child’s page. The child can submit their feelings multiple times a day, but they will get one  star for every day they submit. At 10 stars, they earn a reward. Actual reward will be determined with the specialist. This is to reinforce the child providing the data.

The specialist’s side will contain all the parent and child data. The specialist will be able to choose a client, and see a dashboard for each child with their data, a spot for notes, and an email form for parent communication.

What problems is it trying to solve?
This app is to improve communication between children, their parents, and their specialist. It will serve as a repository for behavior data and the child’s feelings data. A specialist can present the app to the family and show them how to use it, and make it a part of an official treatment plan, if applicable.
I formerly worked as a counselor, therapist, and behavior consultant specialist, and would need to collect data as often as possible. TriHarmony is intended to simplify this data collection.
TriHarmony gives children a voice - they can make notes about their feelings they might not feel comfortable saying out loud, which may give context to some behaviors reported by caregivers. They also have access to a private journal and videos to help teach them about feelings.

Frameworks:
	Django will be used to provide views for parent, child, and specialist.

User Stories:

As a counselor/therapist/behavior specialist, I need to collect as much data as possible to get a clear picture of what is happening with the child. I rely on parents reporting how their child behaves at home. 
Tasks:
Provide parents with form to collect behavior data
Data will be time-stamped
Display scores on specialist dashboard (eventually will be charts)

As a counselor/therapist/behavior specialist, I want to know how a child is feeling day to day, and in different situations. This provides a way for the child to record their own data, without worry of parents influence. I want the child to be motivated to use the site. The child earns a star every time they record their feelings, and after 10 stars (for example) will earn a prize. This will reinforce the child using the site. 
Tasks:
Provide children with feelings chart to collect feelings data
Data will be time stamped

As a specialist, I want to be able to see each family’s data together, with times and dates, in order to get a bigger picture. 
Tasks:
Store data in database
Display data in charts.
______________

Data Models

class Child:
name, age, date of birth, gender, specialist


class Feeling:
name


class Child Entry:
child, feeling, rating, date, notes


class Specialist:
name, email


class Parent:
name, email, child, specialist


class Parent Entry:
child, rating, date, notes, specialist, parent

_______________________
Milestone 1:

Specialist:
form to parent, 
form to child, 
client database

Child:
form to specialist

Parent:
form to specialist, 
contact specialist
_______________________

Milestone 2:

Specialist:
notes section in database

Child:
journaling section, 
star chart for tracking

Parent:
notes section

	
_____________________

Milestone 3:

Specialist:
display data in charts

Child:
section with video links

Parent:
display child's data graph
_______________________

Schedule

1/23-1/28

Login page, 
Create Specialist app: 
	behavior rating forms, 
	feelings charts, 
	dashboard
  
1/29-2/2

Create Parent app: 
	behavior rating form, 
	contact form
  
2/3-2/8

Create Child app: 
	feelings chart, 
	journaling space, 
  tracker
  
2/9-2/14

Styling

Post-capstone: 

TriHarmony will also be a place to hold the family at-home rewards system, if they use one. Containing the behavior expectations and rules. It will be where the family records the child’s stars or whatever they use in their system. The child’s app will also allow them to record reward ideas/suggestions to keep them motivated. 

