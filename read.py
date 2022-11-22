from database import Session, Posts

session = Session()
posts = session.query(Posts).all()

for post in posts:
    print('---------------------- post ----------------')
    print(f'\n\n{post.post_url}\n{post.post_text}')

    print(' comments ')
    for comment in post.comments:
        print(f'\t\t{comment.commenter_name} ---> {comment.comment_text}')

    print('  retweets ')
    for retweet in post.retweets:
        print(f'\t\t{retweet.retweeter_name} ---> {retweet.retweeter_profile_url}')