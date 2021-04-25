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
hashtag_list = ["motivationalquotesi", "motivationalquoteslover", "motivationalquotesaboutlife", "dailymotivationalquote", "motivationalquotesinc", "motivationalquotesforstudents", "motivationalquotesempire", "quotebisnis", "quotesviral", "quoteofthedayy", "quoteshidup", "quotesbisnis", "bestmotivationalquotes", "quotesonlove", "quotesforwomen", "quotesofday", "quotessad", "quotescreator", "motivationalwednesday", "quotesmotivation", "quotesbaperan", "quotessholawat", "quoteoftheday❤️", "quotespelajar", "quotesabouthim", "quoteshariini", "quotesherex", "quoteofinstagram", "quotesanimeindonesia", "quotesabouther"]

# List of comments to be randonmly chosen from
comments_list = ['Nice Quote. Checkout my @quote.inme for motivational quotes!',
'Nice thought :) Check out mine also @quote.inme',
'Amazing~ for more post like this check out @quote.inme',
'Looks great! :) for amazing quotes check out @quote.inme',
'Beautiful stay happy with my @quote.inme page',
"follow @quote.inme to upleaft your soul, becouse only soul matters",
"Hey guys, hope you are doing great check out my quote page for dailly motivational quotes"]

# Number of posts to go through per hashtag
number_of_posts = 100

# Chance of commenting on photo
# i.e. chance_to_comment = 4 means a 1/4 chance
chance_to_comment = 2

# Time to wait in between processing instagram posts in seconds
# Enter lower and upper limit in randint()
wait_between_posts = randint(7, 13)

# Time to wait in between liking a post and commenting on it in seconds
# Enter lower and upper limit in randint()
wait_to_comment = randint(7, 15)