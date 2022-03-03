## Data Science & Machine Learning Discussion Group
### 23 November 2017
RSVPs: 45 | Waiting: 0 | Event Type: physical | [Meetup Event Link](https://www.meetup.com/Data-Science-Discussion-Auckland/events/241871346)

This week we will be discussing the Porto Seguro Kaggle Competition at a high level and will discuss team formation.

https://www.kaggle.com/c/porto-seguro-safe-driver-prediction

Please look at the competition and attempt it before coming to the meetup. The real value from this group comes from when people give the competition some effort and can come to the meetup with their ideas and questions that came up for them.

Tony has provided instructions below * for how to get started using R if you are new to Kaggle. The purpose of this meetup is to attempt the competition and use the discussion time to comment, share ideas and ask questions.

This week we encourage you to bring the results of your model to the meetup so that we can share them and each take them away to ensemble for a group submission. See instructions for this below ** You must follow these instructions closely for this to work.

Note: In order to comply with the Kaggle rules we will not be sharing any executable code unless it is also shared publicly on the Kaggle website.

Meeting Schedule:

6:00 - 6:30 - Arrive at venue

6:30 - Introductions

6:35 - Discussion - Porto Seguro Kaggle competition

7:30 - Decide on what to talk about at next meeting

7:40 - Meeting ends

Thank you to GridAKL for providing the venue!

* Here are the instructions to install R:

Download R from https://mran.microsoft.com/download/ and install it
Download the free RStudio Desktop https://www.rstudio.com/products/rstudio/download/ and install it
Run Rstudio
Inside RStudio open the R kernel that you downloaded from Kaggle and make sure the kernel is accessing the right location for the train.csv and test.csv you downloaded from Kaggle
Run the kernel and send the submission file that it created to Kaggle

** Instructions for joining the team to ensemble

1) There are 595212 rows of training data. Split these rows into a training set and a holdout set using id > 1338765 as the holdout
set. This will produce a training set of 535691 rows and a holdout set of 59521 rows. Put the holdout set aside. Don't use it for
anything related to your model. Don't use it for feature engineering or validation or ANYTHING.

2) Fit your model using the 535691 rows of the training set.

3) Use the model from (2) to predict the 59521 rows of the holdout set. Save the probabilities into a two column csv file with
headers id,target and name the file yourname.yourmodel.yourscore.holdout.csv

4) combine the training data and holdout data into the original 595212 rows of training data

5) repeat step (2) with this new training data - use the same method to fit as in (2) to make sure that the model is the same as (2)
but with the benefit of the extra data

6) Use the model from (5) to predict the 892816 rows of the Kaggle test set. Save the probabilities into a two column csv file with
headers id,target and name the file yourname.yourmodel.yourscore.test.csv

7) Submit that csv file to Kaggle and record the score

8) Bring both csv files and the score along to the next meeting and also put them in the Dropbox repository https://www.dropbox.com/request/Y97jOmZpK4sJMuIjVJEZ and be prepared to
say a few sentences about what you did

All models are useful even if they score low. "Weak learners" can be built into strong learners. So don't worry about your score.

Bring along more models if you want - but try to bring at least one.
