'''
This file stores variables detailing feature names.

Which features will I use in my project and which type are they?

I think I'd like to separate out the features based on their survey responses
in order to automate a lot of the cleaning.

Once I determine which survey responses are of what type (there seem to be <8 groups)
I can use those dictionaries (cryptic_feature_name: plain_english_description)
in my make_data_clean.py file.

As I work I am trying to think about how to write replicable, approachable code.

The feature name dictionaries will be great later as well. The current names of
each feature are not interpretable. Having dictionaries with their comprehendible
names will be super helpful for maintaining interpretability.

So far I have spent a lot of time going back to the data docs. These should help
alleviate this back and forth for me and help speed things up. :-D 
'''


frequencies = {}
unique_types = {}
ratings = {}
binaries = {}
continuous = {}
DIAGNOSIS = {}
