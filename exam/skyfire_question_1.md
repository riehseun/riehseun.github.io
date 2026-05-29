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

Thank you very much for your initial inveistion. It really helped me get started!

I would need to do some validation to idenity root cause of the problem, that is currently going on in production

For each user account that you've tested (flowerchild@60s.com, programmer@gizmo.com, avocado@hipmail.com, squadgoals@gmail.com, defaultdance@fortnitefan.com), I would like to perform the following validation

- Turn on one of social media (Facebook, Twitter, Linkedin, Instagram, Pinterest, Snapshot) and check which social media integration goes through for each email. This would validate if problem is related to particular social media integration
- If same email goes through one set of social media, but not others. We might need to narrow the investigation down to how that particualr social media integration had been implemented. They may have rule to accept some form of emails, but not others. We can even make logical guesses by comparing emails that worked for that particular social media and those that didn't work
- If an email does not go through for all social media integration, then I suspect the format of email cannot pass a common validation that these social media integration is using. We may need to compare our own email validation mechanism in our service against those used by social media integration to further investigate
- If there is social media that accepts all emails, we can (for short-term) only enable that particular social media integration in our service until the issue is fully addressed.

To prevent this issues going forward, we would need to understand email validation rules for all social media integrations and keep our own validation logic in sync

Also, rather than returning 500 when at least one of integration fails, we could update our service to fail more gracefully by creating individual calls to fetch profile from each social media, then combine profiles from social media where integration worked (For those that fails, we can log if for further investigation. We can use backfill jobs to pull down any missed social media profiles offline)

In additional to above, the integration services of social media can be down as well. We can implement health-check service before pulling down profiles using user email to understand if service itself is running 

**Ticket #9584 Comment** to Tamara (customer support colleague)

Hi Tamara,

We are really sorry for the outage that is happening in production. We are deligently working to identiy the root cause of the issue and implement a fix asap. We will keep you posted with our progress on this issue

Once the issue is addressed, we will also provide you with steps that we've taken to prevent this issue from happening in the future

Thanks,

Seungmoon


# What we liked

We liked that you used your understanding of the problem to propose a change that would address the issue.
We really liked that you proposed adding logging/monitoring to learn more about the issue or find it more quickly in the future.
We appreciated that you offered to follow up with your customer support colleague on the issue.

# Potential areas for improvement
Some of the best responses we saw made a bit more progress on diagnosing the underlying issue, which was related to invalid profile ids from certain social networks.
Some of the top responses documented more details that they found like specific error messages or ids. This would help teammates gain a shared understanding of the problem.