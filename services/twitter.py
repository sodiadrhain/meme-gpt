# import asyncio

# from twikit import Client

# ###########################################

# client = Client('en-US')

# async def main():
#     # Asynchronous client methods are coroutines and
#     # must be called using `await`.
#     await client.login(
#         auth_info_1=USERNAME,
#         auth_info_2=EMAIL,
#         password=PASSWORD
#     )

#     ###########################################
# asyncio.run(main())

import asyncio

from twikit.guest import GuestClient

client = GuestClient()


async def main():
    # Activate the client by generating a guest token.
    await client.activate()

    # # Get user by screen name
    # user = await client.get_user_by_screen_name('elonmusk')
    # print(user)
    # Get user by ID
    # user = await client.get_user_by_id('44196397')
    # print(user)


    user_tweets = await client.get_user_tweets('the_marcoli_boy')
    print(user_tweets)

    # tweet = await client.get_tweet_by_id('1876880904917803386')
    # print(tweet)

asyncio.run(main())