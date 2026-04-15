import asyncio
from telegram_woocommerce import *


def main():
    username = "sa"
    team_name = "perspolis"
    league_name = "premiere_league"
    age_group = "adults"

    tw = TelegramWoocommerce()

    customer = tw.get_customer(username)

    if (len(customer) == 0):
        print("customer not exists")
        customer = tw.create_customer(username)
    else:
        print("customer exist")

    try:
        product_id = tw.get_filtered_product(team_name, league_name, age_group)
    except Exception as e:
        print(e)
        return

    order_detail = tw.create_order(customer["id"], [product_id], username)

    print(order_detail["payment_url"])

    # todo: not update order customer id currectly and should edit in function
    # print(tw.update_order(order_detail["id"], customer["id"]))

if __name__ == '__main__':
    main()
