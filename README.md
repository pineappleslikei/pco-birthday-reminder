# Thanks for checking out pco-birthday-reminder!

This application will generate an email reminder indicating any upcoming team birthdays. These birthdays fall into 2 categories:
1. occur this week before the next plan dates
2. the person is scheduled this weekend and its the last time before their birthday

pco-birthday-reminder is intended to be deployed on a cloud service where it can be a scheduled task.

The scheduler module is included for services such as "pythonanywhere" that might allow daily tasks but not weekly.

## Getting Started
#### You'll need:
1. Planning Center Account
    Generate an app id and key at https://api.planningcenteronline.com/oauth/applications.
2. Gmail Account
    Go to "google->account->security->signing into google->app passwords" and generate an app password. Drop both of these into their respective places in the credentials module.
