from random import randint

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
***IMPORTANT***

Please be aware of Instagram's daily limits for likes and comments to avoid getting banned

https://socialpros.co/instagram-daily-limits#Instagram%E2%80%99s_Daily_Limits_in_2020

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Local path to chrome driver
chromedriver_path = "C:/chromedriver.exe"


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Make adjustments below to tweak the bot to your liking

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# List of hashtags to go through
#hashtag_list = ['motivationalquotes', 'quoteoftheday', "quoteforlife", "lovequotes"]
#hashtag_list = ["motivationalquotesi", "motivationalquoteslover", "motivationalquotesaboutlife", "dailymotivationalquote", "motivationalquotesinc", "motivationalquotesforstudents", "motivationalquotesempire", "quotebisnis", "quotesviral", "quoteofthedayy", "quoteshidup", "quotesbisnis", "bestmotivationalquotes", "quotesonlove", "quotesforwomen", "quotesofday", "quotessad", "quotescreator", "motivationalwednesday", "quotesmotivation", "quotesbaperan", "quotessholawat", "quoteoftheday❤️", "quotespelajar", "quotesabouthim", "quoteshariini", "quotesherex", "quoteofinstagram", "quotesanimeindonesia", "quotesabouther"]
#hashtag_list = ["quotes", "motivationalquotes", "motivational", "quotestoliveby", "lovequotes", "quotestagram", "inspirationalquotes", "lifequotes", "quotesoftheday", "quotesaboutlife", "quotesdaily", "quotesindonesia", "successquotes", "motivationalspeaker", "islamicquotes", "positivequotes", "instaquotes", "dailyquotes", "motivationalquote", "quotestags", "quotesofinstagram", "quotesgram", "quotesandsayings", "hindiquotes", "motivationalmonday", "relationshipquotes", "quotescinta", "quotesgalau", "sadquotes", "quotesforlife"]
hashtag_list = ["photooftheday", "picoftheday", "bestoftheday", "instadaily", "instapic", "lifestyle", "nature", "adventure", "landscape", "wildlife", "life", "naturelovers", "beautiful", "travel", "wanderlust", "work", "photography", "sunset", "quotes", "instagram", "fashion", "outdoors", "travelphotography", "summer", "style", "love", "selflove", "model", "view", "elegant"]

# List of comments to be randonmly chosen from
"""
comments_list = ['Nice Quote. Checkout my @quote.inme for motivational quotes!',
'Nice thought :) Check out mine also @quote.inme .',
'Amazing~ for more post like this check out @quote.inme .',
'Looks great! :) for amazing quotes check out @quote.inme .',
'Beautiful stay happy with my @quote.inme page',
"follow @quote.inme to upleaft your soul, becouse only soul matters",
"Hey guys, hope you are doing great check out my quote page for dailly motivational quotes"]
"""

comments_list = ['Nice Quote. Checkout my @get_premium_followers1m to gain real followers!',
'Nice thought :) Check out mine @get_premium_followers1m to grow your real followers.',
'Amazing~ for more post like this check out @quote.inme .',
'Looks great! :) for amazing quotes check out @quote.inme .',
'Beautiful stay happy with my @quote.inme page',
"to incress the followes dm me @get_premium_followers1m ."]

# Number of posts to go through per hashtag
number_of_posts = 10

# Chance of commenting on photo
# i.e. chance_to_comment = 4 means a 1/4 chance
chance_to_comment = 1

# Time to wait in between processing instagram posts in seconds
# Enter lower and upper limit in randint()
wait_between_posts = randint(7, 13)

# Time to wait in between liking a post and commenting on it in seconds
# Enter lower and upper limit in randint()
wait_to_comment = randint(7, 15)