""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import random


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

session = InstaPy(username="#put your username here", 
                  password="#put your password here",
                  headless_browser=False)

comments = ["Nice! pls check out @sonal_tunes","love it! pls check out @sonal_tunes "]

with smart_run(session):
  hashtags = ["instasinger", "coversinger", "indiansinger" , "song" , "melodious"]
  random.shuffle(hashtags)
  
  session.set_action_delays(enabled=True,
                             like=30.31,
                             comment=35.12,
                             follow=45.85,
                             unfollow=56.26,
                             randomize=True,
                             random_range_from=50,
                             random_range_to=150)

  session.set_do_like(enabled=True, percentage=60)
  session.set_delimit_liking(enabled=True, max_likes=25, min_likes=0)
  session.set_do_comment(enabled=True, percentage=100)
  session.set_comments(comments)
  session.set_do_follow(enabled=True, percentage=10, times=1)
  session.set_dont_unfollow_active_users(enabled=True, posts=1)

  session.unfollow_users(amount=10,
                         nonFollowers=True,
                         style="FIFO",
                         unfollow_after=12 * 60 * 60, sleep_delay=501)

  session.set_quota_supervisor(enabled=True,
                               sleep_after=["likes", "comments", "follows", "unfollows", "server_calls"],
                               sleepyhead=True,
                               stochastic_flow=True,
                               notify_me=True,
                               peak_likes_hourly=45,
                               peak_likes_daily=560,
                               peak_comments_hourly=30,
                               peak_comments_daily=300,
                               peak_follows_hourly=30,
                               peak_follows_daily=500,
                               peak_unfollows_hourly=20,
                               peak_unfollows_daily=250,
                               peak_server_calls_hourly=200,
                               peak_server_calls_daily=2500)

  session.set_relationship_bounds(enabled=True,
                                  potency_ratio=None,
                                  delimit_by_numbers=True,
                                  max_followers=5000,
                                  max_following=5000,
                                  min_followers=40,
                                  min_following=40)

  
  session.like_by_tags(hashtags, amount=25, interact=False, skip_top_posts=True)
