# The hypothesis app

## What?
This currently is a few really simple scripts that store guesses and answers, with a little bit of extra data, as explained below:

### Guesses
When you make a guess(a.k.a. hypothesis), user will be prompted to enter the following fields:
1. a sentence about what your hypothesis is.
1. Confidence level
1. Notes, links, associated references

### Answers
When you answer, or resolve the guess, user will be prompted to enter the following fields:
1. result
1. explanation
1. lessons


## Why?
I have built this tool to speed up my own progress and learning by actually slowing it down and making it more intentional. When doing coding/engineering work, what is all-too-common is to get frustrated and make changes in haphazard fashion, which results in sub-optimal conditions, such as:
1. losing track of what I've tried
1. many git commits
1. many failing builds
1. wasted time
1. more frustration
1. 20 different browser tabs open
1. cussing
1. throwing things

What I've found is that by taking a moment to slow down and make my best guess about the cause or a problem, or the outcome of a given action, or potential solution - I often have more knowlege and insight hidden away than I realize, and the simple act of making a guess can unearth it and save me a lot of time and endless cycles of drudgery just 'trying things'.  Having a process for this calms my brain a little bit and keeps it from spinning out of control when trying to figure something out or get something to work.


## Example Scenarios
I have a proposed change to a service that I think will solve a problem, but not sure how to test it.  Rather than stare at my screen flipping between many windows hoping the answer will just come to me(possibly forgetting what I was after in the first place) - I type `guess` in my terminal to initiate the process.
```
$ guess
Name of entry : testing_change_to_config_validation_lambda
Enter your hypothesis : I can push my change to github, which will deploy my change to my dev environment, and I can modify my test stack build configuration to validate against the dev-environment lambda rather than the prod-environment validator.
What's your confidence level? : 5
any notes, links, etc? : <github commit link for change in question>
```

After making my guess and trying it out, at some point I'll resolve and close out that guess entry.
```
$ answer testing_change_to_config_validation_lambda
I can push my change to github, which will deploy my change to my dev environment, and I can modify my test stack build configuration to validate against the dev-environment lambda rather than the prod-environment validator.
result(correct, incorrect, mu): correct
explanation: That would work, however, the feedback loop could be drastically shortened by cutting out both builds by manually editing the lambda in the console, and using a curl command to send a test config to the lambda instead of running a whole test build.
lessons: The first idea is not always the best idea, and taking the time to figure how to shorten the feedback loop can save huge amounts of time and frustration in the long run.
```

## Commands: (really, just different scripts at this time):
- guess.py   # make a new guess
- guesses.py # print out all currently unresolved guesses
- answer.py  # resolve, or answer a guess
- answers.py # print all answers


## Future Vision/Features

How can this tool be improved and made more widely available for others to use?

### Dockerize
Containerizing this tool would make it much more portable and developer friendly.  A simple docker pull would let a developer get started right away.  The tool could be run locally and all guesses/answers stored locally.

### Data Use/Visualization
Aside from the above mentioned benefits, the guesses and answers stored could also be put to use.  Data could be displayed in a tool like Jupyter notebook to track information and trends, such as:
1. How many guesses per day(Making guesses is a healthy development practice, making a moderate amount of guesses per day is worth tracking)
1. Confidence level / result correlation - It might be interesting to draw a correlation between confidence levels of initial guess versus outcome(correct/incorrect). Or, maybe it wouldn't be that useful..
1. Answers and explanations - How can these be made easily searchable - if I i figure out something once, how can I make sure next time I run across the same question/problem, whatever answer I came up with is available to me later?

### Scalability(pie in the sky?)
Aside from making this into a publicly available repo/docker image, is this suitable for non-developers, in the form of a web gui?  This would require much more infrastructure:
- Having this run as a cloud service.
- All info stored in a database
- User registration
- Dashboard showing visualizations as described above.