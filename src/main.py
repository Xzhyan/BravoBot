# core
from core import bot, settings
from core.logger import addlog


if __name__ == "__main__":
    try:
        bot.run(settings.DISCORD_TOKEN)

    except Exception as e:
        addlog('errors', str(e))

    except KeyboardInterrupt:
        print("[INFO] finalizando...")
