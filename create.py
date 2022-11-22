from database import Base, engine, Session, Posts, Comments, Retweets


def store_into_database(post, comments, retweets):
    Base.metadata.create_all(engine)
    session = Session()
    # p1 = Posts(1, 2, 3, 'my url', 'my time', 'my post text')
    # c1 = Comments("my url 1", 'my name 1', 'my time 1', 'my comment text 1')
    # c2 = Comments("my url 2", 'my name 2', 'my time 2', 'my comment text 2')
    # c3 = Comments("my url 3", 'my name 3', 'my time 3', 'my comment text 3')
    post_values = list(post.values())
    post_obj = Posts(post_values[0],
                     post_values[1],
                     post_values[2],
                     post_values[3],
                     post_values[4],
                     post_values[5]
                     )
    if comments:
        comments_list = []
        for c in comments:
            c_values = list(c.values())
            comments_list.append(Comments(c_values[0],
                                          c_values[1],
                                          c_values[2],
                                          c_values[3]
                                          ))
        post_obj.comments = comments_list

    if retweets:
        retweets_list = []
        for r in retweets:
            c_values = list(r.values())
            retweets_list.append(Retweets(c_values[0],
                                          c_values[1],
                                          c_values[2]
                                          ))
        post_obj.retweets = retweets_list

    session.add(post_obj)
    session.commit()
    session.close()
