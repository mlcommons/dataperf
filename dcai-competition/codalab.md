% display image / width=1300
[dataset Data-Centric-AI..logo-set-04.png]{0x6377655228e84f548898913ab2d7c751}

# Introduction

A collaboration between DeepLearning.AI and Landing AI, the Data-Centric AI Competition aims to elevate data-centric approaches to improving the performance of machine learning models. In most machine learning competitions, you are asked to build a high-performance model given a fixed dataset. However, machine learning has matured to the point that high-performance model architectures are widely available, while approaches to engineering datasets have lagged. The Data-Centric AI Competition inverts the traditional format and instead asks you to improve a dataset given a fixed model. We will provide you with a dataset to improve by applying data-centric techniques such as fixing incorrect labels, adding examples that represent edge cases, apply data augmentation, etc. Contestants must submit their altered dataset for evaluation by September 4, 2021. (We picked this date because it is the birthday of John McCarthy, who had coined the term artificial intelligence!) The top three winners from each of the two categories (Best Performance Overall and Most Innovative) will be invited to a private event with Andrew Ng to share ideas about how to grow the data-centric movement, and will be highlighted in The Batch and other DeepLearning.AI and Landing AI channels. Good luck!







In this tutorial, we will cover the process of submitting your dataset and results for official evaluation on the Data-Centric AI Competition. Once your dataset has been evaluated officially, your scores will be added to the [leaderboard](https://https-deeplearning-ai.github.io/data-centric-comp/?utm_source=linkedin&utm_medium=social&utm_campaign=dc-ai-competition&utm_content=dl-ai). Before we begin, please create a [CodaLab Worksheets account](https://worksheets.codalab.org/). **Be sure to create a CodaLab *Worksheets* account, not to be confused with a standard CodaLab account.**







# Rules

- Maximum 5 submissions per week (65 total over the course of the competition)
- Submission must have less than 10,000 images combined in training and validation
- Only one CodaLab account per team
    - *Companies that want to make an official submission using the company name/brand should direct message us on [Discourse](https://discourse.deeplearning.ai/c/competitions-dlai/data-centric-ai/50)*

**Submissions will be evaluated according to two categories:**
1. **Best Performance Overall**
2. **Most Innovative**





# Getting started






First, download the dataset by clicking into the bundle (click the uuid `0xcea1d7`) and press the download button. The dataset contains ~3000 images of handwritten roman numerals 1-10. **Your task is to optimize model performance by improving the dataset and making training and validation splits.**
% display image / width=1300
[dataset Screen-Shot-202..10.46.05-AM.png]{0xfa76dea4d62143a78e4b6e597a15ce5e}

[dataset data]{0xcea1d733e1f144d9aba83929af51f191}





Your submission should be a zip file with the following file structure, and with your training and validation data split into different folders. You can rename `sample_submission` whatever you like, but *the name of your zip file should match your folder name*. In this example, it should be called `sample_submission.zip`. When the zip file is expanded, the file structure and names inside must match the following:

    sample_submission/
        train/
            i/
            ii/
            iii/
            iv/
            ...
        val/
            i/
            ii/
            iii/
            iv/
            ...


You can try fixing incorrect labels, adding data for side case tuning, apply data augmentation techniques, or use any other method to improve the data. You may also find it helpful to take a look at the training script to get a better sense of the preprocessing and model (these are held fixed). The script will resize all images to `(32, 32)` and run them through a cut off ResNet50.
[dataset train.py]{0x57030e4a2d034af4b8efa38df4ff6af6}


If you choose to create your own data, you may find this script helpful for converting your images:
[dataset convert.py]{0x3a2514052d9240ffa24774a7092b82b8}

We also provide you with a label book that has five examples for each label. You can use it as a sample test set as you create your submission:
[dataset label_book]{0xe1d24af2ca5e4d95be653f1c7877125e}













# Submission

**Because we use automated evaluation to score your submission, please follow the steps in this tutorial exactly to ensure proper submission.**








#### Step 1: Upload improved training data


Go to your CodaLab profile and make a new worksheet.
% display image / width=300
[dataset Screen-Shot-202..-3.55.39-PM.png]{0xc8240916e4444213b4bdc785ceaea0ae}

Name it whatever you like, and upload your submission folder by clicking the `upload` button on the tool bar. **Make sure you upload the folder as a zip file.**
% display image / width=600
[dataset Screen-Shot-202..-3.57.42-PM.png]{0xff953857e3b04f88ba6815dd728a7c6f}





#### Step 2: Copy standard bundles into your worksheet









Go into the `web interface terminal` (click the `show terminal` button on the right side of the toolbar) and enter the following commands:
% display image / width=1000
[dataset Screen-Shot-202..-7.58.10-PM.png]{0x4b37b3eca3024a5b8a8641e714750970}

    cl add bundle data-centric-utils//train.py

    cl add bundle data-centric-utils//label_book






#### Step 3: Make a run bundle to get predictions on the label book

Next, train the standard model on your submission data to make predictions on the label book. Use the following command in the `web interface terminal`:

    cl run :train.py :<submission-file-name> :label_book 'python train.py <submission-file-name> label_book' -n run-train --request-docker-image jupyter/tensorflow-notebook


**Be sure to change the `<submission-file-name>` field to the name of your folder.** For example, for if you uploaded a zip file named `sample_submission.zip`, you would change the fields to `sample_submission`:

    cl run :train.py :sample_submission :label_book 'python train.py sample_submission label_book' -n run-train --request-docker-image jupyter/tensorflow-notebook

You should see a run-bundle like the following appended to the contents of your worksheet. If the bundle fails, reach out on [Discourse](https://discourse.deeplearning.ai/c/competitions-dlai/data-centric-ai/50) and we can help you out.
[run run-train -- :train.py,:data,:label_book : python train.py data label_book]{0x2decee5053e544e8bce21275026bc062}

#### Step 4: Extract predictions file


Next, extract out the predictions file into a bundle of its own. Run the following command in your `web interface terminal`:

    cl make run-train/predictions.json -n <your-submission-name>

Your `<your-submission-name>` should not contain spaces (avoid using special characters too). For example: `cl make run-train/predictions.json -n sample-submission`. You should see a bundle like the following appended to the contents of your worksheet:
[make sample_submission -- run-train/predictions.json]{0xeb0b8c13485d4104ba01050cd101196f}










#### Step 5: Tag your submission and add description

You're almost there! Give your submission a description. First, click into the `<your-submission-name>` bundle by clicking the small arrow next to the uuid and modify the `Description field` on the right sidebar.


% display image / width=850
[dataset Screen-Shot-202..11.18.14-AM.png]{0x690a2aef651d4add9ec3e803a2c577ab}

 Please use the following convention for the bundle description to identify your submission on the leaderboard:
% display image / width=250

    <your-submission-name> (Institution) optional_http_link


### ***You must have a properly formatted description to see your score on the leaderboard!!***

Some examples of properly formatted descriptions (`<your-submission-name>` cannot have any spaces!):
[Here](https://worksheets.codalab.org/worksheets/0x48ac66ba7d99418d9a2560082e800bcb) is an example of a successful submission. **NOTE: all bundles and worksheets have the permission `public: read`. If your bundle does not have the proper submissions, our competition script cannot read it. You can change the permissions on your submissions after you see it on the leaderboard.**
- sample_submission ( )
- sample_submission (DeepLearning.AI)
- sample_submission (DeepLearning.AI) https://www.deeplearning.ai/


You're now finally going to add the `mnist-roman` flag to mark the bundle as ready for submission. Run the following command:

    cl edit <your-submission-name> --tags mnist-roman

[Here](https://worksheets.codalab.org/worksheets/0x48ac66ba7d99418d9a2560082e800bcb) is an example of a successful submission.

**NOTE: all bundles and worksheets have the permission `public: read`. If your bundle does not have the proper submissions, our competition script cannot read it. You can change the permissions on your submissions after you see it on the leaderboard.**

#### Step 6: Fill out Google Form

**Fill out this [Google Form](https://docs.google.com/forms/d/e/1FAIpQLScpcF8UNtYKGkYUf0OPeWJxQJCC7zEjIl7E-huio7bRAhgnUw/viewform) so we can contact you and you are done!!** Congratulations! Please give us a couple days to evaluate your submission and add it to the leaderboard.

# More Information

If you have any questions or want to form teams with others, join us on Discourse. Click [here]((http://bit.ly/dlai-competition) to join if you are a new user, and [here](https://discourse.deeplearning.ai/g) if you are an existing user. Navigate to the Data-Centric AI Competition category to see announcements and post your questions!

Note: we reserve the right to disqualify anyone suspected of cheating.






