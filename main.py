import asyncio
import telegram
from telegram_woocommerce import *

# async def main():
#     bot = telegram.Bot("8274731879:AAG00TvwxuNRQaT3LOZKbL6ihAFP2duHXj4")
#     async with bot:
#         print(await bot.get_me())



# if __name__ == '__main__':
#     asyncio.run(main())

username = "sadfasfdasfsdfsafasfsaf"
team_name = "perspolis"
league_name = "premiere-league"
age_group = "adults"

tw = TelegramWoocommerce()

customer = tw.get_customer(username)
if (len(customer) == 0):
    print("customer not exists")
    customer = tw.create_customer(username)
else:
    print("customer exist")

product_id = tw.get_filtered_product(team_name, league_name, age_group)[0]["id"]


print(tw.create_order(customer["id"], [product_id])["payment_url"])