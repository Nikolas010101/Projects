from Booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    # bot.change_currency()
    bot.select_destination('São Paulo')
    bot.select_date(checkin='2022-03-20', checkout = '2022-04-16')