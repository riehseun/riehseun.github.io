# Social media integration (FB, Twitter, Instagram) with the app is broken. How do you investigate

A few months ago, your team released a feature to pull in some social media profile information when a new user is added to the system. An email is provided to a third-party library, which then pulls down some basic information from Facebook, Twitter, LinkedIn, Instagram, Pinterest, and Snapchat.

You come into work one morning and check your email and see the following message from Casey, a senior software engineer on your team:

Hey, something might be up with the social media integration... Do you have any time to take a look at this today? Just want to make sure it's not too big of an issue. Here's a [link] to the bug report. Thank you!

Casey was able to narrow the bug down to one area of code, and even provided some test cases for you to work with to get started. The two accounts in TestSomeUsersThatWork are working as expected and saving successfully. The three accounts in TestSomeUsersThatFail should be saving, but they are not, which is why they incorrectly return false right now.

Debug the issue

The data is being stored in a PostgreSQL database. You do not have the time or system access needed to fix this bug, but you can make progress and recommend a fix.

Document what you learned

Whether or not you have identified the issue, stop with ~5 minutes left and spend 5-10 minutes on communication. You will be passing this info to another engineer for continued debugging/fixing, so consider what might be helpful to them. (Who knows, that other engineer might be Future You™!)

Enter your response in the "Your Notes" tab (in the upper-right quadrant). You will write two responses:

An email back to Casey with any technical details on what the issue is or how to solve it
A comment on the support ticket to give Tamara the information she needs to help the customer make progress.


**From**: You
**To**: Casey (senior engineer teammate)
**Subject**: re: User creation error
Hi Casey,

Thank you very much for your initial investigation. It really helped me get started!

I would need to do some validation to identity root cause of the problem, that is currently going on in production

For each user account that you've tested (flowerchild@60s.com, programmer@gizmo.com, avocado@hipmail.com, squadgoals@gmail.com, defaultdance@fortnitefan.com), I would like to perform the following validation

- Inspect "profile" object returned by "fetch_social_profiles" call
- For example, user "avocado" has instragram profile id being "24ab21dd47a7" and snapshot profile id being "3af170bb82d6", which are likely invalid. 
- User "squadgoals" also has instagram and snapshot profile id containing letters. 
- In fact, the "result" object mentions that the error is "invalid input syntax for integer: 2eddba8ac85e'", which further suggest invalid profile id to be the culprit 
- Furthermore, users whose test worked have returned profile ids containing only numbers
- Verify this by turning off Instagram and snapshot integration for these users and try retrieving & saving their profiles 

To prevent this issues going forward, we would need to ensure that data stored in post SQL is correct. We can run periodic data quality check on our DB using pre-defined rules (For example, profile id should only contain nubmers) and correct any invalid data before any issues occur in production 

Also, rather than returning "success: False" when at least one of integration fails, we could update our service to fail more gracefully by creating individual calls to fetch profile from each social media, then combine profiles from social media where integration worked (For those that fails, we can log if for further investigation. We can use backfill jobs to pull down any missed social media profiles offline)

In additional to above, the integration services of social media could be down as well at any time. We can implement health-check service to perform period checks on whether service itself is running 

**Ticket #9584 Comment** to Tamara (customer support colleague)

Hi Tamara,

We are really sorry for the outage that is happening in production. We are diligently working to identify the root cause of the issue and implement a fix asap. We will keep you posted with our progress on this issue

Once the issue is addressed, we will also provide you with steps that we've taken to prevent this issue from happening in the future

Thanks,

Seungmoon
