from core import bot, settings


if __name__ == "__main__":
    try:
        bot.run(settings.DISCORD_TOKEN)

    except KeyboardInterrupt:
        print("finalizando o bot...")
